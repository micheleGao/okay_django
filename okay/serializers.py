from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Artist
from .models import Photo

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset= Artist.objects.all(),
        source = 'artist'
    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Photo
        fields = ('id', 'artist', 'artist_id', 'title', 'album', 'owner')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.HyperlinkedRelatedField(
        view_name='photo_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Artist
       fields = ('id', 'photo_url', 'nationality', 'name', 'photo')