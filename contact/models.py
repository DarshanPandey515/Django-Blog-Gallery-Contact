from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=500)

    def __str__(self):
        return self.Name