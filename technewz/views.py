from django.views import generic
from blog.views import Article
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class HomePage(generic.ListView):
    model = Article
    template_name = "home.html"


class CacheMixin(object):
    method_decorator(cache_page(60 * 15))

    def dispatch(self, request, *args, **kwargs):
        return super(CacheMixin, self).dispatch(request, *args, **kwargs)


class AboutPage(CacheMixin,generic.TemplateView):
    template_name = "checkout.html"


class ContactPage(CacheMixin, generic.TemplateView):
    template_name = "contact.html"


