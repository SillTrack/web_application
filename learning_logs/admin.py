from django.contrib import admin
from .models import Topic, Entry


# Регистрировать мои модели здесь
admin.site.register(Topic)
admin.site.register(Entry)
