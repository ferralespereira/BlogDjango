from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    description = models.CharField(max_length=255, verbose_name="description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categorys"

    
    def __str__(sefl):
        return sefl.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="title")
    content = RichTextField(verbose_name="content")
    image = models.ImageField(default='null', verbose_name="image")
    public = models.BooleanField(verbose_name="Public?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="categories", blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    
    def __str__(sefl):
        return sefl.title
