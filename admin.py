"""
   Copyright 2016 Areeb Beigh

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.contrib import admin
from django import forms

from .customfields.imagefields import SVGAndImageFormField
from .models import *


# Model Forms

class ImageModelForm(forms.ModelForm):
    class Meta:
        exclude = []
        field_classes = {
            'image': SVGAndImageFormField,
        }


# Model Admin Classes

class BaseAdmin(admin.ModelAdmin):
    """ Base class for other model admin classes """

    def get_thumbnail(self, obj):
        return mark_safe('<img src="' + obj.get_thumbnail() + '" alt="Thumbnail" width="100px" height="100px"')

    get_thumbnail.short_description = "Thumbnail"


class ProjectAdmin(BaseAdmin):
    list_display = ('name', 'short_description', 'publish_date')
    list_filter = ['publish_date']


class PlatformAdmin(BaseAdmin):
    list_display = ('name', 'get_thumbnail')


class LanguageAdmin(BaseAdmin):
    list_display = ('name', 'get_thumbnail')


class WebsiteAdmin(BaseAdmin):
    list_display = ('name', 'url', 'get_thumbnail')


class ContactAdmin(BaseAdmin):
    list_display = ('name', 'url')


class ImageAdmin(admin.ModelAdmin):
    form = ImageModelForm
    fields = ('image_preview', 'name', 'image')
    list_display = ('name', 'image_preview',)
    readonly_fields = ('image_preview',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Image, ImageAdmin)
