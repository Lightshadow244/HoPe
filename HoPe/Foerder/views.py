from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

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
