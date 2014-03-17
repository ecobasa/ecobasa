from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from content.admin import DownloadInline
from content.models import SlideshowPlugin, SlideshowImage

class SlideshowImageInline(admin.StackedInline):
    model = SlideshowImage
    extra = 0


class CMSSlideshowPlugin(CMSPluginBase):
    model = SlideshowPlugin
    name = _("Slide show")
    render_template = "plugins/slideshow.html"
    text_enabled = False
    admin_preview = False
    inlines = [SlideshowImageInline,]
    
    def render(self, context, instance, placeholder):
        context.update({
            'slideshow': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSSlideshowPlugin)