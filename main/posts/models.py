from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    createdAt = models.DateTimeField(default = datetime.now, blank = True)
    photoPrimary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photoSecondary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photoTernary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
    