from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Core.models import Banner,Gallery_Image,Review,Enquiry,Partners,Event,Schools
from Frontpage.models import Visitor
import uuid
from django.contrib import messages

# Create your views here.

def update_visitors():
    key = str(uuid.uuid4().hex)[:8]
    Visitor.objects.create(Key=key)


def home(request):
    mobile_banners = Banner.objects.filter(Banner_Type='Mobile').order_by('-id')
    system_banners = Banner.objects.filter(Banner_Type='System').order_by('-id')
    images = Gallery_Image.objects.all().order_by('-id')[:6]
    reviews = Review.objects.all().order_by('-id')[:6]
    partners = Partners.objects.all().order_by('-id')
    events = Event.objects.all().order_by('-Date')[:3]
    schools = Schools.objects.all().order_by('-id')[:2]

    update_visitors()

    context = {
        'mobile_banners' : mobile_banners,
        'system_banners' : system_banners,
        'images' : images,
        'reviews' : reviews,
        'partners' : partners,
        'events' : events,
        'schools' : schools,
    }
    return render(request,'Frontpage/index.html',context)

def about(request):
    reviews = Review.objects.all().order_by('-id')
    partners = Partners.objects.all().order_by('-id')

    context = {
        'reviews' : reviews,
        'partners' : partners
    }
    return render(request,'Frontpage/about.html',context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        description = request.POST.get('description')

        try:
            Enquiry.objects.create(Name=name,Mobile=mobile,Description=description)
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status':'failed'})
    return render(request,'Frontpage/contact.html')

def events(request):
    events = Event.objects.all().order_by('-Date')

    context = {
        'events' : events
    }
    return render(request,'Frontpage/events.html',context)

def gallery(request):
    images = Gallery_Image.objects.all().order_by('-id')

    context = {
        'images' : images
    }
    return render(request,'Frontpage/gallery.html',context)

def packages(request):
    schools = Schools.objects.all().order_by('-id')

    context = {
        'schools' : schools
    }
    return render(request,'Frontpage/packages.html',context)

def rides(request):
    return render(request,'Frontpage/rides.html')

@csrf_exempt
def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        description = request.POST.get('description')
        rating = request.POST.get('rating')

        try:
            Review.objects.create(Name=name,Place=place,Description=description,Rating=rating)
            # return JsonResponse({'status':'success'})
            messages.success(request,'Review Added Successfully ... !')
            return redirect('review')
        except:
            return JsonResponse({'status':'failed'})
        
    return render(request,'Frontpage/review.html')