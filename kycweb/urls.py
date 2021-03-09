from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("index/",views.index,name="index"),
    # path('video_feed', views.video_feed, name='video_feed'),
    # path("addfaces/",views.addfaces,name="addfaces"),
    # path('show_video_on_page', views.show_video_on_page, name='show_video_on_page'),
]