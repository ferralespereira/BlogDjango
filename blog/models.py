from django.db import models

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