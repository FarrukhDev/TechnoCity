from django.urls import path, include
from .views import *
from asosiy.views import Home,About,Contact,Shop,Blog,Team

urlpatterns = [
    path('',Home.as_view(),name = 'home'),
    path('about/',About.as_view(),name = 'about'),
    path('contact/',Contact.as_view(),name = 'contact'),
    path('shop/',Shop.as_view(),name = 'shop'),
    path('team/',Team.as_view(),name = 'team'),
    path('blog/',Blog.as_view(),name = 'blog'),
]