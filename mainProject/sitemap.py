from django.contrib.sitemaps import Sitemap


class TourismSiteApp(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return ["loginpage", "signuppage", "signoutpage","homepage","randompage","destinationpage","aboutpage","culturespage"]
    
allsitemaps = { "tourismapplinks":TourismSiteApp}