import webbrowser


class movie():
    """
    summary line.
    the class havetwo function for movie
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        summary line.
        the function is to add information for movie
        parameters
        ----------
        movie_title: string
            title for movie
        movie_storyline: string
            storyline about movie
        pster_image: string
            poster of the movies
        trailer_youtube: string
            trailer of the movies from youtube
        """
        self.title = movie_title
        # variable for title movie
        self.storyline = movie_storyline
        # variable for storyline movie
        self.poster_image_url = poster_image
        # variable for poster movie
        self.trailer_youtube_url = trailer_youtube
        # variable for trailer for movie

    def show_trailer(self):
        # this function for open web browser
        webbrowser.open(self.trailer_youtube_url)
