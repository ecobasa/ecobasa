from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import SkillName, Skill, Badge


class SkillNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(SkillName, SkillNameAdmin)



class BadgeInline(admin.TabularInline):
    model = Badge


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    list_filter = ('teach',)
    search_fields = ['name', 'slug', 'info',]
    inlines = [ BadgeInline, ]
admin.site.register(Skill, SkillAdmin)



class BadgeAdmin(admin.ModelAdmin):
    list_display = ('get_skill_names', 'get_skill_owners', 'giver',)
    search_fields = ['skill__owner__username', 'giver__username',]

    def get_skill_names(self, obj):
            return '%s' % (obj.skill.name)
    get_skill_names.short_description = _('Skill name')

    def get_skill_owners(self, obj):
            return '%s' % (obj.skill.owner)
    get_skill_owners.short_description = _('Skill owner')
admin.site.register(Badge, BadgeAdmin)
