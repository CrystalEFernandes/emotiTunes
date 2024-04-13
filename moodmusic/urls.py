from django.urls import path
from . import views

urlpatterns = [
    path('detect-mood/', views.detect_mood, name='detect_mood'),
    path('all-songs/', views.render_all_songs, name='all_songs'), 
]
