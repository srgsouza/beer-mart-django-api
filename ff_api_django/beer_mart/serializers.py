from rest_framework import serializers
from .models import Beer, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    beers = serializers.PrimaryKeyRelatedField(many=True, queryset=Beer.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'beers')


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Beer
        fields = ('brewery_name', 'beer_name', 'description', 'abv', 'ibu', 'price', 'package', 'user' )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'beer', 'user')

