from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import settings

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now=True)

    def get_articles(self):
        article = Article.objects.all().filter(pk=self.pk)
        return article

    def get_tags_under(self,pk):
        articles = Article.objects.get(tag=self.name)
        return articles

    def get_absolute_url(self):
        return Tag.objec

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=name)
    content = RichTextField()
    publish = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/images')
    #comments = models.ForeignKey(Comments)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_latest_article(self):
        return Article.objects.all().order_by(self.created_at)[:5]

    def get_tag(self):
        return Article.objects.get(tag=self.tag)

    def get_short(self):
        articles = Article.objects.filter(publish=True).get(content=self.content)[:300]
        return articles

    def get_published(self):
        articles = Article.objects.filter(published=True)
        return articles

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def get_likes(self):
        article = Article.objects.get(article=self)
        likes = Likes.objects.count(like=article)
        return likes

    def get_absolute_url(self):
        return '/name/article/%i/' % self.pk

    '''
    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})
    '''
    '''
    def get_comments(self):
        comments = Comments.objects.all()
        return comments

    def total_comments(self):
        comments = Comments.objects.all().count()
    '''


class Likes(models.Model):
    like = models.IntegerField(default=0)
    #created_at = models.DateTimeField(auto_now_add=True)

    def get_total_likes(self):
        return Likes.objects.all().count()

    def get_all_likes(self):
        return Likes.objects.all()


class Comments(models.Model):
    comment = models.TextField(max_length=500)
    commentor = models.ForeignKey(User)
    created_at = models.DateField(auto_now=True)

