from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import Banner,Gallery_Image,Partners,Event,Review,Enquiry,Schools
from django.contrib import messages
from Core.reuse import resize
from Frontpage.models import Visitor

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'
    enquiries = Enquiry.objects.all().order_by('-id')[:10]
    images = Gallery_Image.objects.all().count()
    events = Event.objects.all().count()
    reviews = Review.objects.all().count()
    visitors = Visitor.objects.all().count()

    context = {
        'page' : page,
        'enquiries' : enquiries,
        'images' : images,
        'events' : events,
        'reviews' : reviews,
        'visitors' : visitors,
    }
    return render(request,'Dashboard/Core/dashboard.html',context)

#----------------------------------- Banners -----------------------------------#

@login_required
def manage_banners(request):
    banners = Banner.objects.all().order_by('-id')

    context = {
        "banners" : banners
    }
    return render(request,'Dashboard/Banners/banners.html',context)

#----------------------------------- Add Banner -----------------------------------#

@login_required
def add_banner(request):
    if request.method == 'POST':
        banner_type = request.POST.get('type')
        image = request.FILES.get('image')

        try:
            # resized = resize(image,800)
            Banner.objects.create(Banner_Type=banner_type, Image=image)

            messages.success(request, 'New banner added successfully ...!')
            return redirect('manage-banners')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-banner')

    return render(request, 'Dashboard/Banners/banner-add.html')

#----------------------------------- Delete Banner -----------------------------------#

@login_required
def delete_banner(request):
    banner_id = request.POST.get('banner_id')
    banner = Banner.objects.get(id=banner_id)
    banner.delete()
    return redirect('manage-banners')

#----------------------------------- Vlogs -----------------------------------#

@login_required
def manage_vlogs(request):
    return render(request,'Dashboard/Vlogs/vlogs.html')

#----------------------------------- Gallery -----------------------------------#

@login_required
def manage_gallery(request):
    images = Gallery_Image.objects.all().order_by('-id')

    context = {
        'images' : images
    }
    return render(request,'Dashboard/Gallery/images.html',context)

#----------------------------------- Add Images -----------------------------------#

@login_required
def add_images(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for image in images:
            # resized = resize(image,800)
            try:
                Gallery_Image.objects.create(Image=image)
            except Exception as exception:
                messages.warning(request,exception)
                return redirect('image-gallery')
        messages.success(request,'New images added successfully ... !')
        return redirect('manage-gallery')
    
#----------------------------------- Delete Image -----------------------------------#

@login_required
def delete_image(request):
    image_id = request.POST.get('image_id')
    image = Gallery_Image.objects.get(id=image_id)
    image.delete()
    messages.warning(request,'Image Deleted ... !')
    return redirect('manage-gallery')

#----------------------------------- Partners -----------------------------------#

@login_required
def manage_partners(request):
    partners = Partners.objects.all().order_by('-id')

    context = {
        'partners' : partners
    }
    return render(request,'Dashboard/Gallery/partners.html',context)

#----------------------------------- Add Partners -----------------------------------#

@login_required
def add_partners(request):
    if request.method == 'POST':
        partners = request.FILES.getlist('partners')

        for partner in partners:
            # resized = resize(partner,300)
            Partners.objects.create(Image=partner)

        messages.success(request,'New partners added successfully ... !')
        return redirect('manage-partners')
    
#----------------------------------- Delete Partner -----------------------------------#

@login_required
def delete_partner(request):
    partner_id = request.POST.get('partner_id')
    partner = Partners.objects.get(id=partner_id)
    partner.delete()
    messages.warning(request,'Partner Deleted ... !')
    return redirect('manage-partners')

#----------------------------------- Manage Events -----------------------------------#

@login_required
def manage_events(request):
    events = Event.objects.all().order_by('-Date')

    context = {
        'events':events
    }
    return render(request,'Dashboard/Events/events.html',context)

#----------------------------------- Add Event -----------------------------------#

@login_required
def add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        start = request.POST.get('start')
        end = request.POST.get('end')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        try:
            Event.objects.create(Name=name,Date=date,Start_Time=start,End_Time=end,Image=image,Description=description)
            messages.success(request,'New event added successfully ... !')
            return redirect('manage-events')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('event-add')

    return render(request,'Dashboard/Events/event-add.html')

#----------------------------------- Edit Event -----------------------------------#

@login_required
def edit_event(request,event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        try:
            if len(request.FILES) > 0:
                event.Image = request.FILES.get('image')

            event.Name = request.POST.get('name')
            event.Date = request.POST.get('date')
            event.Start_Time = request.POST.get('start')
            event.End_Time = request.POST.get('end')
            event.Description = request.POST.get('description') 
            event.save()
            messages.success(request,'Event details edited successfully ... !')
            return redirect('manage-events')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-event',event_id=event.id)
        
    context = {
        'event' : event
    }
    return render(request,'Dashboard/Events/event-edit.html',context)

#----------------------------------- Delete Event -----------------------------------#

@login_required
def delete_event(request):
    event_id = request.POST.get('event_id')
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('manage-events')

#----------------------------------- Reviews -----------------------------------#

@login_required
def manage_reviews(request):
    reviews = Review.objects.all().order_by('-id')

    context = {
        'reviews' : reviews
    }
    return render(request,'Dashboard/Core/reviews.html',context)

#----------------------------------- Delete Reviews -----------------------------------#

@login_required
def delete_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = Review.objects.get(id=review_id)
        review.delete()
        return redirect('manage-reviews')

#----------------------------------- Enquiries -----------------------------------#

@login_required
def enquiries(request):
    enquiries = Enquiry.objects.all().order_by('-id')

    context = {
        'enquiries' : enquiries
    }
    return render(request,'Dashboard/Core/enquiries.html',context)

#----------------------------------- Delete Enquiry -----------------------------------#

@login_required
def delete_enquiry(request):
    if request.method == 'POST':
        enquiry_id = request.POST.get('enquiry_id')
        enquiry = Enquiry.objects.get(id=enquiry_id)
        enquiry.delete()
        return redirect('enquiries')
    
#----------------------------------- Happy Schools -----------------------------------#

@login_required
def manage_schools(request):
    schools = Schools.objects.all().order_by('-id')

    context = {
        'images' : schools
    }
    return render(request,'Dashboard/Gallery/schools.html',context)

#----------------------------------- Add Partners -----------------------------------#

@login_required
def add_schools(request):
    if request.method == 'POST':
        schools = request.FILES.getlist('images')

        for school in schools:
            # resized = resize(school,800)
            Schools.objects.create(Image=school)

        messages.success(request,'New schools added successfully ... !')
        return redirect('manage-schools')
    
#----------------------------------- Delete Partner -----------------------------------#

@login_required
def delete_school(request):
    school_id = request.POST.get('image_id')
    school = Schools.objects.get(id=school_id)
    school.delete()
    messages.warning(request,'school Deleted ... !')
    return redirect('manage-schools')