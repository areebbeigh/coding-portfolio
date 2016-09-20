from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        # ('Date Information', {'fields': ['publish_date'], 'classes': ['collapse']}), # NOT EDITABLE
        ('Project Information', {'fields': ['name', 'description', 'languages', 'thumbnail']}),
    ]
    list_display = ('name', 'publish_date')
    list_filter = ['publish_date']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(About)
