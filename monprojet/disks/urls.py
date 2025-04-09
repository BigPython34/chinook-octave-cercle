from . import views
from django.urls import path
app_name = 'disks'

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
]