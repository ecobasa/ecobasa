# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import six

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from six.moves import urllib
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from osm_field.fields import LatitudeField, LongitudeField, OSMField

from cosinnus.models import (
    BaseUserProfile, BaseUserProfileManager, CosinnusGroup)


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


class TaggedInterest(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaUserProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedSkill(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaUserProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedProduct(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaUserProfile')

    class Meta:
        app_label = 'ecobasa'


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
        max_length=2, blank=True, choices=GENDER_CHOICES, default=GENDER_OTHER)

    birth_date = models.DateField(_('birth date'),
        default=None, blank=True, null=True)

    country = models.CharField(_('country'),
        max_length=2, blank=True, choices=COUNTRY_CHOICES, default='ZZ')
    city = models.CharField(_('city'),
        max_length=255, blank=True, null=True)
    zipcode = models.CharField(_('zipcode'),
        max_length=255, blank=True, null=True)

    interests = TaggableManager(_('interests'),
        through=TaggedInterest, related_name='_interest', blank=True,
        help_text='A comma-separated list of tags. You can type anything here. You can also chose from other users tags. Connect two words with a "-" to have one tag.')
    about = models.TextField(_('About you'),
        blank=True,
        null=True)
    ecobasa_what = models.TextField(_('What would you like to use ecobasa mainly for?'),
        blank=True, null=True)
    world = models.TextField(_('What do you do to make the world a better place?'),
        blank=True, null=True)

    skills = TaggableManager(_('knowledge/skills'),
        through=TaggedSkill, related_name='_skill', blank=True,
        help_text='What skills do you have? What can you do to help others? What can you teach someone?')
    products = TaggableManager(_('products'),
        through=TaggedProduct, related_name='_product', blank=True,
        help_text='Can you manufacture any products, like jewelery, furniture, clothes, soap etc.. ?')

    # bus fields
    has_bus = models.BooleanField(
        _('Do you have a bus or car that you want to take on the tour?'),
        default=False, blank=True)
    bus_image = ThumbnailerImageField(_('bus_image'),
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

    objects = BaseUserProfileManager()

    class Meta:
        app_label = 'ecobasa'


class TaggedOffersService(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedOffersSkill(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedOffersCreation(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedOffersMaterial(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedOffersTool(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedWishSkill(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedWishMaterial(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'


class TaggedWishTool(TaggedItemBase):
    content_object = models.ForeignKey('EcobasaCommunityProfile')

    class Meta:
        app_label = 'ecobasa'



@python_2_unicode_compatible
class EcobasaCommunityProfile(models.Model):
    group = models.OneToOneField(CosinnusGroup,
        editable=False, related_name='profile')
    # mandatory name!
    name = models.CharField(_('name of community'), max_length=255)
    website = models.URLField(_('link of your communities website'), max_length=100,
        blank=True, null=True)
    image = ThumbnailerImageField(
        verbose_name=_('image'),
        help_text=_('Header image for the community-profile, minimum resolution 1200x400'),
        upload_to='community_images',
        blank=True,
        null=True)
    video = models.URLField(
        verbose_name=_('Video'),
        help_text=_('Link to a video showing your community'),
        max_length=255,
        blank=True,
        null=True)

    # contact info
    contact_telephone = models.CharField(_('telephone'),
        max_length=255, 
        blank=True, 
        null=True)
    contact_street = models.CharField(_('street'),
        max_length=255, 
        blank=True, 
        null=True)
    contact_location = OSMField(_('Location'),
        blank=True, 
        null=True)
    contact_location_lat = LatitudeField(
        blank=True, 
        null=True)
    contact_location_lon = LongitudeField(
        blank=True, 
        null=True)
    contact_city = models.CharField(_('city'),
        max_length=255, blank=True, null=True)
    contact_zipcode = models.CharField(_('zipcode'),
        max_length=255, blank=True, null=True)
    contact_country = models.CharField(_('country'),
        max_length=2, blank=True, choices=COUNTRY_CHOICES, default='ZZ')
    contact_show = models.BooleanField(_('show address in profile'),
        default=False, blank=True)

    # visitors
    visitors_num = models.PositiveIntegerField(
        _('maximum number of people you can host'),
        blank=True, default=0)
    visitors_accommodation = models.TextField(_('accommodation for guests'),
        blank=True, null=True,
        help_text='Where can your visitors sleep? Do you have space for a bus, tents? How is the indoor sleeping situation? Do you have matresses, a couch?')

    # wishlist
    wishlist_projects = models.TextField(
        _('Do you have any construction projects? List and describe them together with needed materials, tools, experts, time and knowledge.'),
        blank=True, null=True)
    wishlist_materials = TaggableManager(_('What materials do you need?'),
        through=TaggedWishMaterial,
        related_name='_wishlist_material', blank=True)
    wishlist_materials_info = models.TextField(_('Do you have any additional info about materials, or details to your request (like condition, when you need them)?'),
        blank=True, null=True)
    wishlist_tools = TaggableManager(_('What tools or machines do you need?'),
        through=TaggedWishTool,
        related_name='_wishlist_tool', blank=True)
    wishlist_tools_info = models.TextField(
        _('Do you have any additional info about materials, or details to your request (like condition, when you need them) ?'),
        blank=True, null=True)
    wishlist_skills = TaggableManager(_('Are you looking for some experts that could help you with a project or problem? Tag their desired skills here:'),
        through=TaggedWishSkill,
        related_name='_wishlist_skill', blank=True)
    wishlist_special_needs = models.TextField(
        _('Special needs (knowledge, information)'), blank=True, null=True)

    # offers
    offers_services = TaggableManager(_('Services offered in your community'),
        through=TaggedOffersService,
        related_name='_offers_service', blank=True)
    offers_skills = TaggableManager(_('Skills people can learn in your community'),
        through=TaggedOffersSkill,
        related_name='_offers_skill', blank=True)
    offers_creations = TaggableManager(_('Creations/Products'),
        through=TaggedOffersCreation,
        related_name='_offers_creation', blank=True)
    offers_materials = TaggableManager(_('Do you have any materials that you produce or that you dont need anymore?'),
        through=TaggedOffersMaterial,
        related_name='_offers_material', blank=True)
    offers_tools = TaggableManager(_('Do you have any tools that you produce or that you dont need anymore?'),
        through=TaggedOffersTool,
        related_name='_offers_tool', blank=True)
    offers_workshop_spaces = models.TextField(_('Do you have workshop spaces, where people can build/construct/manufacture things?'),
        blank=True, null=True)
    offers_learning_seminars = models.TextField(_('Do you offer any seminars that visitors could attend?'),
        blank=True, null=True)

    # basic info
    basic_description = models.TextField(
        _('Describe your community'), blank=True, null=True)
    basic_inhabitants = models.PositiveIntegerField(
        _('how many people live in your community?'),
        null=True, blank=True, default=0)
    basic_inhabitants_underage = models.PositiveIntegerField(
        _('how many of them are under 18?'), null=True, blank=True, default=0)
    basic_brings_together = models.TextField(
        _('what brings your community together'), blank=True, null=True)
    MEMBERSHIP_OPEN = 'o'
    MEMBERSHIP_LOOKING = 'l'
    MEMBERSHIP_CLOSED = 'c'
    MEMBERSHIP_CHOICES = (
        (MEMBERSHIP_OPEN, _('open to new members')),
        (MEMBERSHIP_LOOKING, _('looking for members')),
        (MEMBERSHIP_CLOSED, _('closed for new members')),
    )
    basic_membership_status = models.CharField(_('member status'),
        max_length=2,
        blank=True,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_OPEN)

    class Meta:
        app_label = 'ecobasa'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # copy profile name to cosinnus group name
        self.group.name = self.name
        # ensure the CosinnusGroup is always public!
        self.group.public = True
        self.group.save()
        return super(EcobasaCommunityProfile, self).save(*args, **kwargs)


class EcobasaCommunityProfileSeed(models.Model):
    profile = models.ForeignKey(EcobasaCommunityProfile,
        verbose_name=_('seeds'),
        on_delete=models.CASCADE,
        related_name='wishlist_seeds',
    )
    kind = models.CharField(_('what kind of seeds?'),
        max_length=255,
        blank=True,
        null=True)
    num = models.PositiveIntegerField(_('how many?'), blank=True, default=0)

    class Meta:
        app_label = 'ecobasa'
