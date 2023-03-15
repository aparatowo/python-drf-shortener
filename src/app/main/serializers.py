from typing import Any

import shortuuid
from rest_framework import serializers
from .models import UrlModel


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = ['id', 'url']

    def validate_id(self, value):
        try:
            if shortuuid.decode(value):
                return value
        except ValueError:
            raise serializers.ValidationError("This is not our shortcut.")
