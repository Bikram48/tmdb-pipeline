import requests

BASEURL = "https://api.themoviedb.org"
APIKEY = "c8df32a7e7eccf429d632722313f43d7"


def extract_data(page):
    url = f"{BASEURL}/3/discover/movie?api_key={APIKEY}&page={page}&sort_by=vote_average.desc"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("invalid call")

def transform_data(data):
    transform = []
    
    for info in data['results']:
        transform.append({
            "id": info['id'],
            "title": info['title'],
            "original_language": info['original_language'],
            "overview": info["overview"],
            "release_date": info['release_date'],
            "vote_average": info["vote_average"],
            "vote_count": info['vote_count'],
            "popularity": info['popularity']
        })

total_movies = 0
page = 1
while total_movies<=200:
    movie_info = extract_data(page)
    transform_data(movie_info)
    page += 1
    total_movies += 20

