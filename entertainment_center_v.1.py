import media
import requests
import json
import fresh_tomatoes
#print (media.Movie.__name__)
#print (media.Movie.__module__)
#print (media.Movie.__doc__)
# Constants for disocovery url and Image url as well as API key ( Before running this python code make sure to replace the API key with YOUR API KEY)
IMAGE_URL = "https://image.tmdb.org/t/p/w500"
DISCOVER_URL = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?&api_key=" #By popularity
#DISCOVER_URL = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2011&sort_by=vote_average.desc&api_key=" #By release Year
API_KEY = '3ffde410d62fa9617bb816fa0215335d'
VIDEO_URL = "https://www.youtube.com/watch?v="

def make_video_url(movie_id, api_key):

    MOVIE_URL = "https://api.themoviedb.org/3/movie/"
    LANG = "&language=en-US"
    # Find the youtube key for video trailer
    connection = requests.get(MOVIE_URL + str(movie_id) +
                              "/videos?api_key=" + api_key + LANG)
    videos_json = json.loads(connection.text)
    connection.close()
    #print videos_json
    if connection.status_code != 200:
        return VIDEO_URL + '5PSNL1qE6VY'  # constant in case issue is found with connection....
    else:
       if len(videos_json['results']) == 0:
          return VIDEO_URL + '5PSNL1qE6VY' # constant in case no video is found for given movie....I have checked many movies do not have video urls.So handled it
       else:
          return VIDEO_URL + videos_json['results'][0]['key'] # If all well we get aa video url for all movie based on discovery or discovery by year

movies = []
connection = requests.get(DISCOVER_URL + API_KEY)
movies_json = json.loads(connection.text)
connection.close()
#popularity = movies_json['results'][0]
#print popularity
for rows in movies_json['results']:
    title = rows['title'].encode('utf-8') #encodeing was required to deal with special character coming as part of movie data
    story_line = rows['overview'].encode('utf-8') #encodeing was required to deal with special character coming as part of movie data
    img_url = IMAGE_URL + str(rows['poster_path'])
    movie_id = rows['id']
    v_url = make_video_url(movie_id, API_KEY)
    #print v_url
    movies.append(media.Movie(title, story_line, img_url, v_url)) # create and append movie insatnce

# Generate Web Page
fresh_tomatoes.open_movies_page(movies)
