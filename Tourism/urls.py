"""
URL configuration for Tourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from general import views
from AdminZone import views as ad
urlpatterns = [
    path('admin/', admin.site.urls),


    path('',views.index),
    path('home/',views.pre),
    path('aboutUs/',views.aboutus),
    path('logIn/',views.logIn),
    path('bus/',views.bus),
    path('contacts/',views.contacts),
    path('services/',views.services),
    path('train/',views.train),
    path('dashboard/',ad.dashboard),
    path('contactmgmt/',ad.contactmgmt),
    path('changepass/',ad.changepass),
    path('logout/',ad.logout),
    path('flight/',views.flight),
    path('visa/',views.visa),
    path('saveData/',views.SaveData),
    path('loginData/',views.loginData),
    path('feedbackmgmt/',ad.feedbackmgmt),
    path('bookingmgmt/',ad.bookingmgmt),
    path('feedback/',views.feedback),
    path('booking/',views.booking),
    path('delData/<int:id>',ad.delData)

]
