from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('Date')
    description = models.TextField(max_length=250)

# Create your models here.
