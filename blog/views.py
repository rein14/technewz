from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Article, Tag
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class ArticleList(generic.ListView):
    model = Article
    template_name = "articles.html"
    paginate_by = 10
    context_object_name = "article_list"

    def get_queryset(self):
        return Article.objects.all().filter(publish=True)

'''
class ArticleShort(generic.ListView):
    queryset = Article.get_short_article
'''


class BlogDetail(generic.DetailView):
    Model = Article
    template_name = "articles_details.html"
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(publish=True)


class TagList(generic.ListView):
    Model = Tag
    template_name = "Categories.html"
    context_object_name = "tag_list"

    def get_queryset(self):
        return Tag.objects.all()


class TagsTemp(generic.TemplateView):
    template_name = "Categories.html"

    def all_tags(self):
        return Article.objects.all().filter(tag=Tag.pk)
