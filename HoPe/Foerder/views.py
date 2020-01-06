from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import Event, Image
from django.template import loader

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
	images = []
	for e in events:
		i = Image.objects.filter(whichEvent_id=e.id)
		images.append(i)
	context = {
		'events': events,
		'images': images,
	}
	return HttpResponse(template.render(context, request))
