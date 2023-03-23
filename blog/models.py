from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from tinymce import models as tinymce_models


class Post(models.Model):
    # class Status(models.IntegerChoices):
    #     DRAFT = 0
    #     PUBLIC = 1

    title = models.CharField(
        max_length=150
    )
    description = models.TextField(
        help_text = "For meta-desc tag",
        blank=True,
        null=True,
    )
    content = tinymce_models.HTMLField(help_text = "Content of post")
    author_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    published_at = models.DateTimeField(
        help_text = 'date published',
        blank=True,
        null=True,
    )
    slug = models.CharField(
        max_length = 50,
        unique = True,
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now_add = True
    )
    like = models.IntegerField(
        default = 0
    )
    statuses = models.SmallIntegerField(
        help_text = "0: Draft, 1: Published",
        default = 0
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_posts'


class Comment(models.Model):
    # class Status(models.IntegerChoices):
    #     DRAFT = 0
    #     PUBLIC = 1

    content = models.TextField()
    author_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    post_id = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'blog_comments'