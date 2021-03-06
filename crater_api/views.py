from django.http import HttpResponse, JsonResponse
from django.db.models import Count, Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.postgres.search import SearchVector
from crater_api.models import Artist, Dj, Episode, SongArtist
from crater_api.serializers import ArtistSerializer, GlobalSearchSerializer, ArtistDetailsSerializer, DjDetailsSerializer, ArtistPlayCountSerializer, DjEpCountSerializer, EpisodeSerializer
from collections import namedtuple
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# TODO: update to psycopg2 instead of psycopg-binary

""" ARTIST """


@csrf_exempt
def get_artist(request, pk):
    """
    Retrieve an artist record
    """
    try:
        artist = Artist.objects.get(pk)
    except Artist.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return JsonResponse(serializer.data)


@csrf_exempt
def artist_name_contains(request, keyword):
    """
    Retrieve an artist whose name contains the search parameter keyword
    """
    try:
        artists = Artist.objects.filter(artist_name__search=keyword)
    except Artist.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)

# For Global Search


@csrf_exempt
@api_view(['GET'])
def global_search(request, keyword):
    """
    Search music data tables for a keyword and return all results
    """
    SearchResults = namedtuple('SearchResults', ('artists', 'djs', 'episodes'))
    try:
        search_results = SearchResults(
            artists=Artist.objects.filter(
                artist_name__icontains=keyword).order_by('-play_count', 'artist_id')[:20],
            
            djs=Dj.objects.filter(
                dj_name__icontains=keyword).order_by('-episode_count', 'dj_id')[:20],
                        
            episodes=Episode.objects.filter(
                Q(episode_name__icontains=keyword) | Q(episode_url__icontains=keyword) | Q(episode_description__icontains=keyword)).order_by('-episode_date', 'episode_id')[:20],
        )
    except Artist.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GlobalSearchSerializer(search_results)
        return JsonResponse(serializer.data, safe=False)


# For Artist info page:
@csrf_exempt
@api_view(['GET'])
def artist_details(request, artist_id):
    ArtistDetails = namedtuple(
        'ArtistDetails', ('artist', 'episodes', 'djs', 'song_artists'))
    try:
        # Get artist name
        artist = Artist.objects.get(pk=artist_id)

        # Find episodes which played a specific artist, ranked by episode date
        episodes = Episode.objects.all().prefetch_related('setlist_set')
        episodes = episodes.filter(
            song_artists__artist_id=artist_id).order_by('-episode_date', 'episode_id')[:15]

        # Find DJs which played that artist
        djs = Dj.objects.all().prefetch_related('episodes')
        djs = djs.filter(episodes__in=episodes).annotate(
            artistdetails_episode_count=Count('episodes')).order_by('-artistdetails_episode_count', 'dj_id')[:15]

        # Songs by the artist which were included in Setlists (ranked by play count, descending)
        song_artists = SongArtist.objects.filter(artist_id=artist_id).annotate(songartist_play_count=Count(
            'setlist')).order_by('-songartist_play_count', 'song_artist_id').select_related('song').select_related('artist')[:15]

        # Package for serialization
        artist_details = ArtistDetails(artist, episodes, djs, song_artists,)

    # Serialize
    except Artist.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArtistDetailsSerializer(artist_details)
        return JsonResponse(serializer.data, safe=False)


# For DJ Info Page:
@csrf_exempt
@api_view(['GET'])
def dj_details(request, dj_id):
    DjDetails = namedtuple('DjDetails', ('dj', 'episodes', 'artists'))
    try:
        # Get DJ name
        dj = Dj.objects.get(dj_id=dj_id)

        # Find episodes performed by a DJ, ranked by episode date
        episodes = Episode.objects.all().prefetch_related('dj_set')
        episodes = episodes.filter(dj__dj_id=dj_id).order_by(
            '-episode_date')[:15]

        # Find artists which the DJ uses in their mixes
        song_artists = SongArtist.objects.all().prefetch_related('episode').filter(episode__in=episodes).annotate(
            songartist_play_count=Count('setlist')).order_by('-songartist_play_count').select_related('song').select_related('artist')

        artists = Artist.objects.all().prefetch_related('songartist_set')
        artists = artists.filter(songartist__in=song_artists).annotate(
            djdetails_play_count=Count('songartist')).order_by('-djdetails_play_count')[:15]

        # Package for serialization
        dj_details = DjDetails(dj, episodes, artists)

    # Serialize
    except Dj.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = DjDetailsSerializer(dj_details)
        return JsonResponse(serializer.data, safe=False)


# GET all Artists, DJs, Episodes

class ArtistListPlayCount(generics.ListCreateAPIView):
    queryset = Artist.objects.order_by('-play_count')[:500]
    serializer_class = ArtistPlayCountSerializer


class DjListEpisodeCount(generics.ListCreateAPIView):
    queryset = Dj.objects.order_by('-episode_count')[:500]
    serializer_class = DjEpCountSerializer


class EpisodeList(generics.ListCreateAPIView):
    queryset = Episode.objects.order_by('-episode_date')[:500]
    serializer_class = EpisodeSerializer


""" BOOKMARK MANAGEMENT """


@csrf_exempt
def bookmark_list(request):
    """
    List all bookmarks, or create a new bookmark.
    """
    if request.method == 'GET':
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmarks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookmarkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def bookmark_detail(request, pk):
    """
    Retrieve, update, or delete a bookmark
    """
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookmarkSerializer(bookmark)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookmarkSerializer(bookmark, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bookmark.delete()
        return HttpResponse(status=204)
