from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


class SkillName(models.Model):
    name = models.CharField(max_length=255,
        help_text=_('Name of the Skill'),
        db_index=True,
    )
    slug = models.SlugField(max_length=255,
        help_text=_('Slug of the Skill'),
    )

    def __unicode__(self):
        return self.name



class Skill(models.Model):
    NOVICE = 'NOV'
    LEARNER = 'LEA'
    PROFESSIONAL = 'PRO'
    EXPERT = 'EXP'
    CHOICES_EXPERIENCE = (
        (NOVICE, _('Novice')),
        (LEARNER, _('Learner')),
        (PROFESSIONAL, _('Professional')),
        (EXPERT, _('Expert')),
    )
    name = models.ForeignKey(SkillName,
        related_name='%(app_label)s_%(class)s',
        help_text=_('Name of this Skill'),
    )
    creator = models.ForeignKey(User,
        related_name='%(app_label)s_%(class)s_creator',
        help_text=_('Who created this Skill'),
    )
    owner = models.ForeignKey(User,
        related_name='%(app_label)s_%(class)s_owner',
        help_text=_('Who owns this Skill'),
    )
    info = models.TextField(
        help_text=_('How the owner obtained this skill'),
    )
    experience = models.CharField(max_length=3,
        choices=CHOICES_EXPERIENCE,
        default=NOVICE,
        help_text=_('Level of experience in this Skill'),
    )
    teach = models.BooleanField(
        default=False,
        help_text=_('If the Skill will be taught by the owner'),
    )


    class Meta:
        ordering = ['name']
        unique_together = (('name', 'owner'),)


    def __unicode__(self):
        return u'%s: %s' % (self.name, self.owner)


    def get_absolute_url(self):
        return reverse('skillshare:detail', kwargs={
            'slug': self.slug,
            'owner': skill.owner,
        })


    def can_edit(self, user):
        if user.is_staff:
            return True
        if user == self.owner:
            return True
        return False



class Badge(models.Model):
    skill = models.ForeignKey(Skill,
        related_name='%(app_label)s_%(class)s',
        help_text=_('Skill this badge was given for'),
    )
    giver = models.ForeignKey(User,
        help_text=_('Who awarded this badge'),
    )
    # no awardee - that's part of the Skill
    feedback = models.TextField(
        help_text=_('Why this badge was awarded'),
    )


    def __unicode__(self):
        return u'%s: %s -> %s' % (self.skill.name, self.giver, self.skill.owner)
