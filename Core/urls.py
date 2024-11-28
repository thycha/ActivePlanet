from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('banner/list/',views.manage_banners,name='manage-banners'),
    path('banner/add/',views.add_banner,name='add-banner'),
    path('banner/delete',views.delete_banner,name='delete-banner'),

    path('vlogs/manage/',views.manage_vlogs,name='manage-vlogs'),

    path('gallery/manage/',views.manage_gallery,name='manage-gallery'),
    path('gallery/images/add/',views.add_images,name='add-images'),
    path('gallery/image/delete/',views.delete_image,name='delete-image'),

    path('partner/manage/',views.manage_partners,name='manage-partners'),
    path('partner/add/',views.add_partners,name='add-partners'),
    path('partner/delete/',views.delete_partner,name='delete-partner'),

    path('school/manage/',views.manage_schools,name='manage-schools'),
    path('school/add/',views.add_schools,name='add-schools'),
    path('school/delete/',views.delete_school,name='delete-school'),

    path('events/manage/',views.manage_events,name='manage-events'),
    path('event/add/',views.add_event,name='add-event'),
    path('event/edit/<int:event_id>/',views.edit_event,name='edit-event'),
    path('event/delete/',views.delete_event,name='delete-event'),

    path('reviews/',views.manage_reviews,name='manage-reviews'),
    path('review/delete/',views.delete_review,name='delete-review'),
    path('enquiries/',views.enquiries,name='enquiries'),
    path('enquiry/delete/',views.delete_enquiry,name='delete-enquiry'),
]