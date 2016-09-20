from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from coding_portfolio import feeds  # Feeds
from coding_portfolio import views  # Views
from coding_portfolio.sitemap import ProjectSitemap

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
