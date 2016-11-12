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

from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from . import feeds  # Feeds
from . import views  # Views
from .sitemap import ProjectSitemap

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
