from django_jalali.db import models as jalali
import uuid


from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = jalali.jDateField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=True , editable=False ,default=uuid.uuid4)
    # Generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'uuid')

    class Meta:
        ordering = ['-created_at']