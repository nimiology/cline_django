from rest_framework import serializers

from clipboard.models import Clipboard


class ClipboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clipboard
        fields = '__all__'
