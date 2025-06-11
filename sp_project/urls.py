"""
URL configuration for sp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from find_your_ticket import views as find_your_ticket_view
# from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('find_your_ticket.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('login/', find_your_ticket_view.Login, name ='login'),
    # path('logout/', auth.LogoutView.as_view(template_name ='find_your_ticket/index.html'), name ='logout'),
    # path('register/', find_your_ticket_view.register, name ='register'),
]
