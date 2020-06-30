from django.shortcuts import render, redirect

# Create your views here.

from .forms import *

from users.models import *

from django.contrib import messages

from django.urls import reverse

import datetime

from django.db.models import Count

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets, mixins

from .serializers import *

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
# import boto3

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Register successfully, please login!', extra_tags='alert')
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/users/login/')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})


def index(request):
    orderstatus = OrderStatus.objects.get(status_name='published')
    allneeds = Need.objects.filter(orderstatus=orderstatus, isDeleteByUser=False)

    return render(request, 'index.html', context={'allneeds': allneeds})

def citys(request):

    return render(request, 'citys/citys.html')

def findservice(request):
    orderstatus = OrderStatus.objects.get(status_name='published')
    allservice = Service.objects.filter(orderstatus=orderstatus, isDeleteByUser=False)

    return render(request, 'findservice.html', context={'allservice': allservice})

def addservice(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            username = request.user
            instance.user = username
            orderstatus = OrderStatus.objects.get(status_name='published')
            instance.orderstatus = orderstatus
            instance.save()
            messages.success(request, 'Addservice successfully!', extra_tags='alert')
            return redirect('/addservicedone/')

    else:
        form = AddServiceForm()

    return render(request, 'addservice.html', context={'form': form})

def addneeds(request):
    if request.method == 'POST':
        form = AddNeedsForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            username = request.user
            instance.user = username
            orderstatus = OrderStatus.objects.get(status_name='published')
            instance.orderstatus = orderstatus
            # imgurl = request.POST.get('img-url')
            # instance.imageurl = imgurl
            instance.save()
            messages.success(request, 'Addneeds successfully!', extra_tags='alert')
            return redirect('/addneedsdone/')

    else:
        form = AddNeedsForm()

        # S3_BUCKET = os.environ.get('S3_BUCKET')
        #
        # file_name = request.args.get('file_name')
        # file_type = request.args.get('file_type')
        #
        # s3 = boto3.client('s3')
        #
        # presigned_post = s3.generate_presigned_post(
        #     Bucket=S3_BUCKET,
        #     Key=file_name,
        #     Fields={"acl": "public-read", "Content-Type": file_type},
        #     Conditions=[
        #         {"acl": "public-read"},
        #         {"Content-Type": file_type}
        #     ],
        #     ExpiresIn=3600
        # )
        #
        # return json.dumps({
        #     'data': presigned_post,
        #     'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
        # })

    return render(request, 'addneeds.html', context={'form': form})

def addservicedone(request):
    return render(request, 'addservicedone.html')

def addneedsdone(request):
    return render(request, 'addneedsdone.html')

def mypublish(request):
    orderstatus = OrderStatus.objects.get(status_name='published')
    publishedneeds = Need.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)
    orderstatus = OrderStatus.objects.get(status_name='placed')
    placedneeds = Need.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)
    orderstatus = OrderStatus.objects.get(status_name='payed')
    payedneeds = Need.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)
    orderstatus = OrderStatus.objects.get(status_name='completed')
    completedneeds = Need.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)

    orderstatus = OrderStatus.objects.get(status_name='published')
    publishedservice = Service.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)
    orderstatus = OrderStatus.objects.get(status_name='placed')
    placedservice = Service.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)
    orderstatus = OrderStatus.objects.get(status_name='payed')
    payedservice = Service.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)
    orderstatus = OrderStatus.objects.get(status_name='completed')
    completedservice = Service.objects.filter(user=request.user, orderstatus=orderstatus, isDeleteByUser=False)

    return render(request, 'mypublish.html', context={
        'publishedneeds':publishedneeds,
        'placedneeds': placedneeds,
        'payedneeds': payedneeds,
        'completedneeds': completedneeds,

        'publishedservice':publishedservice,
        'placedservice': placedservice,
        'payedservice': payedservice,
        'completedservice': completedservice,
    })

def deleteneeds(request):
    print('Are you sure?')

    needsid = request.GET.get('needsid')
    needs = Need.objects.get(id=needsid)
    needs.isDeleteByUser = True
    needs.save()
    return redirect(reverse('mypublish'))

def editneeds(request):
    if request.method == 'POST':
        needsid = request.POST.get('needsid')
        needs = Need.objects.get(id=needsid)

        form = AddNeedsForm(request.POST or None, request.FILES or None, instance=needs)

        if form.is_valid():
            instance = form.save(commit=False)
            username = request.user
            instance.user = username
            instance.save()
            return redirect(reverse('mypublish'))
    else:
        needsid = request.GET.get('needsid')
        needs = Need.objects.get(id=needsid)

        data = {
            "image": needs.image,
            "start_city": needs.start_city,
            "end_city": needs.end_city,
            "start_date": needs.start_date,
            "end_date": needs.end_date,
            "good_name": needs.good_name,
            "offer_price": needs.offer_price,
            "message": needs.message,
                 }
        form = AddNeedsForm(initial=data)

    return render(request, 'editneeds.html', {'form':form, 'needs':needs})

