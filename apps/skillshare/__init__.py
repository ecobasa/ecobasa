from .models import Skill
from .forms import get_form_badge


def get_skills_for_owner(request, owner, return_url=None, form_badge=True):
    skills = Skill.objects.filter(owner=owner)
    if not form_badge:
        return skills

    for skill in skills:
        skill.form_badge = get_form_badge(request, skill, return_url)

    return skills
