from .serializers import UrlSerializer
from .models import UrlModel


def shorten(data):
    mapping = UrlSerializer(data=data)
    mapping.is_valid()
    mapping.save()
    return mapping.id


def load_url(url_hash):
    url_hash = UrlSerializer(data={'id': url_hash})
    return UrlModel.objects.get(id=url_hash.data['id'])
