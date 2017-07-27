from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^article/$', views.ArticleList.as_view(), name='article'),
    url(r'^category/$', views.TagList.as_view()),
    url(r'^article/(?P<pk>\d+)/$', views.BlogDetail.as_view(), name="article_details"),
    #url(r'^tag/$', views.TagList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)