def deleteservice(request):
    print('Are you sure?')

    serviceid = request.GET.get('serviceid')
    service = Service.objects.get(id=serviceid)
    service.isDeleteByUser = True
    service.save()
    return redirect(reverse('mypublish'))

def editservice(request):
    if request.method == 'POST':
        serviceid = request.POST.get('serviceid')
        service = Service.objects.get(id=serviceid)

        form = AddServiceForm(request.POST or None, request.FILES or None, instance=service)

        if form.is_valid():
            instance = form.save(commit=False)
            username = request.user
            instance.user = username
            instance.save()
            return redirect(reverse('mypublish'))
    else:
        serviceid = request.GET.get('serviceid')
        service = Service.objects.get(id=serviceid)

        data = {
            "image": service.image,
            "start_city": service.start_city,
            "end_city": service.end_city,
            "start_date": service.start_date,
            "end_date": service.end_date,
            "ask_price": service.ask_price,
            "message": service.message,
        }
        form = AddServiceForm(initial=data)

    return render(request, 'editservice.html', {'form':form, 'service':service})

def myorder(request):
    orderstatus = OrderStatus.objects.get(status_name='placed')
    placedneeds = Need.objects.filter(orderuser=request.user, orderstatus=orderstatus, isDeleteByOrderUser=False)
    orderstatus = OrderStatus.objects.get(status_name='payed')
    payedneeds = Need.objects.filter(orderuser=request.user, orderstatus=orderstatus, isDeleteByOrderUser=False)
    orderstatus = OrderStatus.objects.get(status_name='completed')
    completedneeds = Need.objects.filter(orderuser=request.user, orderstatus=orderstatus, isDeleteByOrderUser=False)

    orderstatus = OrderStatus.objects.get(status_name='placed')
    placedservice = Service.objects.filter(orderuser=request.user, orderstatus=orderstatus, isDeleteByOrderUser=False)
    orderstatus = OrderStatus.objects.get(status_name='payed')
    payedservice = Service.objects.filter(orderuser=request.user, orderstatus=orderstatus, isDeleteByOrderUser=False)
    orderstatus = OrderStatus.objects.get(status_name='completed')
    completedservice = Service.objects.filter(orderuser=request.user, orderstatus=orderstatus, isDeleteByOrderUser=False)

    return render(request, 'myorder.html', context={
        'placedneeds': placedneeds,
        'payedneeds': payedneeds,
        'completedneeds': completedneeds,

        'placedservice': placedservice,
        'payedservice': payedservice,
        'completedservice': completedservice,
    })

def orderuserdeleteneeds(request):
    print('Are you sure?')

    needsid = request.GET.get('needsid')
    needs = Need.objects.get(id=needsid)
    needs.isDeleteByOrderUser = True
    needs.save()
    return redirect(reverse('myorder'))

def orderuserdeleteservice(request):
    print('Are you sure?')

    serviceid = request.GET.get('serviceid')
    service = Service.objects.get(id=serviceid)
    service.isDeleteByOrderUser = True
    service.save()
    return redirect(reverse('myorder'))

def message(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)
    receiver = service.user
    sender_id = User.objects.get(username=request.user).id
    receiver_id = User.objects.get(username=receiver).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = MessageForm()
    if receiver == request.user:
        return redirect('findservice')
    return render(request, 'message.html', context={'form': form, 'message_saved': message_saved, 'receiver':receiver, 'receiver_id':receiver_id, 'service_id':service_id})

