from django.db import models


# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length =30,blank=True)
    country = models.ImageField(upload_to='photos/',blank=True) 
    def __str__(self):
        return self.country
    
class Category(models.Model):
    name  = models.CharField(max_length =30,blank=True)
    def __str__(self):
        return self.category
    



class Image(models.Model):
    image_name = models.CharField(max_length =30,blank=True)
    picture = models.ImageField(upload_to='photos/',blank=True) 
    description= models.TextField(blank=True)
    
    location = models.ForeignKey(Location,blank=True)
    category = models.ForeignKey(Category,blank=True)
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']


