from django.urls import path
from okay import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    # path('artists/photos', views.ArtistDetail.as_view(), name='artist_detail'),
    path('photos/', views.PhotoList.as_view(), name='photo_list'),
    path('photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'),
    # path('reviews/', views.ReviewList.as_view(), name='review_list'),
    # path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

]