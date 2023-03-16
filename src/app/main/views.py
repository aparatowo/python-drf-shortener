import os
from django.shortcuts import redirect
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer


from . import service

domain = os.environ.get('DOMAIN')

if domain is None:
    domain = '0.0.0.0'


@csrf_exempt
@api_view(['POST'])
@renderer_classes([JSONRenderer])
def get_url(request):
    # user_url = request.POST.get('url')
    if request.data:
        shortened_url = service.shorten(request.data)
        return Response({shortened_url}, status=200)
    return Response("Send your URL", status=200)


@api_view(['GET'])
def go_to(request, id):
    try:
        long_url = service.load_url(id)
    except ValueError:
        return Response(status=404)
    return redirect(long_url)
