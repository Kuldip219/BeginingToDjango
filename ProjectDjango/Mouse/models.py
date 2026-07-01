from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
# One to Many

class ProjectReview(models.Model):
    mice = models.ForeignKey(variety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.mice.name}'
    
# Many to Many

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    varieties = models.ManyToManyField(variety, related_name='projects')

    def __str__(self):
        return self.name