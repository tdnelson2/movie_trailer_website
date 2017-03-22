import video

class Movie(video.Video):
    """Data struction for movies"""

    def __init__(self, title, storyline, poster, trailer_url):
        print("Movie constructor initiated")
        video.Video.__init__(self, title, storyline, poster, trailer_url)
