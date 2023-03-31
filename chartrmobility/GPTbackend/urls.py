from django.urls import path, include
from .views import GPTgenerator
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', GPTgenerator.as_view(), name='gpt_generator'),
]
