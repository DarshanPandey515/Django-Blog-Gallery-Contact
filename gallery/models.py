from django.db import models

# Create your models here.
class Imagegallery(models.Model):
    Image_title = models.CharField(max_length=100)
    Gallery_Image = models.ImageField(null=True,upload_to='gallery/')