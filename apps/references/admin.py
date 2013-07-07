from django.contrib import admin

from .models import Reference


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('giver', 'receiver',)
    list_filter = ('giver', 'receiver',)
    search_fields = ['giver__username', 'receiver__username', 'text',]
admin.site.register(Reference, ReferenceAdmin)
