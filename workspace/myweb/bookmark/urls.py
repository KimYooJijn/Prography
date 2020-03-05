from django.urls import path
from bookmark import views

urlpatterns = [
    path('', views.bookmarkMain),
]
