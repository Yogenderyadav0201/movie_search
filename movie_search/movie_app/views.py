from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from movie_app.models import Movie

API_KEY = '334ace0c6e8e90dfd49bb82cbdd12716'
API_BASE_URL = 'https://api.themoviedb.org/3'

def index(request):
    return render(request, 'index.html')

def about(request):
   return render(request,'about.html')

def contact(request):
   return render(request,'contact.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        return redirect(f'/search/{query}')
    else:
        return render(request, 'search.html')

def search_results(request, query):
    print("query" , query)
    # Make API request to search movies
    response = requests.get(f'{API_BASE_URL}/search/movie', params={'api_key': API_KEY, 'query': query})
    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        return render(request, 'search_results.html', {'movies': movies, 'query': query})
    else:
        return HttpResponse('Error occurred during movie search.')

def movie_details(request, movie_id):
    # Make API request to get movie details
    response = requests.get(f'{API_BASE_URL}/movie/{movie_id}', params={'api_key': API_KEY})
    if response.status_code == 200:
        movie = response.json()
        return render(request, 'movie_details.html', {'movie': movie})
    else:
        return HttpResponse('Error occurred while fetching movie details.')