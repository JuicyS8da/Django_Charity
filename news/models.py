from django.db import models
from django.db.models import Count, F
from django.conf import settings
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    categories = models.ManyToManyField('Categories', related_name='cat_posts')
    tags = models.ManyToManyField('Tags', related_name='tag_posts')
    picture = models.ImageField(unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug}) #post/cool-post/
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Categories(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("post_category", kwargs={"post_category_slug": self.slug})
    
    def post_count(self):
        return self.cat_posts.count()
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Tags(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("post_tag", kwargs={"post_tag_slug": self.slug})
    
    def post_count(self):
        return self.tag_posts.count()
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'