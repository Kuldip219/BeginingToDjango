from django.db import models
from django.utils import timezone

# Create your models here.

class variety(models.Model):
    CP_TYPE_CHOICES = [
        ('Type1', 'Report Type 1'),
        ('Type2', 'Report Type 2'),
        ('Type3', 'Report Type 3'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='variety_images/')
    date_created = models.DateTimeField(default=timezone.now)
    cp_type = models.CharField(max_length=5, choices=CP_TYPE_CHOICES, default='Type1')
    description = models.TextField(default="")

    def __str__(self):
        return self.name