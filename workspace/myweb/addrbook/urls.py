from django.urls import path
from addrbook import views

app_name = 'addrbook'
urlpatterns = [
    path('', views.addrIndex, name='index'),
    path('view/', views.addrView, name='view'),
    path('add/', views.addrAdd, name='add'),
    path('mod/', views.addrMod, name='mod'),
    path('del/', views.addrDel, name='del'),
]
