import uuid

from django.db import models


# Create your models here.
class Clipboard(models.Model):
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
