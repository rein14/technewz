from django.contrib.syndication.views import Feed
from .models import Article
from django.core.urlresolvers import reverse

class ArticleFeeds(Feed):
    title = "Technewz Article "
    link ='/TechnewArticle/'
    description='Updates on Articles'

    def items(self):
        return Article.objects.all()[:10]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return '/name/article/%i' %item.pk


