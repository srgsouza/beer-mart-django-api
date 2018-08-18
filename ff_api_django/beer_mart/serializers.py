from rest_framework import serializers
from .models import Beer, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    beers = serializers.PrimaryKeyRelatedField(many=True, queryset=Beer.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'beers')


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Beer
        fields = ('brewery_name', 'beer_name', 'description', 'abv', 'price', 'package', )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'beer', 'owner')

