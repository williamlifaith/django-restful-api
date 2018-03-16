from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer


# Create your views here.

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()[:10]
    serializer_class = NewsSerializer
