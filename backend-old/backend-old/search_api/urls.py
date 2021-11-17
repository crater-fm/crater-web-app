from django.urls import path

from . import views

app_name = 'search_api'
urlpatterns = [
    path('', views.index, name='index'),
]