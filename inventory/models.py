from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

class Category(models.Model):

    name = models.CharField(max_length=200,
                            unique=True)
    slug = models.SlugField(max_length=200,
                            unique=True,
                            blank=True)

    image = ThumbnailerImageField(upload_to='product/%Y/%m/%d',
                                  resize_source=dict(quality=95,
                                                     size=(1368, 720),
                                                     sharpen=True),)

    class Meta:

        ordering = ['-name']
        indexes = [
            models.Index(fields=['-name'])
        ]


    def __str__(self):
        return self.name
    

    def save(self,*args, **kwargs):

        if not self.slug:
            slugify(unidecode(self.name))
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("category_detail", args=[self.slug])
    

class Product(models.Model):

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 name='product_category')
    
    name = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250,
                            unique=True,
                            blank=True)
    
    image = ThumbnailerImageField(upload_to='product/%Y/%m/%d',
                                  resize_source=dict(quality=95,
                                                     size=(1368, 720),
                                                     sharpen=True),)

    text = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2)

    quantity = models.PositiveIntegerField()

    protein = models.PositiveIntegerField()

    fat = models.PositiveIntegerField()

    callories = models.PositiveIntegerField()

    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)


    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]


    def __str__(self):
        return self.name
    

    def save(self,*args, **kwargs):

        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        return super().save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug,
                                               self.id])
    

    