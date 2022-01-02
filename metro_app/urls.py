from django.contrib import admin
from django.urls import path 
from metro_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('AboutUs/', views.AboutUs, name="AboutUs"),
    path('FeedbackForum/', views.FeedbackForum, name="FeedbackForum"),
    path('question/<int:id>', views.questionPage, name="question")


]
