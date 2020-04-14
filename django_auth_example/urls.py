"""django_auth_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^findneeds/$', views.index, name='findneeds'),
    url(r'^findservice/$', views.findservice, name='findservice'),
    url(r'^addservice$', views.addservice, name='addservice'),
    url(r'^addneeds$', views.addneeds, name='addneeds'),
    url(r'^addservicedone/$', views.addservicedone, name='addservicedone'),
    url(r'^addneedsdone/$', views.addneedsdone, name='addneedsdone'),
    url(r'^mypublish$', views.mypublish, name='mypublish'),
    url(r'^deleteneeds$', views.deleteneeds, name='deleteneeds'),
    url(r'^editneeds$', views.editneeds, name='editneeds'),
    url(r'^editneeds_handler$', views.editneeds_handler, name='editneeds_handler'),
    url(r'^deleteservice$', views.deleteservice, name='deleteservice'),
    url(r'^editservice$', views.editservice, name='editservice'),
    url(r'^editservice_handler$', views.editservice_handler, name='editservice_handler'),
    url(r'^myorder$', views.myorder, name='myorder'),
    url(r'^orderuserdeleteneeds$', views.orderuserdeleteneeds, name='orderuserdeleteneeds'),
    url(r'^orderuserdeleteservice$', views.orderuserdeleteservice, name='orderuserdeleteservice'),
    url(r'^message$', views.message, name='message'),
    url(r'^message_handler$', views.message_handler, name='message_handler'),
    url(r'^orderneedmessage$', views.orderneedmessage, name='orderneedmessage'),
    url(r'^orderneedmessage_handler$', views.orderneedmessage_handler, name='orderneedmessage_handler'),
    url(r'^myorderneedmessage$', views.myorderneedmessage, name='myorderneedmessage'),
    url(r'^myorderneedmessage_handler$', views.myorderneedmessage_handler, name='myorderneedmessage_handler'),
    url(r'^myorderservicemessage$', views.myorderservicemessage, name='myorderservicemessage'),
    url(r'^myorderservicemessage_handler$', views.myorderservicemessage_handler, name='myorderservicemessage_handler'),
    url(r'^replymessage$', views.replymessage, name='replymessage'),
    url(r'^replymessage_handler$', views.replymessage_handler, name='replymessage_handler'),
    url(r'^sendmessage$', views.sendmessage, name='sendmessage'),
    url(r'^sendmessage_handler$', views.sendmessage_handler, name='sendmessage_handler'),
    url(r'^placeorder$', views.placeorder, name='placeorder'),
    url(r'^placeorder_handler$', views.placeorder_handler, name='placeorder_handler'),
    url(r'^placeneedorder$', views.placeneedorder, name='placeneedorder'),
    url(r'^placeneedorder_handler$', views.placeneedorder_handler, name='placeneedorder_handler'),
    url(r'^payment$', views.payment, name='payment'),
    url(r'^payment_handler$', views.payment_handler, name='payment_handler'),
    url(r'^confirm$', views.confirm, name='confirm'),
    url(r'^needspayment$', views.needspayment, name='needspayment'),
    url(r'^needspayment_handler$', views.needspayment_handler, name='needspayment_handler'),
    url(r'^needsconfirm$', views.needsconfirm, name='needsconfirm'),
    url(r'^inbox$', views.inbox, name='inbox'),
    url(r'^outbox$', views.outbox, name='outbox'),

    # url(r'users/', views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

