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

# Django imports
from django.conf import settings
from django.test import TestCase

# Local imports
from .models import Project, Language
from .templatetags.custom_filters import getsubdivisions, getrange, stripmarkup, getlanguages


class CustomTemplateFilterTests(TestCase):
    def test_stripmarkup(self):
        HTML = '<html><body><p>This is my <a href="github.com/areebbeigh">github</a>, go on and <b>follow me</b>.</body></html>'
        STRIPPED_TEXT = 'This is my github, go on and follow me.'
        self.assertEqual(stripmarkup(HTML), STRIPPED_TEXT)

    def test_getsubdivisions(self):
        self.assertEqual(getsubdivisions(range(1, 8), 3), [[1, 2, 3], [4, 5, 6], [7]])
        self.assertEqual(getsubdivisions(range(1, 8), "random garbage value"), [[1, 2, 3], [4, 5, 6], [7]])
        with self.assertRaises(ValueError):
            getsubdivisions(2134, "bullshit value")

    def test_getrange(self):
        self.assertEqual(getrange(5), range(1, 6))
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
