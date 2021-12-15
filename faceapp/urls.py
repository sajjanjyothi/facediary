from django.urls import path

from . import views
app_name = 'faceapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save_video, name='save'),
    path('delete', views.delete_video, name='delete'),
]