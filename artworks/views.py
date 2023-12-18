# artworks/views.py

import requests
from django.shortcuts import render
from artworks.models import Artwork

def artwork_list(request):
    api_key = 'abb53b86-ab26-41ee-bb5c-32bac71dcf53'
    
    # Handling search queries
    query = request.GET.get('q')
    
    search_results = []

    if query:
        
        url = 'https://api.harvardartmuseums.org/object'
        params = {
            'apikey': api_key,
            'title': query,
            'fields': 'objectnumber,title,dated,primaryimageurl',
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Extracting data
        artworks_data = data.get('records', [])

        # tried to filter out artworks without an image
        artworks_data_with_images = [artwork for artwork in artworks_data if 'primaryimageurl' in artwork]

        # Build Artwork objects from the API data
        search_results = [
            Artwork(
                title=artwork.get('title', 'Untitled'),
                artist=artwork.get('people', [{'name': 'Unknown Artist'}])[0]['name'],
                description=artwork.get('dated', 'No date available'),
                image_url=artwork.get('primaryimageurl', None),
            )
            for artwork in artworks_data_with_images
        ]
    else:
        
        pass

    context = {'search_results': search_results, 'query': query}
    return render(request, 'artworks/artwork_list.html', context)
