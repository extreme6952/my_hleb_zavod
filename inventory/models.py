import os
import barcode
from barcode.writer import SVGWriter
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
    
    name = models.CharField(max_length=250,
                            unique=True)

    slug = models.SlugField(max_length=250,
                            unique=True,
                            blank=True)
    
    image = ThumbnailerImageField(upload_to='product/%Y/%m/%d',
                                  resize_source=dict(quality=95,
                                                     size=(1368,720),
                                                     sharpen=True),)

    text = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2)

    protein = models.PositiveIntegerField()

    carbohydrates = models.PositiveIntegerField()

    fats = models.PositiveIntegerField()

    callories = models.PositiveIntegerField(blank=True)

    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    barcode = models.CharField(max_length=250,
                               blank=True,
                               null=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):

        if not self.callories:
            self.callories = (self.carbohydrates*4)+(self.protein*4)+(self.fats*9)
        elif not self.slug:
            self.slug = slugify(unidecode(self.name))
        elif not self.barcode:
            self.barcode = str(self.id)
 
        super().save(*args, **kwargs)

        self.generate_barcode()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug,
                                               self.id])
    
    def generate_barcode(self):
        code = barcode.get('code128',str(self.id),
                        writer = SVGWriter()) 
        #Сохраняем файл, в текущую дерикторию media/save/barcode/
        barcode_directory = os.path.join('media','save','barcode')

        if not os.path.join('media','save','barcode'):
            os.makedirs(barcode_directory)

        filename = os.path.join(barcode_directory,
                                f'barcode_{unidecode(self.name)}_{self.id}')   
        code.save(filename)



