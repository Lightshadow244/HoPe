from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('home', views.home, name='home'),
    path('support_us', views.support_us, name='support_us'),
    path('impressum', views.impressum, name='impressum'),
    path('events', views.event_list, name='event_list'),
    path('about_us', views.about_us, name='about_us'),
    path('partner', views.partner, name='partner'),
    path('events/<int:event_id>', views.event, name='event'),
    path('donate_fv_ghana', views.donate_fv_ghana, name='donate_fv_ghana'),
]
