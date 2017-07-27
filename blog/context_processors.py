from .models import Article,Tag


def sidebar_articles(request):
    """Return the 5 most recent articles for the sidebar."""
    tag = Tag.objects.all()
    latest = Article.objects.all()[:5]
    return {'SIDEBAR_ARTICLES': tag,
            'SIDEBAR_LATEST': latest
            }

