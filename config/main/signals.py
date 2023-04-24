from django.db.models.signals import post_save
from django.dispatch import receiver
from main.tasks import send_new_movie_email
from .models import Movie


@receiver(post_save, sender=Movie)
def send_new_movie_email_signal(sender, instance, created, **kwargs):
    if created:
        send_new_movie_email.delay(instance.id)
