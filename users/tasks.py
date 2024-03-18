from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def async_send(**email_kwargs):
    send_mail(**email_kwargs)