def message_handler(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('receiver')

            instance = form.save(commit=False)

            sender_id = User.objects.get(username=request.user)
            instance.sender = sender_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = sender_id

            instance.save()
            return redirect(redirect_to)

def orderneedmessage(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)
    receiver = need.user
    sender_id = User.objects.get(username=request.user).id
    receiver_id = User.objects.get(username=receiver).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = MessageForm()
    if receiver == request.user:
        return redirect('index')
    return render(request, 'orderneedmessage.html', context={'form': form, 'message_saved': message_saved, 'receiver':receiver, 'receiver_id':receiver_id, 'need_id':need_id})

def orderneedmessage_handler(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('receiver')

            instance = form.save(commit=False)

            sender_id = User.objects.get(username=request.user)
            instance.sender = sender_id

            created_at = datetime.datetime.now()
            instance.created_at = created_at

            instance.author = sender_id

            instance.save()
            return redirect(redirect_to)

def myorderneedmessage(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)
    receiver = need.user
    sender_id = User.objects.get(username=request.user).id
    receiver_id = User.objects.get(username=receiver).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = MessageForm()
    return render(request, 'myorderneedmessage.html', context={'form': form, 'message_saved': message_saved, 'receiver':receiver, 'receiver_id':receiver_id, 'need_id':need_id})

def myorderneedmessage_handler(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('receiver')

            instance = form.save(commit=False)

            sender_id = User.objects.get(username=request.user)
            instance.sender = sender_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = sender_id

            instance.save()
            return redirect(redirect_to)

def myorderservicemessage(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)
    receiver = service.user
    sender_id = User.objects.get(username=request.user).id
    receiver_id = User.objects.get(username=receiver).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = MessageForm()
    return render(request, 'myorderservicemessage.html', context={'form': form, 'message_saved': message_saved, 'receiver': receiver,
                                                    'receiver_id': receiver_id, 'service_id': service_id})

def myorderservicemessage_handler(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('receiver')

            instance = form.save(commit=False)

            sender_id = User.objects.get(username=request.user)
            instance.sender = sender_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = sender_id

            instance.save()
            return redirect(redirect_to)

def replymessage(request):
    sender = request.GET.get('sender')
    sender_id = User.objects.get(username=sender).id
    receiver_id = User.objects.get(username=request.user).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = replyMessageForm()
    return render(request, 'replymessage.html', context={'form': form, 'message_saved': message_saved, 'sender':sender, 'sender_id':sender_id})

def replymessage_handler(request):
    if request.method == 'POST':
        form = replyMessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('sender')

            instance = form.save(commit=False)

            receiver_id = User.objects.get(username=request.user)
            instance.receiver = receiver_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = receiver_id

            instance.save()
            return redirect(redirect_to)

def sendmessage(request):
    receiver = request.GET.get('receiver')
    receiver_id = User.objects.get(username=receiver).id
    sender_id = User.objects.get(username=request.user).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = MessageForm()
    return render(request, 'sendmessage.html', context={'form': form, 'message_saved': message_saved, 'receiver':receiver, 'receiver_id':receiver_id})

def sendmessage_handler(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('receiver')

            instance = form.save(commit=False)

            sender_id = User.objects.get(username=request.user)
            instance.sender = sender_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = sender_id

            instance.save()
            return redirect(redirect_to)

def inbox(request):
    inboxmessage = Message.objects.filter(receiver=request.user)\
        .order_by('sender', '-created_at').distinct('sender')

    return render(request, 'inbox.html', context={'inboxmessage':inboxmessage})

def outbox(request):
    outboxmessage = Message.objects.filter(sender=request.user) \
        .order_by('receiver', '-created_at').distinct('receiver')

    return render(request, 'outbox.html', context={'outboxmessage':outboxmessage})


def placeorder(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)

    return render(request, 'placeorder.html', context={'service':service})

def placeorder_handler(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)
    service.orderuser = request.user
    orderstatus = OrderStatus.objects.get(status_name='placed')
    checkstatus = OrderStatus.objects.get(status_name='published')
    if service.orderstatus == checkstatus:
        service.orderstatus = orderstatus
        service.save()

        redirect_to = '/payment?service_id=' + service_id

        return redirect(redirect_to)
    else:
        return redirect('error')

def placeneedorder(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)

    return render(request, 'placeneedorder.html', context={'need':need})

def placeneedorder_handler(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)
    need.orderuser = request.user
    orderstatus = OrderStatus.objects.get(status_name='placed')
    checkstatus = OrderStatus.objects.get(status_name='published')
    if need.orderstatus == checkstatus:
        need.orderstatus = orderstatus
        need.save()

        redirect_to = 'myorder'

        return redirect(redirect_to)
    else:
        return redirect('error')

def payment(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)

    return  render(request, 'payment.html', context={'service':service})

def payment_handler(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)

    orderstatus = OrderStatus.objects.get(status_name='payed')
    checkstatus = OrderStatus.objects.get(status_name='placed')
    if service.orderstatus == checkstatus:
        service.orderstatus = orderstatus
        service.save()

        return redirect('myorder')
    else:
        return redirect('error')

def confirm(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)

    orderstatus = OrderStatus.objects.get(status_name='completed')
    checkstatus = OrderStatus.objects.get(status_name='payed')
    if service.orderstatus == checkstatus:
        service.orderstatus = orderstatus
        service.save()

        return redirect('myorder')
    else:
        return redirect('error')

def needspayment(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)

    return  render(request, 'needspayment.html', context={'need':need})

def needspayment_handler(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)

    orderstatus = OrderStatus.objects.get(status_name='payed')
    checkstatus = OrderStatus.objects.get(status_name='placed')
    if need.orderstatus == checkstatus:
        need.orderstatus = orderstatus
        need.save()

        return redirect('mypublish')
    else:
        return redirect('error')

def needsconfirm(request):
    need_id = request.GET.get('need_id')
    need = Need.objects.get(id=need_id)

    orderstatus = OrderStatus.objects.get(status_name='completed')
    checkstatus = OrderStatus.objects.get(status_name='payed')
    if need.orderstatus == checkstatus:
        need.orderstatus = orderstatus
        need.save()

        return redirect('mypublish')
    else:
        return redirect('error')

def error(request):

    return render(request, 'error.html')

@api_view(['GET', 'POST'])
def citys_list(request):
    if request.method == 'GET':
        data = City.objects.all()

        serializer = CitySerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def citys_detail(request, pk):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

class NeedViewSet(viewsets.ModelViewSet):
    orderstatus = OrderStatus.objects.get(status_name='published')
    queryset = Need.objects.filter(orderstatus=orderstatus, isDeleteByUser=False)
    serializer_class = NeedListSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceListSerializer
    orderstatus = OrderStatus.objects.get(status_name='published')
    queryset = Service.objects.filter(orderstatus=orderstatus, isDeleteByUser=False)
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]