from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Avatar


@receiver(post_save, sender=User)
def crear_avatar_usuario(sender, instance, created, **kwargs):
    if created:
        Avatar.objects.get_or_create(user=instance)