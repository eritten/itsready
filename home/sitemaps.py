# sitemap for the site

from django.contrib.sitemaps import Sitemap

class ItsreadySitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'login', 'signup', 'privacy', 'terms']

    def location(self, item):
        return reverse(item)