from datetime import datetime
from django.http.response import Http404

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from playground.exceptions import Http410
from playground.articles.models import Article
from playground.articles.serializers import ArticleSerializer


class ArticleList(APIView):
    def get(self, request):
        snippets = Article.objects.filter(deleted__isnull=True)
        serializer = ArticleSerializer(snippets, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_object(self, pk: int) -> Article:
        try:
            article: Article = Article.objects.get(pk=pk)
        except Article.DoesNotExist as article_no_exists:
            raise Http404 from article_no_exists

        # trying to put something already deleted
        if article.deleted is not None:
            raise Http410

        return article

    def get(self, request, pk: int):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)

        return Response(serializer.data)

    def put(self, request: Request, pk: int):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)

        article.deleted = datetime.utcnow()

        article.save()
