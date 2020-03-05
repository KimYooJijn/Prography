from django.urls import path
from board import views

app_name = 'board'
urlpatterns = [
    path('', views.boardIndex, name='index'),
    path('view/', views.boardView, name='view'),
    path('add/', views.boardAdd, name='add'),
    path('mod/', views.boardMod, name='mod'),
    path('del/', views.boardDel, name='del'),
    path('good/', views.boardGood, name='good'),
    path('bad/', views.boardBad, name='bad'),
    path('comment/', views.boardComment, name='comment'),
]
