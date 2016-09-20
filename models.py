from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def validate_only_one_instance(obj):
    """ Ensures that the model can have only one instance """
    # Thanks to http://stackoverflow.com/a/6436008/4591121
    model = obj.__class__
    if model.objects.count() > 0 and obj.id != model.objects.get().id:
        raise ValidationError("You can create only one %s instance, edit the previous one to make any changes." % model.__name__)


class Language(models.Model):
    """ Stores programming languages. """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True, help_text='A programming language or coding framework name.')


class Project(models.Model):
    """ Stores projects, with their name, description, thumbnail, publish date and languages. """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Returns the absolute URL to the project page """
        return reverse('project_detail', args=[self.id])

    def get_thumbnail(self):
        """ Returns the relative path to the project thumbnail to add as an image source on the website """
        if self.thumbnail.name:
            return self.thumbnail.url
        else:
            return settings.MEDIA_URL + '/default_thumbnail.png'  # Default thumbnail

    name = models.CharField(max_length=50, help_text='Your project\'s name.')
    description = models.TextField(
        help_text='Your project\'s description, what it does, how it works, download links etc.')
    languages = models.ManyToManyField(Language, help_text='The language(s) your project is based on.')
    thumbnail = models.ImageField(blank=True)
    publish_date = models.DateTimeField("Publish Date", auto_now_add=True)


class About(models.Model):
    """ Stores information to display on the about page """
    def clean(self):
        validate_only_one_instance(self)

    description = models.TextField(help_text='Stuff about yourself.')
