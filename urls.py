from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from coding_portfolio import feeds  # Feeds
from coding_portfolio import views  # Views
from coding_portfolio.sitemap import ProjectSitemap

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


sitemaps = {
    'projects': ProjectSitemap()
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/view/(\d+)/$', views.project_detail, name='project_detail'),
    url(r'^projects/(.+)/$', views.project_list, name='projects_page'),
    url(r'^query/', views.search, name='search_page'),
    url(r'^about/$', views.about, name='about_page'),
    url(r'^rss/$', feeds.ProjectFeeds(), name='project_feed'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
