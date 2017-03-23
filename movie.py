import video


class Movie(video.Video):

    """Data struction for movies"""

	# Init using the same variable names fresh_tomatoes.py will look for
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        # Init the super-class
        video.Video.__init__(self, movie_title, movie_storyline,
                             poster_image, trailer_youtube)


