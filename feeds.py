from django.contrib.syndication.views import Feed

from coding_portfolio.models import Project

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
        return item.description

    def item_link(self, item):
        return item.get_absolute_url()