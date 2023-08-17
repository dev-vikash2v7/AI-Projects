from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('play/<room_code>',views.play)
]