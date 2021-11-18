from django.urls import path
from crater_api import views

urlpatterns = [
    path('api/artist', views.artist_list),
    path('api/artist/<int:pk>', views.artist_detail),
    path('api/artist/name/<keyword>', views.artist_name_contains),
    path('api/bookmark', views.bookmark_list),
    path('api/bookmark/<int:pk>', views.bookmark_detail),
    path('api/search/<keyword>', views.global_search),
]
