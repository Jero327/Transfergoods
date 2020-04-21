from django.db import models
import datetime

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass
    def __str__(self):
        return f'{self.username}'

class City(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class OrderStatus(models.Model):
    status_id = models.IntegerField(default=0)
    status_name = models.CharField(max_length=100, default='completed')
    def __str__(self):
        return f'{self.status_id}'

class Service(models.Model):
    image = models.ImageField(upload_to='servicepic/', default='servicepic/default_img.jpg', blank=True)
    start_city = models.ForeignKey("City", related_name='service_start_city', on_delete=models.CASCADE, null=True)
    end_city = models.ForeignKey("City", related_name='service_end_city', on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    ask_price = models.IntegerField(validators=[MinValueValidator(1)])
    message = models.CharField(max_length=100)

    user = models.ForeignKey("User", related_name='service_user', on_delete=models.CASCADE, null=True)
    orderuser = models.ForeignKey("User", related_name='service_orderuser', on_delete=models.CASCADE, null=True, blank=True)
    orderstatus = models.ForeignKey("OrderStatus", related_name='service_orderstatus', on_delete=models.CASCADE, default=1)

    isDeleteByUser  = models.BooleanField(default=False)
    isDeleteByOrderUser = models.BooleanField(default=False)

    def __str__(self):
        return f'Service: {self.user} - {self.orderuser} - {self.orderstatus}'


class Need(models.Model):
    image = models.ImageField(upload_to='needspic/', default='needspic/default_img.jpg', blank=True)
    start_city = models.ForeignKey("City", related_name='need_start_city', on_delete=models.CASCADE, null=True)
    end_city = models.ForeignKey("City", related_name='need_end_city', on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    good_name = models.CharField(max_length=100)
    offer_price = models.IntegerField(validators=[MinValueValidator(1)])
    message = models.CharField(max_length=100)

    user = models.ForeignKey("User", related_name='need_user', on_delete=models.CASCADE, null=True)
    orderuser = models.ForeignKey("User", related_name='need_orderuser', on_delete=models.CASCADE, null=True, blank=True)
    orderstatus = models.ForeignKey("OrderStatus", related_name='need_orderstatus', on_delete=models.CASCADE, default=1)

    isDeleteByUser = models.BooleanField(default=False)
    isDeleteByOrderUser = models.BooleanField(default=False)

    def __str__(self):
        return f'Need: {self.user} - {self.orderuser} - {self.orderstatus}'

class Message(models.Model):
    sender = models.ForeignKey("User", related_name='message_sender', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey("User", related_name='message_receiver', on_delete=models.CASCADE, null=True)
    msg_content = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField()
    author = models.ForeignKey("User", related_name='message_author', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return f'Message: {self.sender} - {self.receiver} - {self.created_at}'