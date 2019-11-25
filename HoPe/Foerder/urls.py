from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('home', views.home, name='home'),
    path('support_us', views.support_us, name='support_us'),
    path('impressum', views.impressum, name='impressum'),
]
