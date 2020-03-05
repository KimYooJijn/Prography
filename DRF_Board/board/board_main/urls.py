from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='board_main'
'''
urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^', views.Board_main.as_view(), name='board'),
    url(r'^board_list/$', views.Board_main.as_view(), name='board_list'),
    url(r'^board_list/(?P<id>\d+)/$', views.Board_detail.as_view(), name='board_detail'),
]
'''
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("", views.Board_main.as_view(), name='board'),
    path('board_list/', views.Board_main.as_view(), name='board_list'),
    path('board_list/create/', views.Board_create.as_view(), name='board_create'),
    path('board_list/<int:id>/', views.Board_detail.as_view(), name='board_detail'),
    path('board_list/<int:id>/update/', views.Board_update.as_view(), name='board_update'),
    path('board_list/<int:id>/delete/', views.Board_delete.as_view(), name='board_delete'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)