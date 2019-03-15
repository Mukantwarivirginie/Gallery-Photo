from django.db import models


# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length =30,blank=True)
    country = models.CharField(max_length =30,blank=True) 
    def __str__(self):
        return self.country



    
class Category(models.Model):
    name  = models.CharField(max_length =30,blank=True)
    def __str__(self):
        return self.name


    @classmethod
    def search_by_category(cls,name):
        category = cls.objects.filter(image_name__icontains=name).first()
        images=Image.objects.filter(category=category)
        return images
    



class Image(models.Model):
    image_name = models.CharField(max_length =30,blank=True)
    picture = models.ImageField(upload_to='photos/',blank=True) 
    description= models.TextField(blank=True)
    
    location = models.ForeignKey(Location,blank=True)
    category = models.ForeignKey(Category,blank=True)
    def __str__(self):
        return self.image_name

    


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()
    
    def display_image(self):
        self.display()

    @classmethod
    def search_by_category(cls,image_name):
        category = Category.objects.filter(image_name__icontains=image_name).first()
        images=cls.objects.filter(category=category)
        return images

    class Meta:
        ordering = ['image_name']

    @classmethod
    def get_image(cls,id):
            return Image.objects.get(id=id)



