# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from cosinnus.models import BaseUserProfile, BaseUserProfileManager


class TaggedInterest(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaUserProfile')


class TaggedSkill(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaUserProfile')


class TaggedProduct(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaUserProfile')


class EcobasaUserProfile(BaseUserProfile):
    # FIXME: why need tagged* to be part of SKIP_FIELDS? where are they
    # injected into the model fields?
    SKIP_FIELDS = ('id', 'user',
                   'taggedskill', 'taggedinterest', 'taggedproduct')

    avatar = ThumbnailerImageField(_('avatar'),
        upload_to='avatars', null=True, blank=True)

    GENDER_OTHER = 'o'
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'
    GENDER_CHOICES = (
        (GENDER_OTHER, '---'),
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male')),
        (GENDER_OTHER, _('Other')),
    )
    gender = models.CharField(_('"gender"'),
        max_length=2, choices=GENDER_CHOICES, default=GENDER_OTHER)

    birth_date = models.DateField(_('birth date'),
        default=None, blank=True, null=True)

    COUNTRY_CHOICES = (
        ('AD', _('Andorra')),
        ('AE', _('United Arab Emirates')),
        ('AF', _('Afghanistan')),
        ('AG', _('Antigua & Barbuda')),
        ('AI', _('Anguilla')),
        ('AL', _('Albania')),
        ('AM', _('Armenia')),
        ('AN', _('Netherlands Antilles')),
        ('AO', _('Angola')),
        ('AQ', _('Antarctica')),
        ('AR', _('Argentina')),
        ('AS', _('American Samoa')),
        ('AT', _('Austria')),
        ('AU', _('Australia')),
        ('AW', _('Aruba')),
        ('AZ', _('Azerbaijan')),
        ('BA', _('Bosnia and Herzegovina')),
        ('BB', _('Barbados')),
        ('BD', _('Bangladesh')),
        ('BE', _('Belgium')),
        ('BF', _('Burkina Faso')),
        ('BG', _('Bulgaria')),
        ('BH', _('Bahrain')),
        ('BI', _('Burundi')),
        ('BJ', _('Benin')),
        ('BM', _('Bermuda')),
        ('BN', _('Brunei Darussalam')),
        ('BO', _('Bolivia')),
        ('BR', _('Brazil')),
        ('BS', _('Bahama')),
        ('BT', _('Bhutan')),
        ('BV', _('Bouvet Island')),
        ('BW', _('Botswana')),
        ('BY', _('Belarus')),
        ('BZ', _('Belize')),
        ('CA', _('Canada')),
        ('CC', _('Cocos (Keeling) Islands')),
        ('CF', _('Central African Republic')),
        ('CG', _('Congo')),
        ('CH', _('Switzerland')),
        ('CI', _('Ivory Coast')),
        ('CK', _('Cook Iislands')),
        ('CL', _('Chile')),
        ('CM', _('Cameroon')),
        ('CN', _('China')),
        ('CO', _('Colombia')),
        ('CR', _('Costa Rica')),
        ('CU', _('Cuba')),
        ('CV', _('Cape Verde')),
        ('CX', _('Christmas Island')),
        ('CY', _('Cyprus')),
        ('CZ', _('Czech Republic')),
        ('DE', _('Germany')),
        ('DJ', _('Djibouti')),
        ('DK', _('Denmark')),
        ('DM', _('Dominica')),
        ('DO', _('Dominican Republic')),
        ('DZ', _('Algeria')),
        ('EC', _('Ecuador')),
        ('EE', _('Estonia')),
        ('EG', _('Egypt')),
        ('EH', _('Western Sahara')),
        ('ER', _('Eritrea')),
        ('ES', _('Spain')),
        ('ET', _('Ethiopia')),
        ('FI', _('Finland')),
        ('FJ', _('Fiji')),
        ('FK', _('Falkland Islands (Malvinas)')),
        ('FM', _('Micronesia')),
        ('FO', _('Faroe Islands')),
        ('FR', _('France')),
        ('FX', _('France, Metropolitan')),
        ('GA', _('Gabon')),
        ('GB', _('United Kingdom (Great Britain)')),
        ('GD', _('Grenada')),
        ('GE', _('Georgia')),
        ('GF', _('French Guiana')),
        ('GH', _('Ghana')),
        ('GI', _('Gibraltar')),
        ('GL', _('Greenland')),
        ('GM', _('Gambia')),
        ('GN', _('Guinea')),
        ('GP', _('Guadeloupe')),
        ('GQ', _('Equatorial Guinea')),
        ('GR', _('Greece')),
        ('GS', _('South Georgia and the South Sandwich Islands')),
        ('GT', _('Guatemala')),
        ('GU', _('Guam')),
        ('GW', _('Guinea-Bissau')),
        ('GY', _('Guyana')),
        ('HK', _('Hong Kong')),
        ('HM', _('Heard & McDonald Islands')),
        ('HN', _('Honduras')),
        ('HR', _('Croatia')),
        ('HT', _('Haiti')),
        ('HU', _('Hungary')),
        ('ID', _('Indonesia')),
        ('IE', _('Ireland')),
        ('IL', _('Israel')),
        ('IN', _('India')),
        ('IO', _('British Indian Ocean Territory')),
        ('IQ', _('Iraq')),
        ('IR', _('Islamic Republic of Iran')),
        ('IS', _('Iceland')),
        ('IT', _('Italy')),
        ('JM', _('Jamaica')),
        ('JO', _('Jordan')),
        ('JP', _('Japan')),
        ('KE', _('Kenya')),
        ('KG', _('Kyrgyzstan')),
        ('KH', _('Cambodia')),
        ('KI', _('Kiribati')),
        ('KM', _('Comoros')),
        ('KN', _('St. Kitts and Nevis')),
        ('KP', _('Korea, Democratic People\'s Republic of')),
        ('KR', _('Korea, Republic of')),
        ('KW', _('Kuwait')),
        ('KY', _('Cayman Islands')),
        ('KZ', _('Kazakhstan')),
        ('LA', _('Lao People\'s Democratic Republic')),
        ('LB', _('Lebanon')),
        ('LC', _('Saint Lucia')),
        ('LI', _('Liechtenstein')),
        ('LK', _('Sri Lanka')),
        ('LR', _('Liberia')),
        ('LS', _('Lesotho')),
        ('LT', _('Lithuania')),
        ('LU', _('Luxembourg')),
        ('LV', _('Latvia')),
        ('LY', _('Libyan Arab Jamahiriya')),
        ('MA', _('Morocco')),
        ('MC', _('Monaco')),
        ('MD', _('Moldova, Republic of')),
        ('MG', _('Madagascar')),
        ('MH', _('Marshall Islands')),
        ('ML', _('Mali')),
        ('MN', _('Mongolia')),
        ('MM', _('Myanmar')),
        ('MO', _('Macau')),
        ('MP', _('Northern Mariana Islands')),
        ('MQ', _('Martinique')),
        ('MR', _('Mauritania')),
        ('MS', _('Monserrat')),
        ('MT', _('Malta')),
        ('MU', _('Mauritius')),
        ('MV', _('Maldives')),
        ('MW', _('Malawi')),
        ('MX', _('Mexico')),
        ('MY', _('Malaysia')),
        ('MZ', _('Mozambique')),
        ('NA', _('Namibia')),
        ('NC', _('New Caledonia')),
        ('NE', _('Niger')),
        ('NF', _('Norfolk Island')),
        ('NG', _('Nigeria')),
        ('NI', _('Nicaragua')),
        ('NL', _('Netherlands')),
        ('NO', _('Norway')),
        ('NP', _('Nepal')),
        ('NR', _('Nauru')),
        ('NU', _('Niue')),
        ('NZ', _('New Zealand')),
        ('OM', _('Oman')),
        ('PA', _('Panama')),
        ('PE', _('Peru')),
        ('PF', _('French Polynesia')),
        ('PG', _('Papua New Guinea')),
        ('PH', _('Philippines')),
        ('PK', _('Pakistan')),
        ('PL', _('Poland')),
        ('PM', _('St. Pierre & Miquelon')),
        ('PN', _('Pitcairn')),
        ('PR', _('Puerto Rico')),
        ('PT', _('Portugal')),
        ('PW', _('Palau')),
        ('PY', _('Paraguay')),
        ('QA', _('Qatar')),
        ('RE', _('Reunion')),
        ('RO', _('Romania')),
        ('RU', _('Russian Federation')),
        ('RW', _('Rwanda')),
        ('SA', _('Saudi Arabia')),
        ('SB', _('Solomon Islands')),
        ('SC', _('Seychelles')),
        ('SD', _('Sudan')),
        ('SE', _('Sweden')),
        ('SG', _('Singapore')),
        ('SH', _('St. Helena')),
        ('SI', _('Slovenia')),
        ('SJ', _('Svalbard & Jan Mayen Islands')),
        ('SK', _('Slovakia')),
        ('SL', _('Sierra Leone')),
        ('SM', _('San Marino')),
        ('SN', _('Senegal')),
        ('SO', _('Somalia')),
        ('SR', _('Suriname')),
        ('ST', _('Sao Tome & Principe')),
        ('SV', _('El Salvador')),
        ('SY', _('Syrian Arab Republic')),
        ('SZ', _('Swaziland')),
        ('TC', _('Turks & Caicos Islands')),
        ('TD', _('Chad')),
        ('TF', _('French Southern Territories')),
        ('TG', _('Togo')),
        ('TH', _('Thailand')),
        ('TJ', _('Tajikistan')),
        ('TK', _('Tokelau')),
        ('TM', _('Turkmenistan')),
        ('TN', _('Tunisia')),
        ('TO', _('Tonga')),
        ('TP', _('East Timor')),
        ('TR', _('Turkey')),
        ('TT', _('Trinidad & Tobago')),
        ('TV', _('Tuvalu')),
        ('TW', _('Taiwan, Province of China')),
        ('TZ', _('Tanzania, United Republic of')),
        ('UA', _('Ukraine')),
        ('UG', _('Uganda')),
        ('UM', _('United States Minor Outlying Islands')),
        ('US', _('United States of America')),
        ('UY', _('Uruguay')),
        ('UZ', _('Uzbekistan')),
        ('VA', _('Vatican City State (Holy See)')),
        ('VC', _('St. Vincent & the Grenadines')),
        ('VE', _('Venezuela')),
        ('VG', _('British Virgin Islands')),
        ('VI', _('United States Virgin Islands')),
        ('VN', _('Viet Nam')),
        ('VU', _('Vanuatu')),
        ('WF', _('Wallis & Futuna Islands')),
        ('WS', _('Samoa')),
        ('YE', _('Yemen')),
        ('YT', _('Mayotte')),
        ('YU', _('Yugoslavia')),
        ('ZA', _('South Africa')),
        ('ZM', _('Zambia')),
        ('ZR', _('Zaire')),
        ('ZW', _('Zimbabwe')),
        ('ZZ', _('Unknown or unspecified country')),
    )
    country = models.CharField(_('country'),
        max_length=2, choices=COUNTRY_CHOICES, default='ZZ')

    city = models.CharField(_('city'),
        max_length=255, blank=True, null=True)
    zipcode = models.CharField(_('zipcode'),
        max_length=255, blank=True, null=True)

    interests = TaggableManager(_('interests'),
        through=TaggedInterest, related_name='_interest', blank=True)
    skills = TaggableManager(_('knowledge/skills'),
        through=TaggedSkill, related_name='_skill', blank=True)
    products = TaggableManager(_('products'),
        through=TaggedProduct, related_name='_product', blank=True)

    # bus fields
    has_bus = models.BooleanField(
        _('Do you have a bus or car that you want to take on the tour?'),
        default=False, blank=True)
    bus_image = ThumbnailerImageField(_('bus image'),
        upload_to='bus_images', null=True, blank=True)
    bus_has_driving_license = models.BooleanField(
        _('I have a driving license'), default=False, blank=True)
    bus_others_can_drive = models.BooleanField(
        _('Other people can drive it too'),
        default=False, blank=True)
    bus_num_passengers = models.PositiveIntegerField(
        _('How many people can it take'), null=True, blank=True, default=0)
    bus_consumption = models.PositiveIntegerField(
        _('Consumption (l/100km)'), null=True, blank=True, default=0)

    # community fields
#    community_telephone = models.CharField(_('telephone'),
#        max_length=255, blank=True, null=True)
#    community_name = models.CharField(_('name of community'),
#        max_length=255, blank=True, null=True)
#    community_show_address = models.BooleanField(_('show address in profile'),
#        default=False, blank=True, null=True)
#    community_num_visitors = models.PositiveIntegerField(
#        _('maximum number of people you can host'),
#        null=True, blank=True, default=0)
#    community_accommodation = models.TextField(_('accommodation for guests'),
#        blank=True, null=True)
#    community_materials = models.TextField(_('what materials do you need?'),
#        blank=True, null=True)
#    community_tools = models.TextField(
#        _('what tools or machines do you need?'),
#        blank=True, null=True)
#    community_seeds = models.TextField(_('do you need seeds?'),
#        blank=True, null=True)
#    community_special_needs = models.TextField(
#        _('special needs (knowledge, information)'), blank=True, null=True)
#    community_services = TaggableManager(_('services'), blank=True)
#    community_skills = TaggableManager(_('skills people can learn'),
#        blank=True)
#    community_products = TaggableManager(_('products'), blank=True)
#    community_workshop_spaces = models.TextField(_('workshop spaces'),
#        blank=True, null=True)
#    community_learning_seminars = models.TextField(_('learning seminars'),
#        blank=True, null=True)
#    community_num_inhabitants = models.PositiveIntegerField(
#        _('how many people live in your community?'),
#        null=True, blank=True, default=0)
#    community_inhabitants_underage = models.PositiveIntegerField(
#        _('how many of them are under 18?'), null=True, blank=True, default=0)
#    community_together = models.TextField(
#        _('what brings your community together'), blank=True, null=True)
#
#    MEMBER_OPEN = 'o'
#    MEMBER_LOOKING = 'l'
#    MEMBER_CLOSED = 'c'
#    MEMBER_CHOICES = (
#        (MEMBER_OPEN, _('open to new members')),
#        (MEMBER_LOOKING, _('looking for members')),
#        (MEMBER_CLOSED, _('closed for new members')),
#    )
#    community_member_status = models.CharField(_('member status'),
#        max_length=2, choices=MEMBER_CHOICES, default=MEMBER_OPEN)

    objects = BaseUserProfileManager()
