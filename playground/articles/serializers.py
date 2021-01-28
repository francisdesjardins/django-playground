from rest_framework import serializers
from playground.articles import models as playground_articles_models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = playground_articles_models.Article
        fields = ["id", "title", "content", "priority", "created", "updated", "deleted"]


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = playground_articles_models.ArticleComment
        fields = ["article", "content"]
