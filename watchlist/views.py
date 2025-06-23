# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from .models import Movie


# # Create your views here.


# def watchlist_list(request):
#     movie= Movie.objects.all()
#     data={
#         "movie": list(movie.values())
#     }

#     return JsonResponse(data)