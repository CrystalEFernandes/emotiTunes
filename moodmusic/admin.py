from django.contrib import admin
from .models import Song  # Import the Song model

# Register the Song model
admin.site.register(Song)