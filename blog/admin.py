from django.contrib import admin
from .models import Article,Tag
# Register your models here.

admin.site.register(Tag)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','author','tag','created_at','updated_at')
'''
class TagInline(admin.StackedInline):
    model = Tag

    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)


class ArticleInline(admin.StackedInline):
    model = Article


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    list_display = ('name',)
'''
admin.site.register(Article,ArticleAdmin)
