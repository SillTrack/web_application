"""Определяет схемы URL для learning_logs"""

from django.urls import path

from . import views


app_name = "learning_logs"
urlpatterns = [
    # Домашняя странциа
    path("", views.index, name="index"),
    # Страница со списком тем
    path("topics", views.topics, name="topics"),
    # Страница подробной информации по отдельной теме
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
