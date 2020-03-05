"""myweb URL Configuration

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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from myweb import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')), # login/logout
    path('join/', views.userJoin, name='join'),
    path('userinfo/', views.userInfo, name='userinfo'),
    path('addbook/', include('addrbook.urls')),
    path('sche/', include('schedule.urls')),
    path('board/', include('board.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    # path('webtoon/weekday/<str:week>/', views.webtoonWeek),
    # path('webtoon/year/<int:year>/', views.webtoonYear),
    # path('news/<int:year>/<int:month>/<int:day>/', views.newsDate),
    re_path(r'^webtoon/weekday/([a-z]{3})/$', views.webtoonWeek),
    re_path(r'^webtoon/year/(2[0-9]{3})/$', views.webtoonYear),
    re_path(r'^news/(2[0-9]{3})/(0[1-9]|1[0-2])/([0-2][0-9]|30|31)/$', views.newsDate),
    path('abt/', include('about.urls')),
    path('bok/', include('bookmark.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    