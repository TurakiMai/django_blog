from django.urls import path

from comment import views

app_name = "comment"

urlpatterns = [


    path('sumbit_comment/<int:pk>', views.sumbit_comment, name='sumbit_comment'),


]