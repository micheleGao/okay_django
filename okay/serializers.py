from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Artist
from .models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        queryset=Artist.objects.all(),
        # source='artist'
        # read_only= True,
    )
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset= Artist.objects.all(),
        source = 'artist'
    )
    # owner = serializers.PrimaryKeyRelatedField(
    #     # view_name='Artist_detail',
    #     queryset=Artist.objects.all(),
    #     source='owner.username'
    # )
    # add owner back into the fields when commenting it back in.

    class Meta:
        model = Photo
        fields = ('id','artist','artist_id', 'title', 'album')
        
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail', read_only=True)

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source='artist')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'artist', 'title','artist_id',
                  'body', 'created', 'owner')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # photo = serializers.HyperlinkedRelatedField(
    #     view_name='photo_detail',
    #     many=True,
    #     read_only=True
    # )
    photo= PhotoSerializer(
        many= True,
        read_only = True
    )
    reviews=ReviewSerializer(
        many=True, 
        read_only =True
    )
    artist_url=serializers.ModelSerializer.serializer_url_field(view_name='artist_detail')
    class Meta:
       model = Artist
       fields = ('id', 'photo_url','artist_url', 'nationality', 'name','photo')