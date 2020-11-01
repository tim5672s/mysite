from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    created_ar = models.DateTimeField(default=timezone.now)