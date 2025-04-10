from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class TourismSiteApp(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return ["loginpage", "signuppage", "logoutpage","homepage","randompage","destinationspage","aboutpage","culturespage"]
    
    def location(self, obj):
        return reverse(obj)
    
allsitemaps = { "tourismapplinks":TourismSiteApp}