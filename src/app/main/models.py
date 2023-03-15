from django.db import models
from shortuuid.django_fields import ShortUUIDField


class UrlModel(models.Model):
    # A primary key ID of length 16 and a short alphabet.
    id = ShortUUIDField(
        length=16,
        max_length=40,
        alphabet="abcdefgh12345",
        primary_key=True,
        db_index=True
    )
    original_url = models.CharField(max_length=256)
