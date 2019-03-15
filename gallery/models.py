from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='photos/') 
    description= models.TextField()
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']