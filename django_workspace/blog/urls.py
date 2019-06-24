from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    #     url(r'^$', views.index, name="index"),
    #     # path('', views.index, name='index'),
    # #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #     url(r'^(?P<question_id>[0-9]+)/$', views.blogRender, name='blogRender')

    path('', views.index, name='index'),

    path('blogList/', views.blog_render, name='blog_list'),

    path('blogDetail/<int:pk>', views.blog_detail, name='blog_detail')
]
