from django.urls import include, path
from watchlist.api import views


urlpatterns = [
    path('',views.WatchListAV.as_view(), name='MovieList'),
    path('<int:pk>/', views.WatchListDetail.as_view(), name='MovieDetail'),
    path('stream/',views.StreamListAV.as_view(),name='SteamList'),
    path('stream/<int:pk>/', views.StreamListDetailAV.as_view(), name='streamDetail'),
    path('stream/<int:pk>/review/', views.ReviewList.as_view(), name='review'),
    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('stream/review/<int:pk>', views.ReviewListDetail.as_view(), name='reviewDetail'),

    # path('review/', views.ReviewList.as_view(), name='review'),
    # path('review/<int:pk>', views.ReviewListDetail.as_view(), name='reviewDetail'),
]
