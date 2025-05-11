from assignment_5.myproject.celery_app import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email):
    send_mail(
        'Welcome to the CleanApp',
        'Thank you for signing up!',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

@shared_task
def generate_user_report():
    # Placeholder for long-running data processing
    time.sleep(5)
    return "User report generated successfully."
