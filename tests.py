# Django imports
from django.conf import settings
from django.test import TestCase

# Local imports
from coding_portfolio.models import Project, Language
from coding_portfolio.templatetags.custom_filters import getsubdivisions, getrange, stripmarkup, getlanguages

LANG1 = 'Parseltongue'
LANG2 = 'Python'
PROJECT_NAME = 'Hail Voldemort'
PROJECT_DESC = "'Hail Voldemort' in Parseltongue and Python"


class ModelTests(TestCase):
    def setUp(self):
        self.lang1 = Language.objects.create(name=LANG1)
        self.lang2 = Language.objects.create(name=LANG2)
        self.p = Project.objects.create(
            name=PROJECT_NAME,
            description=PROJECT_DESC)
        self.p.languages.add(self.lang1, self.lang2)

    def test_language_model(self):
        self.assertEqual(self.lang1.name, LANG1)
        self.assertEqual(self.lang2.name, LANG2)

    def test_project_model(self):
        self.assertEqual(self.p.name, PROJECT_NAME)
        self.assertEqual(self.p.description, PROJECT_DESC)
        # Test if correct languages are associated with the project
        for lang in self.p.languages.all():
            self.assertTrue(lang in Language.objects.all())

    def test_project_get_thumbnail(self):
        self.assertEqual(self.p.get_thumbnail(), settings.MEDIA_URL + '/default_thumbnail.png')


class CustomTemplateFilterTests(TestCase):
    def test_stripmarkup(self):
        HTML = '<html><body><p>This is my <a href="github.com/areebbeigh">github</a>, go on and <b>follow me</b>.</body></html>'
        STRIPPED_TEXT = 'This is my github, go on and follow me.'
        self.assertEqual(stripmarkup(HTML), STRIPPED_TEXT)

    def test_getsubdivisions(self):
        self.assertEqual(getsubdivisions(range(1,8), 3), [[1,2,3],[4,5,6],[7]])
        self.assertEqual(getsubdivisions(range(1,8), "random garbage value"), [[1,2,3],[4,5,6],[7]])
        with self.assertRaises(ValueError):
            getsubdivisions(2134, "bullshit value")

    def test_getrange(self):
        self.assertEqual(getrange(5), range(1,6))
        with self.assertRaises(ValueError):
            getrange("crap")

    def test_getlanguages(self):
        lang1 = Language.objects.create(name='Java')
        lang2 = Language.objects.create(name='Python')
        lang3 = Language.objects.create(name='PHP')
        p = Project.objects.create(
            name='Coding Portfolio',
            description='Programming portfolio for lazy people like me',
        )
        p.languages.add(lang1, lang2)
        self.assertEqual(getlanguages(""), [lang.name for lang in p.languages.all()])
