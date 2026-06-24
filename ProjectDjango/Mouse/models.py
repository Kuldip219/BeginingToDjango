from django.db import models
from django.utils import timezone

# Create your models here.

class variety(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='variety_images/')
    date_created = models.DateTimeField(default=timezone.now)