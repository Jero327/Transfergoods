from django.contrib import admin

# Register your models here.

from .models import *

admin.site.site_header =   'Transfergoods'

admin.site.register(User)

admin.site.register(City)

admin.site.register(OrderStatus)

admin.site.register(Service)

admin.site.register(Need)

admin.site.register(Message)