from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    #output = _("Welcome to my site.")
    #return HttpResponse(output)
    print(request.build_absolute_uri)
    return render(request, 'Foerder/index.html')
