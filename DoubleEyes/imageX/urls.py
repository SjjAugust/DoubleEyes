from django.urls import path
from imageX import views


app_name = 'imageX'


urlpatterns = [
    path('index/', views.index, name='index'),
    path('uploadimg/', views.uploadimg, name='uploadimg'),
    path('matching/', views.matching, name="matching"),
    path('', views.index),
]