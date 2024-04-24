from rest_framework.generics import CreateAPIView, RetrieveAPIView

from clipboard.models import Clipboard
from clipboard.serializers import ClipboardSerializer


class CreateClipboardAPIView(CreateAPIView):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer


class GetClipboardAPIView(RetrieveAPIView):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    lookup_field = 'slug'
