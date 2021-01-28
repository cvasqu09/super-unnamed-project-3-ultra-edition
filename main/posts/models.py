from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    createdAt = models.DateTimeField(default = datetime.now, blank = True)
    photoPrimary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photoSecondary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photoTernary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    