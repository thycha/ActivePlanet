from django.contrib import admin
from Core.models import Banner,Gallery_Image,Partners,Event,Review,Enquiry,Schools

# Register your models here.

@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date','Banner_Type']

@admin.register(Gallery_Image)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date']

@admin.register(Partners)
class PartnersModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date']

@admin.register(Schools)
class SchoolsModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date']

@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Start_Time','End_Time']

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Place','Description']

@admin.register(Enquiry)
class EnquiryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Mobile','Description']