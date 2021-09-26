from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True,max_length=333)
    description=models.TextField()
    cart_image=models.ImageField(upload_to='categories/photos',blank=True)
    class Meta:
        verbose_name='category'
        verbose_name_plural='catergories'
    def __str__(self):
        return self.category_name