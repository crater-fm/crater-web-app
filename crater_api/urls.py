from django.urls import path
from crater_api import views
from crater_api.views import ArtistListPlayCount, DjListEpisodeCount

urlpatterns = [
    path('api/artist', ArtistListPlayCount.as_view()),
    path('api/artist/<int:artist_id>', views.artist_details),
    path('api/artist/name/<keyword>', views.artist_name_contains),
    path('api/dj/<int:dj_id>', views.dj_details),
    path('api/dj', DjListEpisodeCount.as_view()),
    path('api/episode', views.all_episodes),
    path('api/bookmark', views.bookmark_list),
    path('api/bookmark/<int:pk>', views.bookmark_detail),
    path('api/search/<keyword>', views.global_search)
]
