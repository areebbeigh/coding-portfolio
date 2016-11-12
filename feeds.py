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

from django.contrib.syndication.views import Feed

from coding_portfolio.models import Project


class ProjectFeeds(Feed):
    """ A basic feed page for all the projects on the website """
    title = "Projects Feed"
    link = "/rss/"
    description = "An RSS feed of all the projects on this website"

    def items(self):
        return Project.objects.order_by("-publish_date")

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.short_description

    def item_link(self, item):
        return item.get_absolute_url()
