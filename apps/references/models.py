from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


#############################################################################

class Reference(models.Model):
    giver = models.ForeignKey(User,
        related_name='%(app_label)s_%(class)s_giver',
        help_text=_('Who gave this reference'),
    )
    receiver = models.ForeignKey(User,
        related_name='%(app_label)s_%(class)s_receiver',
        help_text=_('Who received this reference'),
    )
    text = models.TextField(
        help_text=_('Description of the reference'),
    )


    def __unicode__(self):
        return u'%s -> %s' % (self.giver, self.receiver)
