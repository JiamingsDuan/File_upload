from django.urls import path
from app01 import views


urlpatterns = [
    path('upload/', views.upload, name='upload')
]
