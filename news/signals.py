from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Category


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'new_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(post_save, sender=Category)
def notify_about_new_post(instance, **kwargs):
    if kwargs['action'] == 'new_add':
        categories = instance.post_category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.users.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)