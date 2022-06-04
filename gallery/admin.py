from django.contrib import admin
from .models import Imagegallery
# Register your models here.

class ImagegalleryList(admin.ModelAdmin):
    list_display = (
        'id',
        'Image_title',
    )

admin.site.register(Imagegallery,ImagegalleryList)