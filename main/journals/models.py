from django.db import models
from datetime import datetime
from django.conf import settings 
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=15000)
    createdAt = models.DateTimeField(default = timezone.now(), blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})