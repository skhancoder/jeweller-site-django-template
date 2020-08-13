"""rjjewellers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import home,about, contact, gemstones, new, confirm, jewellery, gold, diamond, platinum, coins, gifts
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('gemstones', gemstones, name="gemstones"),
    path('new',new,name="new"),
    path('confirm/',confirm, name="confirm"),
    path('jewellery',jewellery,name="jewellery"),
    path('gold',gold,name="gold"),
    path('diamond',diamond,name="diamond"),
    path('platinum', platinum, name="platinum"),
    path('coins',coins,name="coins"),
    path('gifts',gifts,name="gifts")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)