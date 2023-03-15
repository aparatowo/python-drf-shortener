import shortuuid
from .models import UrlModel


def validate_uuid(url_hash):
    try:
        if shortuuid.decode(url_hash):
            return True
    except ValueError:
        return False


def shorten(url):
    mapping = UrlModel(original_url=url)
    mapping.save()
    return mapping.id


def load_url(url_hash):
    url = UrlModel(id=validate_uuid(url_hash))
    return url.objects.get(url)