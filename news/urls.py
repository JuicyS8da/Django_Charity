from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:post_slug>', views.PostView.as_view(), name='post'),
    path('tag/<slug:post_tag_slug>', views.TagPostListView.as_view(), name='post_tag'),
    path('category/<slug:post_category_slug>', views.CategoryPostListView.as_view(), name='post_category'),
    path('search/', views.search_view, name='search')
]