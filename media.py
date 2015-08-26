class Movie():
    '''
    Creates instances of movies with various attributes.

    Attributes:
        title: A string indicating the title of the movie
        trailer_youtube_url: A string providing the url of the
        movie's youtube trailer
        genre: The movie's genre
        poster_image_url: A string of the url for the movie's poster
        year_released: An int indicating the year the movie was released
        personal_rating: A float between 0 and 5 indicating a movie rating
        review: A string containing a brief review of the movie
    '''
    def __init__(self, title, trailer_youtube_url, genre, year_released, poster_image_url, personal_rating, review):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.genre = genre
        self.poster_image_url = poster_image_url
        self.year_released = year_released
        self.personal_rating = personal_rating
        self.review = review
        
