from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Movie


@shared_task
def send_new_movie_email(movie_id):
    users = User.objects.filter(is_active=True)

    movie = Movie.objects.get(id=movie_id)

    subject = "New movie added"
    message = f'A new movie "{movie.title}" has been added to our collection.'
    from_email = "your-email-address"
    recipient_list = [user.email for user in users]

    send_mail(subject, message, from_email, recipient_list)
