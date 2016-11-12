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

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


def validate_only_one_instance(obj):
    """ Ensures that the model can have only one instance """
    # Thanks to http://stackoverflow.com/a/6436008/4591121
    model = obj.__class__
    if model.objects.count() > 0 and obj.id != model.objects.get().id:
        raise ValidationError(
            "You can create only one %s instance, edit the previous one to make any changes." % model.__name__)


class BaseModel:
    """ Base class for other model classes """

    def get_thumbnail(self, is_project=False, is_website=False):
        """
        Returns the URL to the thumbnail associated with this object.
        """
        if is_project:
            DEFAULT_THUMBNAIL = "/default_project_thumbnail.png"
        elif is_website:
            DEFAULT_THUMBNAIL = "/default_website_thumbnail.svg"
        else:
            DEFAULT_THUMBNAIL = "/default_thumbnail.png"

        if self.thumbnail:
            return self.thumbnail.get_thumbnail()
        else:
            return settings.MEDIA_URL + DEFAULT_THUMBNAIL  # Default thumbnail


class Image(models.Model):
    """ Image model """

    def __str__(self):
        return self.name

    def image_preview(self):
        return mark_safe('<img src="%s" alt="Image" width="100px" height="100px" />' % self.image.url)

    def get_thumbnail(self):
        return self.image.url

    name = models.CharField(max_length=50, help_text='Name of the image.')
    image = models.ImageField(help_text='The image.')


class Platform(BaseModel, models.Model):
    """ Platform model """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True, help_text='Name of the platform.')
    thumbnail = models.ForeignKey(Image, blank=True, null=True, help_text='A thumbnail for the platform.')


class Language(BaseModel, models.Model):
    """ Stores programming languages. """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True, help_text='A programming language or coding framework name.')
    thumbnail = models.ForeignKey(Image, blank=True, null=True, help_text='A thumbnail for the language.')


class Website(BaseModel, models.Model):
    """ Website model. """

    def __str__(self):
        return self.url

    def get_thumbnail(self):
        return super().get_thumbnail(is_website=True)

    name = models.CharField(max_length=50, help_text='Website name.')
    url = models.URLField(help_text='Website url.')
    thumbnail = models.ForeignKey(Image, null=True, blank=True, help_text='Website thumbnail.')


class Project(BaseModel, models.Model):
    """ Stores projects, with their name, description, thumbnail, publish date and languages. """

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        return super().get_thumbnail(is_project=True)

    def get_absolute_url(self):
        """ Returns the absolute URL to the project page """
        return reverse('project_detail', args=[self.id])

    is_project = True
    name = models.CharField(max_length=50, help_text='Project name.')
    website = models.ManyToManyField(Website, help_text='Project website.')
    short_description = models.CharField(help_text='A short description of the project.', max_length=100)
    description = models.TextField(help_text='A more detailed description of the project.')
    platform = models.ManyToManyField(Platform, help_text='The platform this project is intended for.')
    languages = models.ManyToManyField(Language, help_text='The language(s) your project is based on.')
    thumbnail = models.ForeignKey(Image, null=True, blank=True)
    publish_date = models.DateTimeField("Publish Date", auto_now_add=True)


class Contact(models.Model):
    """ Represents a contact to display in the contact information """

    name = models.CharField(max_length=50, help_text='Name of the contact type e.g GitHub.', unique=True)
    font_awesome_class = models.CharField(max_length=50,
                                          help_text='Font Awesome class for the contact icon e.g fa-github')
    url = models.URLField(help_text='A redirecting URL for the contact.')


class About(models.Model):
    """ Stores information to display on the about page """

    def clean(self):
        validate_only_one_instance(self)

    description = models.TextField(help_text='Stuff about yourself.')
