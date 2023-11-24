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
    # Страница добавления новой темы
    path("new_topic/", views.new_topic, name="new_topic"),
    # Страница для добавления новой записис для конкретной темы
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # Странциа для изменения существующей записи ( редактирование )
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    
]
