# from django.shortcuts import render
# from movielist.models import Movie
# from django.http import JsonResponse
#
#
# def movie_lis(request):
#     movies = Movie.objects.all()
#     return JsonResponse(movies.values())
#
#
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
