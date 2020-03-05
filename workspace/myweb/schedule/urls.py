from django.urls import path
from schedule import views

app_name = 'schedule'
urlpatterns = [
    path('', views.scheduleIndex, name='index'),
    path('add/', views.scheduleAdd, name='add'),
    path('mod/', views.scheduleMod, name='mod'),
    path('del/', views.scheduleDel, name='del'),
    path('view/', views.scheduleView, name='view'),
]
