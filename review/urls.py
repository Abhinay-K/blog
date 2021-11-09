from django.urls import path
from . import views
from .views import HomeView ,NovelReviewView
urlpatterns =[
    #path('',views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('review/<int:pk>',NovelReviewView.as_view(),name="review"),
    path('post_a_review',views.write_a_review,name="write_a_review"),
]