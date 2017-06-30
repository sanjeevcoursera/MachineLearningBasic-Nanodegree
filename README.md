# Project 1 - Movie Trailer Website
This project is done as part of [Machine Learning Basic Nanodegree](https://in.udacity.com/course/machine-learning-engineer-nanodegree--nd009-in-basic/) course.

## Dependencies
The project requires API key from [The Movie DB](https://www.themoviedb.org/), to generate the movie trailer page.

## Usage
Before running this program do the following
1. Open entertainment_center_v.1.py
2. Find API_KEY Constant
3. Replace api key that you got from [The Movie DB](https://www.themoviedb.org/)

Once you are done with the above steps
You can run entertainment_center.py to see the web page.

Note:
You may choose to produce the movies web page output based on
1. Movies popularity
2. release year

You can play around with other ways of getting your favorite movies by reading https://www.themoviedb.org/documentation/api/discover . All the best !!!

To do that you can comment/uncomment below line of code in entertainment_center_v.1.py
#DISCOVER_URL = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?&api_key=" #By popularity
#DISCOVER_URL = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2011&sort_by=vote_average.desc&api_key=" #By release Year
