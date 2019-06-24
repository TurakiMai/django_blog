# blog/models.py
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# 博客模型
class Blog(models.Model):
    title = models.CharField(max_length=254, unique=True)
    # 博客的内容为 RichTextField 对象
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


# Category
class Category(models.Model):
    """Category"""
    name = models.CharField(max_length=100, unique=True)


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete=True)  # ForeignKey表示1对多（多个article对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)  # 对应标签，支持ManyToMany
    views = models.PositiveIntegerField(default=0)  # 阅读量

    def add_views(self):
        self.views += 1

        self.save()


class IndexTitle(models.Model):
    heading = models.CharField(max_length=100)

    subheading = models.CharField(max_length=100)

    image = models.CharField(max_length=10, blank=True)
