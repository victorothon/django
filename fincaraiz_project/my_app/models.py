from django.db import models


# Create your models here.

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()
    avatar = models.URLField()

class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()
    propertyTypes = models.CharField(max_length=100)

class PropertyTypes(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()

class States(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()
    zip =  models.PositiveSmallIntegerField()
    state = models.ForeignKey('States', on_delete=models.CASCADE)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()

class Properties(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.URLField()
    price = models.PositiveIntegerField()
    city = models.ForeignKey('Cities', on_delete=models.CASCADE)
    baths = models.PositiveSmallIntegerField()
    beds = models.PositiveSmallIntegerField()
    sqft = models.PositiveSmallIntegerField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)     


