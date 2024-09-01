from django.shortcuts import render
from .models import Information
from .forms import VolunteerApplicationForm, ContactForm
from news.models import Posts, Tags, Categories

def home_view(request):
    if request.method == 'POST':
        volunteer_form = VolunteerApplicationForm(request.POST)
        contact_form = ContactForm(request.POST)
        if volunteer_form.is_valid():
            volunteer_form.save()
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
    context = {
        'news': Posts.objects.all()[:2],
        'categories': [category for category in Categories.objects.all() if category.post_count() > 0],
        'info': Information.objects.first(),
        'tags': Tags.objects.all(),
        'volunteer_form': VolunteerApplicationForm,
        'contact_form': ContactForm,
    }
    return render(request, 'index.html', context=context)