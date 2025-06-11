from django.urls import path
from . import views
from .views import display_movies
from django.urls.resolvers import URLPattern
# from django.conf import settings
# from . import views
# from django.conf.urls.static import static

urlpatterns=[
  path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("", views.home, name="home"),
    path("logout/", views.logout_request, name="logout"),
    path("display_movies/",display_movies,name="display_movies"),
]


