from django.contrib.sitemaps import Sitemap
from coding_portfolio.models import Project
from datetime import datetime


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def lastmod(self, item):
        return datetime.now()
