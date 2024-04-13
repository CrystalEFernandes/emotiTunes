from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .recog3 import return_mood, class_labels  

from django.shortcuts import render
from django.http import JsonResponse
from .recog3 import return_mood

from django.shortcuts import render
from django.http import JsonResponse
from .recog3 import return_mood
from .models import Song  # Import your Song model here

def detect_mood(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')  # Get the base64-encoded image data
        mood_index = return_mood(image_data)  # Pass the base64-encoded image data
        print("Mood index:", mood_index)  # Print mood_index for debugging
        if mood_index is not None and isinstance(mood_index, int):
            mood_label = class_labels[mood_index]
            # Fetch songs based on mood index
            songs = Song.objects.filter(mood=mood_label)
            song_data = []
            for song in songs:
                song_data.append({
                    'name': song.title,
                    'artist': song.artist,
                    'image_url': song.image.url,
                    'mp3_url': song.mp3.url,
                })
            return JsonResponse({'result': mood_label, 'songs': song_data})
        else:
            # If mood index is not detected, return an error response
            return JsonResponse({'error': 'Face not detected'}, status=400)
    else:
        # If it's not a POST request, return an error response
        return JsonResponse({'error': 'Invalid request method'}, status=405)



from django.shortcuts import render
from .models import Song  # Import your Song model here

def render_all_songs(request):
    # Fetch all songs from the database
    all_songs = Song.objects.all()

    # Pass the list of songs to the template for rendering
    return render(request, 'dashboard.html', {'songs': all_songs})
