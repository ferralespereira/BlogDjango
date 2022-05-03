from django.db import models

# Create your models here.
class Page(models.Model):
    title      = models.CharField(max_length=50, verbose_name="Title")  
    content    = models.TextField(verbose_name="Content")
    slug       = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    visible    = models.BooleanField(verbose_name="Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Updated at")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "Page"
        verbose_name_plural = "Pages"
