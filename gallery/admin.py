from django.contrib import admin
from .models import Location,Category,Image

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)