from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from project.views import *


urlpatterns = [
    path('admin', admin.site.urls),
    path('',homePage,name="homePage"),
    path('LoginPage',LoginPage,name="LoginPage"),
    path('LogoutPage',LogoutPage,name="LogoutPage"),
    path('SignUpPage',SignUpPage,name="SignUpPage"),
    path('ProfilePage',ProfilePage,name="ProfilePage"),
    path('profile/edit/',edit_profile, name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
