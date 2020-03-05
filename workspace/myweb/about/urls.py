from django.urls import path
from about import views

urlpatterns = [
    path('', views.aboutMain),
    path('django/', views.aboutDjango),
]
