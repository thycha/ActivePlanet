from django.urls import path
from Frontpage import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),
    path('gallery/',views.gallery,name='gallery'),
    path('packages/',views.packages,name='packages'),
    path('rides/',views.rides,name='rides'),
    path('review/',views.review,name='review'),
]