from django.db import models

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField("Uploaded Image")
    name = models.CharField(max_length=200)
