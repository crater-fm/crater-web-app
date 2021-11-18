from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.postgres.search import SearchVector
from crater_api.models import Artist, Dj, Episode
from crater_api.serializers import ArtistSerializer, DjSerializer, EpisodeSerializer, BookmarkSerializer, GlobalSearchSerializer
from collections import namedtuple

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
def artist_detail(request, pk):
    """
    Retrieve, update, or delete an artist
    """
    try:
        artist = Artist.objects.get(pk=pk)
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
        #print(search_results)
    except Artist.DoesNotExist & Dj.DoesNotExist & Episode.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GlobalSearchSerializer(search_results)
        return JsonResponse(serializer.data, safe=False)

    """
    if request.method == 'GET':
        artist_serializer = ArtistSerializer(artists, many=True)
        artists_json = JsonResponse(artist_serializer.data, safe=False)
        artists_json_enclosed = [{'dataType': 'Artist', 'data': artists_json}]
        dj_serializer = DjSerializer(djs, many=True)
        dj_json = JsonResponse(dj_serializer.data, safe=False)
        print(ArtistSerializer.Meta.model)
        return artists_json
"""


""" BOOKMARK """


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
