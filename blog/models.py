from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.
class Post(models.Model):
    Title =  models.CharField(max_length=100)
    Post_Slug = AutoSlugField(populate_from='Title',unique=True)
    Content = RichTextField(blank=True,null=True)
    Header_Image = models.ImageField(null=True,upload_to='HeaderImage/')
    Created_at = models.DateTimeField()

    def __str__(self):
        return self.Title
  


class Knowme(models.Model):
    Your_Name = models.CharField(max_length=100)
    Your_Email = models.EmailField(max_length=100)
    Your_PH = models.IntegerField()
    Your_Address = models.CharField(max_length=500)
    Your_JobRole = models.CharField(max_length=100)
    Your_Website = models.CharField(max_length=100)
    Your_FB = models.CharField(max_length=100,null=True)
    Your_INSTA = models.CharField(max_length=100,null=True)
    Your_GITHUB = models.CharField(max_length=100,null=True)
    Your_TW = models.CharField(max_length=100,null=True)