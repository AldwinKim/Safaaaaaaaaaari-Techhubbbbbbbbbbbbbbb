from .views import homepage, signinpage, signuppage, Signout, randompage, destinationpage, aboutpage, culturespage
from django.urls import path
urlpatterns = [
    path("", homepage, name="homepage"),
    path("signinpage/", signinpage, name="signinpage"),
    path("signuppage/", signuppage, name="signuppage"),
    path("signoutpage/", Signout, name="signoutpage"),
    path("randompage/", randompage, name="randompage"),
    path("destinationspage/", destinationpage, name="destinationspage"),
    path("aboutpage/", aboutpage, name="aboutpage"),
    path("culturespage/", culturespage, name="culturespage")
]