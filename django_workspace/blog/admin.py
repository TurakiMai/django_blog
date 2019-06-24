from django.contrib import admin

# Register your models here.
from blog.models import Blog, Category, Article, Tag, IndexTitle
# 注册该模型
from comment.models import Comment


# admin.site.register(Blog)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['body']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 列表显示列
    list_display = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # 列表显示列
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'views']


@admin.register(IndexTitle)
class IndexTitleAdmin(admin.ModelAdmin):
    list_display = ['heading', 'subheading']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'text', 'created_time']
