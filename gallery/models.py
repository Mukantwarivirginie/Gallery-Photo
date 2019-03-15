from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length =30)
    country = models.ImageField(upload_to='photos/') 
    def __str__(self):
        return self.country
    
class Category(models.Model):
    name  = models.CharField(max_length =30)
    def __str__(self):
        return self.category

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='photos/') 
    description= models.TextField()
    location = models.CharField(max_length =30)
    # location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']



    