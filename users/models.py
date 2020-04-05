from django.db import models
import datetime

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass

class AddService(models.Model):
    start_city = models.CharField(max_length=100)
    end_city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    ask_price = models.IntegerField()
    message = models.CharField(max_length=100)

class AddNeeds(models.Model):
    # image = models.ImageField(label='Please upload a picture of your item if you have one', required=False, help_text=_('Optional image (2.5 MB or less)'), allow_empty_file=True, blank=True, upload_to='goodspic')
    image = models.ImageField(blank=True, upload_to='goodspic/')
    start_city = models.CharField(max_length=100)
    end_city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    good_name = models.CharField(max_length=100)
    offer_price = models.IntegerField()
    message = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title