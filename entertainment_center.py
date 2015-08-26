import media
import fresh_tomatoes
import csv

'''
Gathers data about various movies stored in movie_data.csv,
uses this data to create movie objects, and sends the
movie objects to open_movies_page which renders the movies
in a browser.
'''
movies = []
with open('movie_data.csv', 'rb') as csvreader:
    reader = csv.DictReader(csvreader)
    for row in reader:
        movie = media.Movie(**row)
        movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
