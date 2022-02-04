"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#define function

from django.contrib import admin
from django.urls import path

# 1st method to import views from views.py

#from views import myHomeViewFunction,myAboutUsViewFunction,contact,category,cart,detail,login

# 2nd method to import views (2nd method is easy to import)
from . import views

urlpatterns = [ # List
    path('hello/', admin.site.urls,name="adminRoute"),
    #path(routename, viewfunction, kwargs=None, nameOfTheRoute=None)
    path('', views.myHomeViewFunction , name="homeRoute" ),
    path('aboutus/', views.myAboutUsViewFunction , name="aboutusroute" ),
    path('contact/',views.contact,name="contactroute"),
    path('product/<slug:category>/',views.category,name="categoryroute"),
    path('cart/',views.cart,name="cartroute"),
    path('detail/',views.detail,name="detailroute"),
    path('login/',views.login,name="loginroute"),
    path('home/',views.home,name="Homeroute"),
    path('landing/',views.landing,name="landingroute"),
    path('checkout/',views.checkout,name="checkoutroute"),
    path('404/',views.four04,name="404route"),
    path('blogp/',views.blogp,name="blogaroute"),
    path('blog1/',views.blog1,name="blogbroute"),
    path('blog2/',views.blog2,name="blogcroute"),
    path('blog3/',views.blog3,name="blogdroute"),
    path('category1/',views.category1,name="categoryaroute"),
    path('category2/',views.category2,name="categorybroute"),
    path('category3/',views.category3,name="categorycroute"),
    path('category4/',views.category4,name="categorydroute"),
    path('category5/',views.category5,name="categoryeroute"),
    path('category6/',views.category6,name="categoryfroute"),
    path('category7/',views.category7,name="categorygroute"),
    path('category8/',views.category8,name="categoryhroute"),
    path('home1/',views.home1,name="homearoute"),
    path('home2/',views.home2,name="homebroute"),
    path('home3/',views.home3,name="homecroute"),
    path('home4l/',views.home4l,name="homedroute"),
    path('home4/',views.home4,name="homeeroute"),
    path('home5/',views.home5,name="homefroute"),
    path('detail1/',views.detail1,name="detailaroute"),
    path('detail2/',views.detail2,name="detailbroute"),
    path('detail3',views.detail3,name="detailcroute"),
    path('detail4/',views.detail4,name="detaildroute"),

   
]
