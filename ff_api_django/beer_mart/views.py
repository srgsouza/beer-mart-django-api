# Create your views here.
from django.shortcuts import render, redirect

from .models import Beer, Comment
from .forms import BeerForm, CommentForm

## API-related imports
from rest_framework import generics
# from .serializers import BeerSerializer, CommentSerializer
from .serializers import BeerSerializer, CommentSerializer


# Decorator.  Gets called before a function that has '@login_required' preceeding it.  
from django.contrib.auth.decorators import login_required

# To integrate built-in users
from django.contrib.auth.models import User
from beer_mart.serializers import UserSerializer
from rest_framework import permissions
from beer_mart.permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BeerList(generics.ListCreateAPIView):
  # queryset = Beer.objects.all().prefetch_related('user')
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
  # queryset = Beer.objects.all().prefetch_related('user')
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all().prefetch_related('beer')
  serializer_class = CommentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all().prefetch_related('beer')
  serializer_class = CommentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 