from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify


class Section(models.Model):
    title = models.CharField(max_length=23)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = 'images/')
    slug = models.CharField(max_length=72, editable=False, auto_created=True)
    
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
    def __str__(self):
        return f"{self.title}"
    
    
class Category(models.Model):
    title = models.CharField(max_length=23)
    description = models.CharField(max_length=1000)
    section = models.ManyToManyField(Section)
    image = models.ImageField(upload_to = 'images/')
    slug = models.CharField(max_length=72, editable=False, auto_created=True)

    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=30, default="Uknown Product", null=False)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    slug = models.CharField(max_length=72, editable=False, auto_created=True)
    
    def save(self):
        self.slug = slugify(self.label)
        super().save()
    
    def __str__(self) ->str:
        return self.label






