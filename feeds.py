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
        return item.description

    def item_link(self, item):
        return item.get_absolute_url()