# coding=utf-8

"""
Module that uses the content of media.py to define class movie
"""
import media
import requests
import json
import fresh_tomatoes

"""
 Constants for disocovery url and Image url as well as API key
 Before running this python code make sure to replace the API key with YOUR API KEY)  # noqa
 Discover URL is By popularity

"""
IMAGE_URL = "https://image.tmdb.org/t/p/w500"
DISCOVER_URL = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?&api_key="  # noqa
API_KEY = '3ffde410d62fa9617bb816fa0215335d'
VIDEO_URL = "https://www.youtube.com/watch?v="


def make_video_url(movie_id, api_key):

    """
    get Video link from themoviedb database

    :param movie_id:
    :param api_key:
    :return:
    """

    MOVIE_URL = "https://api.themoviedb.org/3/movie/"
    LANG = "&language=en-US"
    # Find the youtube key for video trailer
    connection = requests.get(MOVIE_URL + str(movie_id) +
                              "/videos?api_key=" + api_key + LANG)
    videos_json = json.loads(connection.text)
    connection.close()

    if connection.status_code != 200:
        # constant in case issue is found with connection....
        return VIDEO_URL + '5PSNL1qE6VY'
    else:
        if len(videos_json['results']) == 0:
            # constant in case no video is found for given movie....
            return VIDEO_URL + '5PSNL1qE6VY'
        else:
            # If all well we get aa video url for all movie
            # based on discovery or discovery by year
            return VIDEO_URL + videos_json['results'][0]['key']

movies = []
connection = requests.get(DISCOVER_URL + API_KEY)
movies_json = json.loads(connection.text)
connection.close()
for rows in movies_json['results']:
    # encodeing was required to deal with special characters
    # coming as part of movie data
    title = rows['title'].encode('utf-8')
    story_line = rows['overview'].encode('utf-8')
    img_url = IMAGE_URL + str(rows['poster_path'])
    movie_id = rows['id']
    v_url = make_video_url(movie_id, API_KEY)

    # create and append movie insatnce
    movies.append(media.Movie(title, story_line, img_url, v_url))

# Generate Web Page
fresh_tomatoes.open_movies_page(movies)
