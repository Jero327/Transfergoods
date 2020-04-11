from django.shortcuts import render, redirect

# Create your views here.

from .forms import *

from users.models import *

from django.contrib import messages

from django.urls import reverse

from datetime import datetime

from django.db.models import Count

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
    allneeds = Need.objects.filter(orderstatus=1, isDeleteByUser=False)

    return render(request, 'index.html', context={'allneeds': allneeds})

def findservice(request):
    allservice = Service.objects.filter(orderstatus=1, isDeleteByUser=False)

    return render(request, 'findservice.html', context={'allservice': allservice})

def addservice(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            username = request.user
            instance.user = username
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
            instance.save()
            messages.success(request, 'Addneeds successfully!', extra_tags='alert')
            return redirect('/addneedsdone/')

    else:
        form = AddNeedsForm()

    return render(request, 'addneeds.html', context={'form': form})

def addservicedone(request):
    return render(request, 'addservicedone.html')

def addneedsdone(request):
    return render(request, 'addneedsdone.html')

# def displayneeds(request):
#     allneeds = Need.objects.all()
#
#     return render(request, 'index.html', context={'allneeds': allneeds})

def mypublish(request):
    publishedneeds = Need.objects.filter(user=request.user, orderstatus=1, isDeleteByUser=False)
    placedneeds = Need.objects.filter(user=request.user, orderstatus=4, isDeleteByUser=False)
    payedneeds = Need.objects.filter(user=request.user, orderstatus=2, isDeleteByUser=False)
    completedneeds = Need.objects.filter(user=request.user, orderstatus=3, isDeleteByUser=False)

    publishedservice = Service.objects.filter(user=request.user, orderstatus=1, isDeleteByUser=False)
    placedservice = Service.objects.filter(user=request.user, orderstatus=4, isDeleteByUser=False)
    payedservice = Service.objects.filter(user=request.user, orderstatus=2, isDeleteByUser=False)
    completedservice = Service.objects.filter(user=request.user, orderstatus=3, isDeleteByUser=False)

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
    needsid = request.GET.get('needsid')
    needs = Need.objects.get(id=needsid)

    return render(request, 'editneeds.html', {'needs':needs})

def editneeds_handler(request):
    needsid = request.POST.get('needsid')

    image = request.POST.get('image')
    start_city = request.POST.get('start_city')
    end_city = request.POST.get('end_city')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    good_name = request.POST.get('good_name')
    offer_price = request.POST.get('offer_price')
    message = request.POST.get('message')

    needs = Need.objects.get(id=needsid)

    needs.image = image
    needs.start_city = start_city
    needs.end_city = end_city
    needs.start_date =  datetime.strptime(start_date, '%Y-%m-%d')
    needs.end_date =  datetime.strptime(end_date, '%Y-%m-%d')
    needs.good_name = good_name
    needs.offer_price = offer_price
    needs.message = message

    needs.save()
    return redirect(reverse('mypublish'))

def deleteservice(request):
    print('Are you sure?')

    serviceid = request.GET.get('serviceid')
    service = Service.objects.get(id=serviceid)
    service.isDeleteByUser = True
    service.save()
    return redirect(reverse('mypublish'))

def editservice(request):
    serviceid = request.GET.get('serviceid')
    service = Service.objects.get(id=serviceid)

    return render(request, 'editservice.html', {'service':service})

def editservice_handler(request):
    serviceid = request.POST.get('serviceid')

    image = request.POST.get('image')
    start_city = request.POST.get('start_city')
    end_city = request.POST.get('end_city')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    ask_price = request.POST.get('ask_price')
    message = request.POST.get('message')

    service = Service.objects.get(id=serviceid)

    service.image = image
    service.start_city = start_city
    service.end_city = end_city
    service.start_date =  datetime.strptime(start_date, '%Y-%m-%d')
    service.end_date =  datetime.strptime(end_date, '%Y-%m-%d')
    service.ask_price = ask_price
    service.message = message

    service.save()
    return redirect(reverse('mypublish'))

def myorder(request):
    placedneeds = Need.objects.filter(orderuser=request.user, orderstatus=4, isDeleteByOrderUser=False)
    payedneeds = Need.objects.filter(orderuser=request.user, orderstatus=2, isDeleteByOrderUser=False)
    completedneeds = Need.objects.filter(orderuser=request.user, orderstatus=3, isDeleteByOrderUser=False)

    placedservice = Service.objects.filter(orderuser=request.user, orderstatus=4, isDeleteByOrderUser=False)
    payedservice = Service.objects.filter(orderuser=request.user, orderstatus=2, isDeleteByOrderUser=False)
    completedservice = Service.objects.filter(orderuser=request.user, orderstatus=3, isDeleteByOrderUser=False)

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
    receiver = request.GET.get('receiver')
    sender_id = User.objects.get(username=request.user).id
    receiver_id = User.objects.get(username=receiver).id
    message_saved = Message.objects.filter(sender=sender_id, receiver=receiver_id)
    form = MessageForm()
    return render(request, 'message.html', context={'form': form, 'message_saved': message_saved, 'receiver':receiver, 'receiver_id':receiver_id})

def message_handler(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            redirect_to = request.GET.get('receiver')

            instance = form.save(commit=False)

            # sender = request.user
            sender_id = User.objects.get(username=request.user)
            instance.sender = sender_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = sender_id

            instance.save()
            # messages.success(request, 'Message sent!', extra_tags='alert')
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

            # receiver = request.user
            receiver_id = User.objects.get(username=request.user)
            instance.receiver = receiver_id

            created_at = datetime.now()
            instance.created_at = created_at

            instance.author = receiver_id

            instance.save()
            # messages.success(request, 'Message sent!', extra_tags='alert')
            return redirect(redirect_to)

def inbox(request):
    # inboxmessage = Message.objects.filter(receiver=request.user).values('sender').annotate(qty=Count('sender'))
    # lastinboxmessage = Message.objects.filter(receiver=request.user).reverse()[0]

    inboxmessage = Message.objects.filter(receiver=request.user)\
        .order_by('sender', '-created_at').distinct('sender')

    # inboxmessage = Message.objects.filter(receiver=request.user).raw("""\
    #     SELECT * FROM
    #     (
    #         SELECT sender, msg_content, created_at
    #         FROM Message
    #         ORDER BY created_at DESC
    #     ) t
    #     GROUP BY t.sender
    # """)

    return render(request, 'inbox.html', context={'inboxmessage':inboxmessage})

def outbox(request):
    # outboxmessage = Message.objects.filter(sender=request.user).values('receiver').annotate(qty=Count('receiver'))
    outboxmessage = Message.objects.filter(sender=request.user) \
        .order_by('receiver', '-created_at').distinct('receiver')

    return render(request, 'outbox.html', context={'outboxmessage':outboxmessage})


def placeorder(request):

    return render(request, 'placeorder.html')