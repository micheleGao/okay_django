from django.shortcuts import render
from rest_framework import generics
from .serializers import ArtistSerializer, PhotoSerializer
from .models import Artist, Photo
from rest_framework import permissions
from okay.permissions import IsOwnerOrReadOnly

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class =PhotoSerializer
    permission_classes = [IsOwnerOrReadOnly]

