"""skillshare tests"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.text import slugify

from .models import SkillName, Skill, Badge


class SkillModelTest(TestCase):
    def _setupUsers(self):
        users = {
            'arne' : User.objects.create_user('arne'),
            'pavlik' : User.objects.create_user('pavlik'),
            'sebastian' : User.objects.create_user('sebastian'),
        }
        users['sebastian'].is_staff = True
        users['sebastian'].save()

        return users


    def _setupSkills(self):
        skills = []
        name = u'fussball spielen'
        skillname, _ = SkillName.objects.get_or_create(
            name=name, slug=slugify(name))
        skill, _ = Skill.objects.get_or_create(
            name=skillname,
            creator=self.users['arne'],
            owner=self.users['arne'],
            info=u'super spieler',
            experience=Skill.PROFESSIONAL,
            teach=True,
        )
        skills.append(skill)

        skill, _ = Skill.objects.get_or_create(
            name=skillname,
            creator=self.users['arne'],
            owner=self.users['sebastian'],
            info=u'naja spieler',
            experience=Skill.LEARNER,
            teach=False,
        )
        skills.append(skill)

        name = u'atombomben stricken'
        skillname, _ = SkillName.objects.get_or_create(
            name=name, slug=slugify(name))
        skill, _ = Skill.objects.get_or_create(
            name=skillname,
            creator=self.users['sebastian'],
            owner=self.users['pavlik'],
            info=u'boom boom shake the room',
            experience=Skill.NOVICE,
            teach=True,
        )
        skills.append(skill)

        skill, _ = Skill.objects.get_or_create(
            name=skillname,
            creator=self.users['sebastian'],
            owner=self.users['sebastian'],
            info=u'sitzt ne kuh aufm baum',
            experience=Skill.EXPERT,
            teach=False,
        )
        skills.append(skill)

        return skills


    def _setupBadges(self):
        badges = []

        badge, _ = Badge.objects.get_or_create(
            skill=self.skills[0],
            giver=self.users['sebastian'],
            feedback=u'einfach super!',
        )
        badges.append(badge)

        badge, _ = Badge.objects.get_or_create(
            skill=self.skills[1],
            giver=self.users['pavlik'],
            feedback=u'genau auch',
        )
        badges.append(badge)

        return badges


    def setUp(self):
        super(SkillModelTest, self).setUp()
        self.users = self._setupUsers()
        self.skills = self._setupSkills()
        self.badges = self._setupBadges()


    def test_can_edit(self):
        """
        Tests can_edit
        """
        self.assertEqual(self.skills[0].can_edit(self.users['arne']), True)
        self.assertEqual(self.skills[0].can_edit(self.users['sebastian']), True)
        self.assertEqual(self.skills[0].can_edit(self.users['pavlik']), False)
