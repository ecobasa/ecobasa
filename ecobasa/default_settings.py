# Django settings for ecobasa project.
import os
import sys
from django.utils.translation import ugettext_lazy as _

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

if 'test' in sys.argv:
    DATABASES['default'] = {  # noqa
        'ENGINE': 'django.db.backends.sqlite3'
    }
    SOUTH_TESTS_MIGRATE = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, 'static-collected'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cosinnus.utils.context_processors.settings',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    #'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    #'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

ROOT_URLCONF = 'ecobasa.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ecobasa.wsgi.application'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "templates"),
)

CMS_TEMPLATES = (
    ('start.html', 'Startpage'),
    ('about.html', 'About'),
)

LANGUAGES = (
    ('en', _('English')),
    ('de', _('German')),
)

INSTALLED_APPS = (
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',

    # custom apps
    'ecobasa',
    'cosinnus',
    # 'skillshare',
    # 'references',

    # third-party
    'appconf',
    'bootstrap3',
    'bootstrap3_datetime',
    'easy_thumbnails',
    # 'geoposition',
    'south',
    'taggit',
    'filer',
    'haystack',

    # CMS
    'djangocms_text_ckeditor',
    'cms',
    'mptt',
    'menus',
    'cms.plugins.link',
    'sekizai',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_file',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    # userprofiles
    'userprofiles',
    'userprofiles.contrib.accountverification',
    #'userprofiles.contrib.emailverification',
    #'userprofiles.contrib.profiles',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# userprofile settings
USERPROFILES_CHECK_UNIQUE_EMAIL = True
USERPROFILES_DOUBLE_CHECK_EMAIL = False
USERPROFILES_DOUBLE_CHECK_PASSWORD = True
USERPROFILES_REGISTRATION_FULLNAME = True
# irrelevant settings, since we override the view
USERPROFILES_REGISTRATION_FORM = 'ecobasa.forms.RegistrationMemberForm'

USERPROFILES_USE_ACCOUNT_VERIFICATION = False
USERPROFILES_ACCOUNT_VERIFICATION_DAYS = 7

USERPROFILES_USE_PROFILE = False
USERPROFILES_INLINE_PROFILE_ADMIN = False
#USERPROFILES_PROFILE_FORM = 'ecobasa.forms.EcobasaProfileForm'

USERPROFILES_USE_EMAIL_VERIFICATION = False
#USERPROFILES_EMAIL_VERIFICATION_DAYS = 2
#USERPROFILES_EMAIL_VERIFICATION_DONE_URL = 'userprofiles_profile_change'


# from django.core.urlresolvers import reverse
# LOGIN_URL = reverse('home')


# COSINNUS settings
FORMAT_MODULE_PATH = 'cosinnus.formats'

# COSINNUS_ATTACHABLE_OBJECTS = {
#     'cosinnus_document.Document' : [
#         'cosinnus_file.FileEntry',
#         'cosinnus_document.Document',
#     ],
# }

COSINNUS_USER_PROFILE_MODEL = 'ecobasa.EcobasaUserProfile'


# Conflict between CMS and DebugToolbar resolved by following
# http://zerokspot.com/weblog/2013/12/25/django-cms-and-debug-toolbar/
# http://django-debug-toolbar.readthedocs.org/en/1.0/installation.html#explicit-setup
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1', '::1', 'localhost',)


CKEDITOR_UPLOAD_PATH = "uploads/"


# Search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
    }
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 30
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
