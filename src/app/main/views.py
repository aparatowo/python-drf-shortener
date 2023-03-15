import os
# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service

domain = os.environ.get('DOMAIN')

if domain is None:
    domain = '0.0.0.0'


@csrf_exempt
def get_url(request):
    print(dict(request))
    user_url = request.POST['url']
    if user_url is not None:
        shortened_url = service.shorten(user_url)
        return HttpResponse({shortened_url}, status=200)
    return HttpResponse("Send your URL", status=200)


def redirect_to_url(request, url):
    try:
        shortened_url = service.load_url(url)
    except ValueError:
        return HttpResponse(status=404)
    return HttpResponse(shortened_url, status=200)
