from django.db import models

PRIORITY_MEH = 0
PRIORITY_WHAAAAT = 1
PRIORITY_NOOOO = 2
PRIORITY_CHOICES = (
    (PRIORITY_MEH, "Meh..."),
    (PRIORITY_WHAAAAT, "Whaaaat?"),
    (PRIORITY_NOOOO, "Noooo!"),
)


class Article(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(blank=True, null=True)

    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=PRIORITY_MEH)
    title = models.CharField(max_length=100, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "articles_article"
        ordering = ["created"]


class ArticleComment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT,
        related_name="comments",
        related_query_name="comment",
    )
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "articles_article_comment"
        ordering = ["created"]
