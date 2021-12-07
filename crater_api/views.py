from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.postgres.search import SearchVector
from crater_api.models import Artist, Dj, Episode, Genre, SongArtist
from crater_api.serializers import ArtistSerializer, BookmarkSerializer, EpisodeSerializer, DjSerializer, GlobalSearchSerializer, ArtistDetailsSerializer
from collections import namedtuple

# TODO: update to psycopg2 instead of psycopg-binary

""" ARTIST """
@csrf_exempt
def artist_list(request):
    """
    List all artists, or create a new artist.
    """
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)

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


@csrf_exempt
def global_search(request, keyword):
    """
    Search music data tables for a keyword and return all results
    """
    SearchResults = namedtuple('SearchResults', ('artists', 'djs', 'episodes'))
    try:
        search_results = SearchResults(
            artists=Artist.objects.annotate(search=SearchVector(
                'artist_name'),).filter(search=keyword),
            djs=Dj.objects.annotate(search=SearchVector(
                'dj_name'),).filter(search=keyword),
            episodes=Episode.objects.annotate(
                search=SearchVector('episode_name', 'episode_url', 'episode_description'),).filter(search=keyword),
        )
    except Artist.DoesNotExist & Dj.DoesNotExist & Episode.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GlobalSearchSerializer(search_results)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def artist_details(request, artist_id):
    ArtistDetails = namedtuple('ArtistDetails', ('episodes', 'djs', 'song_artists'))
    try:
        # Find episodes which played a specific artist, ranked by episode date
        episodes = Episode.objects.filter(song_artists__artist_id=artist_id).order_by(
            '-episode_date')

        # Find DJs which played that artist          
        djs = Dj.objects.filter(episodes__in=episodes)
    
        # Songs by the artist which were included in Setlists (ranked by play count, descending)
        song_artists = SongArtist.objects.filter(artist_id=artist_id).annotate(play_count=Count('setlist')).order_by('-play_count').select_related('song').select_related('artist')
        
        # Package for serialization
        artist_details = ArtistDetails(episodes, djs, song_artists,)
    
    # Serialize
    except Episode.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArtistDetailsSerializer(artist_details)
        return JsonResponse(serializer.data, safe=False)



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
