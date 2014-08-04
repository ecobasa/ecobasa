 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from postman.models import Message
from django.db.models.signals import post_save
from django.conf import settings

def email(subject_template, message_template, recipient_list, object):
    """Compose and send an email."""
    ctx_dict = {'site': Site.objects.get_current(), 'object': object, 'action': 'acceptance'}
    subject = render_to_string(subject_template, ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    message = render_to_string(message_template, ctx_dict)
    # during the development phase, consider using the setting: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=True)


def notify_user(sender, **kwargs):
    """ Creates a root container instance for all hierarchical objects in a newly created group """
    created = kwargs.get('created', False)
    object = kwargs.get('instance')
    if created:
        """Notify a user."""
        user = object.recipient
        parent = object.parent
        label = 'postman_reply' if (parent and parent.sender_id == object.recipient_id) else 'postman_message'
        email('postman/email_user_subject.txt', 'postman/email_user.txt', [user.email], object)

post_save.connect(notify_user, sender=Message)