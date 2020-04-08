from django.shortcuts import render, redirect

# Create your views here.

from .forms import RegisterForm, AddServiceForm, AddNeedsForm

from users.models import AddNeeds, AddService

from django.contrib import messages

from django.urls import reverse

from datetime import datetime

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
    allneeds = AddNeeds.objects.filter(orderstatus=0)

    return render(request, 'index.html', context={'allneeds': allneeds})

def findservice(request):
    allservice = AddService.objects.filter(orderstatus=0)

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
#     allneeds = AddNeeds.objects.all()
#
#     return render(request, 'index.html', context={'allneeds': allneeds})

def mypublish(request):
    publishedneeds = AddNeeds.objects.filter(user=request.user, orderstatus=0)
    placedneeds = AddNeeds.objects.filter(user=request.user, orderstatus=3)
    payedneeds = AddNeeds.objects.filter(user=request.user, orderstatus=1)
    completedneeds = AddNeeds.objects.filter(user=request.user, orderstatus=2)

    publishedservice = AddService.objects.filter(user=request.user, orderstatus=0)
    placedservice = AddService.objects.filter(user=request.user, orderstatus=3)
    payedservice = AddService.objects.filter(user=request.user, orderstatus=1)
    completedservice = AddService.objects.filter(user=request.user, orderstatus=2)

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
    needs = AddNeeds.objects.get(id=needsid)
    needs.delete()
    return redirect(reverse('mypublish'))

def editneeds(request):
    needsid = request.GET.get('needsid')
    needs = AddNeeds.objects.get(id=needsid)

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

    needs = AddNeeds.objects.get(id=needsid)

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
    service = AddService.objects.get(id=serviceid)
    service.delete()
    return redirect(reverse('mypublish'))

def editservice(request):
    serviceid = request.GET.get('serviceid')
    service = AddService.objects.get(id=serviceid)

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

    service = AddService.objects.get(id=serviceid)

    service.image = image
    service.start_city = start_city
    service.end_city = end_city
    service.start_date =  datetime.strptime(start_date, '%Y-%m-%d')
    service.end_date =  datetime.strptime(end_date, '%Y-%m-%d')
    service.ask_price = ask_price
    service.message = message

    service.save()
    return redirect(reverse('mypublish'))


