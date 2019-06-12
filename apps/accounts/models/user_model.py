import uuid
from django.db import models


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    first_name = models.TextField(default='', blank=True)
    last_name = models.TextField(default='', blank=True)
