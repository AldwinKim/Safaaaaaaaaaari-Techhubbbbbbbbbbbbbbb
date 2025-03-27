from .views import homepage, loginpage, signuppage, logoutpage, randompage, destinationpage, aboutpage, culturespage
from django.urls import path
urlpatterns = [
    path("", homepage, name="homepage"),
    path("logininpage/", loginpage, name="logininpage"),
    path("signuppage/", signuppage, name="signuppage"),
    path("logoutpage/", logoutpage, name="logoutpage"),
    path("randompage/", randompage, name="randompage"),
    path("destinationspage/", destinationpage, name="destinationspage"),
    path("aboutpage/", aboutpage, name="aboutpage"),
    path("culturespage/", culturespage, name="culturespage")
]