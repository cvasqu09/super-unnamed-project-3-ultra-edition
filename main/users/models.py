from django.db import models
from datetime import datetime
class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})