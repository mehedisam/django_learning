from django.forms import ValidationError
from watchlist.models import WatchList, StreamList, Review
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from watchlist.api.serializers import WatchlistSerializer,StreamSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .permission import ReviewOwnerOrReadOnly,IsAdminOrReadOnly
from .throttling import ReviewCreateThrottling,ReviewListThrottling
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import ReviewListPagination

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes=[ReviewCreateThrottling]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watch = get_object_or_404(WatchList, pk=pk)
        user = self.request.user

        if Review.objects.filter(watchlist=watch, review_user=user).exists():
            error={'error':'You have already reviewed this movie'}
            raise Response(error)
        
        if watch.avg_rating == 0:
            watch.avg_rating = serializer.validated_data['rating']
        else:
            watch.avg_rating=(watch.avg_rating+serializer.validated_data['rating'])/2
        watch.num_ratings += 1
        watch.save()

        serializer.save(watchlist=watch, review_user=user)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # throttle_classes=[ReviewListThrottling]
    # filter_backends = [DjangoFilterBackend]

    # filterset_fields = ['review_user__username','active']
    pagination_class=ReviewListPagination

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewListDetail(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[ReviewOwnerOrReadOnly]

# class ReviewListDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    


# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)







class StreamListAV(APIView):
    def get(self,request):
        platform=StreamList.objects.all()
        serializer = StreamSerializer(platform, many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer=StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
class StreamListDetailAV(APIView):
    def get(self,request,pk):
        try:
            movielist=StreamList.objects.get(pk=pk)
        except movielist.DoesNotExist:
            return Response({'error':'Not found'},status=400)
        serializer=StreamSerializer(movielist)
        return Response(serializer.data, status=200)
    def put(self,request,pk):
        movie = StreamList.objects.get(pk=pk)
        serializer = StreamSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    def delete(self, request, pk):
        movie = StreamList.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)

class WatchListAV(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        search_query = request.query_params.get('search')
        ordering = request.query_params.get('ordering') 
        if search_query:
            movielist = WatchList.objects.filter(title__icontains=search_query)
        else:
            movielist = WatchList.objects.all()
        if ordering:
            movielist=movielist.order_by(ordering)
        serializer = WatchlistSerializer(movielist, many=True)
        return Response(serializer.data,status=200)
    
    def post(self, request):
        permission_classes = [IsAdminOrReadOnly]
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class WatchListDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except movie.DoesNotExist:
            return Response({'error':'Not Found'}, status=400)
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data, status=200)
        

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)


# @api_view(['GET', 'POST'])
# def watchlist_list(request):
#     if request.method=='GET':
#         movielist = Movie.objects.all()
#         serializer= WatchlistSerializer(movielist,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def watchlist_detail(request, pk):
#     if request.method == 'GET':
#         movie=Movie.objects.get(pk=pk)

#         serializer = WatchlistSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
        