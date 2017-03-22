import video

class TV_Show(video.Video):
    """Data structure for TV Shows"""
    def __init__(self, title, description, thumb, trailer_url, listings_url):
        print("TV Show constructor initiated")
        video.Video.__init__(self, title, description, thumb, trailer_url)
        self.listings_url = listings_url
        
