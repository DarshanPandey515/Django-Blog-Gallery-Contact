from autoslug import AutoSlugField
from django.db import models

# Create your models here.
TAGS_CHOICES = [
    ('MF', 'Mens Fashion'),
    ('WF', 'Womens Fashion'),
    ('OF', 'Old Fashion'),
    ('KF', 'Kids Fashion'),
    ('FC', 'Fancy Collections'),
]



class Product(models.Model):
    Name = models.CharField(max_length=200)
    Slug = AutoSlugField(populate_from='Des', unique=True)
    Tags = models.CharField(max_length=100,choices=TAGS_CHOICES,null=True)
    Price = models.IntegerField()
    Des = models.TextField(max_length=100000000000000)
    Date = models.DateTimeField()
    PImage = models.ImageField(null=True,upload_to='productimg/')