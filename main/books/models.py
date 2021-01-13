from django.db import models
from datetime import datetime
from users.models import User
from django.utils.translation import gettext_lazy as _


class Book(models.Model):

    class Shelf(models.TextChoices):
        READING = 'cr', _('currently-reading')
        READ = 're', _('read')
        TO_READ = 'tr', _('to-read')


    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    gr_id = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10, null=True)
    isbn_13 = models.CharField(max_length=13, null=True)
    rating = models.PositiveSmallIntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_pages = models.PositiveSmallIntegerField(null=True)
    year_published = models.PositiveSmallIntegerField(null=True)
    original_publication = models.PositiveSmallIntegerField(null=True)
    date_read = models.DateField(auto_now=False, null=True)
    date_added = models.DateField(auto_now=False, null=True)
    shelf = models.CharField(max_length=2, choices=Shelf.choices, default=Shelf.TO_READ)
    review = models.CharField(max_length=15000, null=True, blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
