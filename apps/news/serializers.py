from rest_framework import serializers
from django.db.models import Q
from news.models import News, NewsType


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = "_all_"


class NewsSerializer(serializers.ModelSerializer):
    news_type = NewsTypeSerializer()

    class Meta:
        model = News
        fields = "_all_"
