from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import Event, Image
from django.template import loader
import os

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

def redirect(request):
    response = HttpResponse(status=302)
    response['Location'] = 'home'
    return response

def event_list(request):
    template = loader.get_template('Foerder/event_list.html')
    events = Event.objects.order_by('-pub_date')[:5]
    images = {}
    context = {}
    full_event_list = []
    if events:
        for e in events:
            full_event = {}

            i = Image.objects.filter(whichEvent_id=e.id, main=True).first()
            i.image = '../../static/' + i.image.url[12:]
            images[e.id] = i

            full_event['event_object'] = e
            full_event['image_object'] = i
            full_event_list.append(full_event)
    context = {
        #'events': events,
        #'images': images,
        'events': full_event_list,
        }
    #for e in events:
    #    print('########')
    #    print(images[e.id])
    return HttpResponse(template.render(context, request))

def event(request, event_id):
    return HttpResponse(event_id)
