from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import Event, Image
from django.template import loader
import os
from datetime import timedelta
from django.utils import timezone

# Create your views here.
def home(request):
    #output = _("Welcome to my site.")
    #return HttpResponse(output)
    #print(request.build_absolute_uri)
    return render(request, 'Foerder/index.html')

def support_us(request):
    #output = _("Welcome to my site.")
    #return HttpResponse(output)
    #print(request.build_absolute_uri)
    return render(request, 'Foerder/support_us.html')

def impressum(request):
    #output = _("Welcome to my site.")
    #return HttpResponse(output)
    #print(request.build_absolute_uri)
    return render(request, 'Foerder/impressum.html')

def about_us(request):
    return render(request, 'Foerder/about_us.html')

def partner(request):
    return render(request, 'Foerder/partner.html')

def redirect(request):
    response = HttpResponse(status=302)
    response['Location'] = 'home'
    return response

def event_list(request):
    #template = loader.get_template('Foerder/event_list.html')
    template = loader.get_template('Foerder/events.html')
    #events_querry_old = Event.objects.order_by('-pub_date')[:5]
    events_querry_new = Event.objects.filter(pub_date__gt=timezone.now() - timedelta(days=1)).order_by('pub_date')[:3]
    events_querry_old = Event.objects.filter(pub_date__lte=timezone.now() - timedelta(days=1)).order_by('-pub_date')[:6]
    images = {}
    context = {}
    events_old = []
    events_new = []
    #print(events)
    if events_querry_old:
        for e in events_querry_old:
            full_event = {}

            if(Image.objects.filter(whichEvent_id=e.id, main=True).first()):
            	i = Image.objects.filter(whichEvent_id=e.id, main=True).first()
            	i.image = '../../static/' + i.image.url[12:]
            else:
                i = ''
            full_event['event_object'] = e
            full_event['image_object'] = i
            events_old.append(full_event)
    if events_querry_new:
        for e in events_querry_new:
            full_event = {}

            if(Image.objects.filter(whichEvent_id=e.id, main=True).first()):
            	i = Image.objects.filter(whichEvent_id=e.id, main=True).first()
            	i.image = '../../static/' + i.image.url[12:]
            else:
                i = ''
            full_event['event_object'] = e
            full_event['image_object'] = i
            events_new.append(full_event)
    context = {
        'events_old': events_old,
        'events_new': events_new,
        }
    return HttpResponse(template.render(context, request))

def event(request, event_id):
    template = loader.get_template('Foerder/event.html')
    event = {}

    if(Image.objects.filter(whichEvent_id=event_id, main=True).first()):
        event['main_image_object'] = Image.objects.filter(whichEvent_id=event_id, main=True).first().image.url[12:]
    eventImages = Image.objects.filter(whichEvent_id=event_id, main=False).all()
    event['images_object'] = []
    for x in range(eventImages.count()):
        event['images_object'].append(eventImages[x].image.url[12:])
    print(event['images_object'])
    event['event_object'] = Event.objects.get(pk=event_id)
    event['event_id'] = event_id
    #print(event)
    context = { 'event': event, }
    return HttpResponse(template.render(context, request))

def spenden_fv_ghana(request)
    return render(request, 'Foerder/spenden_fv_ghana.html')
