import os
from django.db import models

# Choices for the 'mood' field
MOOD_CHOICES = [
    ('Angry', 'Angry'),
    ('Happy', 'Happy'),
    ('Neutral', 'Neutral'),
    ('Sad', 'Sad'),
    ('Surprise', 'Surprise'),
]

def get_song_upload_path(instance, filename):
    # Assuming mood is stored as a field in the instance
    return os.path.join('song_mp3', instance.mood, filename)

def get_image_upload_path(instance, filename):
    # Assuming mood is stored as a field in the instance
    return os.path.join('song_images', instance.mood, filename)

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES) 
    mp3 = models.FileField(upload_to=get_song_upload_path) 
    image = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
