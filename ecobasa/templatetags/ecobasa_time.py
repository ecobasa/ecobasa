# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()

@register.simple_tag
def time_of_day():
	import datetime, pytz
	from django.conf import settings
	cur_time = datetime.datetime.now(tz=pytz.timezone(str(settings.TIME_ZONE)))
	if cur_time.hour < 12:
		return 'morning'
	elif 12 <= cur_time.hour < 18:
		return 'afternoon'
	else:
		return 'evening'

@register.simple_tag
def tageszeit():
	import datetime, pytz
	from django.conf import settings
	cur_time = datetime.datetime.now(tz=pytz.timezone(str(settings.TIME_ZONE)))
	if cur_time.hour < 12:
		return 'Morgen'
	elif 12 <= cur_time.hour < 18:
		return 'Tag'
	else:
		return 'Abend'