from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView, View
from .models import Posts, Tags, Categories
from home.models import Information

class BaseContextMixin(View):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['categories'] = [category for category in Categories.objects.all() if category.post_count() > 0]
        context['recent_news'] = Posts.objects.all()[:2]
        context['info'] = Information.objects.first()
        return context

class PostView(BaseContextMixin, DetailView):
    model = Posts
    template_name = 'news-detail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['related_news'] = Posts.objects.order_by('?').exclude(title=kwargs['object'].title).all()[:2]
        return context

class PostListView(BaseContextMixin, ListView):
    model = Posts
    template_name = 'news.html'
    context_object_name = 'posts'

class TagPostListView(BaseContextMixin, ListView):
    model = Posts
    template_name = 'news.html'
    context_object_name = 'posts'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Posts.objects.filter(tags__slug=self.kwargs['post_tag_slug'])

class CategoryPostListView(BaseContextMixin, ListView):
    model = Posts
    template_name = 'news.html'
    context_object_name = 'posts'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Posts.objects.filter(categories__slug=self.kwargs['post_category_slug'])

# class SearchView(BaseContextMixin, View):
#     model = Posts
#     template_name = 'news.html'
#     context_object_name = 'posts'
    
#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         if self.request.method == 'POST':
#             searched = self.request.POST.get('searched')
#             results = Posts.objects.filter(content__contains=searched)
#             context['searched'] = searched
#             context['posts'] = results
#         return context

def search_view(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        results = Posts.objects.filter(content__contains=searched)
        context = {
            'tags': Tags.objects.all(),
            'categories': [category for category in Categories.objects.all() if category.post_count() > 0],
            'info': Information.objects.first(),
            'searched': searched,
            'posts': results,
        }
        return render(request, 'news.html', context=context)
    else:
        return render(request, 'news.html')