from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from .models import Posts


# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
