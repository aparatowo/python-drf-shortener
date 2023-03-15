from .serializers import UrlSerializer
from .models import UrlModel


def shorten(url):
    mapping = UrlSerializer(url=url)
    mapping.save()
    return mapping.id


def load_url(url_hash):
    url_hash = UrlSerializer(data={'id': 'url_hash'})
    url_hash.is_valid()
    return UrlModel.objects.get(id=url_hash.data['id'])
