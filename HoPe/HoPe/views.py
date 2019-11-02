# handles the redirect because of the default language from the browser
from django.http import HttpResponse


def index(request):
    response = HttpResponse(status=302)
    if request.LANGUAGE_CODE == 'de':
        response['Location'] = '/de/a'
    else:
        response['Location'] = '/en/a'
    return response
