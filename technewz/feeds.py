from django.contrib.syndication.views import Feed
from blog.models import Article
from django.core.urlresolvers import reverse


class ArticleFeeds(Feed):
    title = "Technewz Article "
    link ='/TechnewArticle/'
    description='Updates on Articles'

    def items(self):
        return Article.objects.filter(publish=True)[:10]

    def item_title(self, item):
        return "{} posted on {}".format(item.name, item.created_at)

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return '/name/article/%i' % item.pk


