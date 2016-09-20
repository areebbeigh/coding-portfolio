# Python imports
import collections
from html.parser import HTMLParser

# Django imports
from django import template

# Local imports
from coding_portfolio.models import Language

################################################################################
#                                                                              #
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                    #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version.                                       #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
################################################################################


# http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

register = template.Library()


@register.filter
def stripmarkup(value):
    """ Removes the HTML tags from the text """
    return strip_tags(value)


@register.filter
def getsubdivisions(value, subdivisions):
    """
    Given a list, returns a new two-dimensional list with each internal list containing
    'subdivisions' number of elements. If len(value) % 3 != 0 then the last list will contain
    len(value) % 3 number of elements.

    Example: getsubdivisions([1,2,3,4,5,6,7], 3)

             -> [[1,2,3],[4,5,6],[7]]
    """
    if not value:  # NoneType
        return []

    if not isinstance(value, collections.Iterable):
        raise ValueError("Expected value type: " + str(collections.Iterable) + ", got: " + str(type(value)))

    try:
        subdivisions = int(subdivisions)
    except ValueError:
        subdivisions = 3

    subdivided_list = []
    subdivision = []
    index = 0
    while index < len(value):
        subdivision.append(value[index])
        if len(subdivision) == subdivisions:
            subdivided_list.append(subdivision)
            subdivision = []
        index += 1
    if subdivision:
        subdivided_list.append(subdivision)
    return subdivided_list


@register.filter
def getrange(value):
    """ Returns a range(1, value + 1) """

    try:
        value = int(value)
    except ValueError:
        raise ValueError("Expected type: " + str(int) + ", got: " + str(type(value)))

    return range(1, value + 1)


@register.filter
def getlanguages(value):
    """
    Returns a list of the languages in the Language model which have at least one project
    associated with them (not a filter). This is here to automatically generate the Projects dropdown
    menu items.
    """
    return [lang.name for lang in Language.objects.all() if lang.project_set.all()]

"""
-> A close yet fucked up attempt at displaying <code></code> blocks as-is in posts.
-> Problem: It shows <br> tags in the code as well, instead of marking them as safe.
-> Looking for an alternative. If you can fix it please feel free to make a pull request.
@register.filter
def checkcode(value):
    # Checks for <code> or <pre> tags in the text and preserves them
    code_block_regex = r"<code>(.*?)</code>|<pre>(.*?)</pre>"
    search_objects = re.finditer(code_block_regex, value)
    temp = value
    # print(list(search_objects))
    for search in search_objects:
        print(search)
        span = search.span()
        print("Span:", span)
        code_block = value[span[0]:span[1]]
        print("Code block:", code_block)
        if code_block.endswith("</code>"):
            print("Ends with </code>")
            inside = value[span[0] + 6:span[1] - 7]
        else:
            inside = value[span[0] + 5:span[1] - 6]
        print("Inside:", inside)
        escaped_code = conditional_escape(inside)
        print("Escaped code:", escaped_code)
        escaped_code_block = code_block.replace(inside, escaped_code)
        print("Escaped code block:", escaped_code_block)
        temp = temp.replace(code_block, escaped_code_block)
    value = temp
    return mark_safe(value)
"""