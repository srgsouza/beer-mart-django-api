from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
  path('api/beers/', views.BeerList.as_view(), name='beer-list'),
  path('api/beers/<int:pk>', views.BeerDetail.as_view(), name='beer-detail'),
  path('api/comments/', views.CommentList.as_view(), name='comment-list'),
  path('api/comments/<int:pk>', views.CommentDetail.as_view(), name='comment-detail'),
  url(r'^users/$', views.UserList.as_view()),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), 
  url(r'^api-auth/', include('rest_framework.urls')), 
]