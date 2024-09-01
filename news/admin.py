from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Posts, Tags, Categories

class PostsAdmin(ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("categories", "tags")
    search_fields = ("content",)
    prepopulated_fields = {'slug': ('title',)}

class TagsAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    def has_module_permission(self, request): # to hide model in admin
        return False

class CategoriesAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    def has_module_permission(self, request): # to hide model in admin
        return False

admin.site.register(Posts, PostsAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Categories, CategoriesAdmin)