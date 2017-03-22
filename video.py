import webbrowser


class Video():

    """Data structure for videos hosted on youtube"""

    def __init__(self, title, description, thumb, link):
        print("Video constructor initiated")
        self. title = title
        self.description = description
        self.thumb = thumb
        self.link = link

    def show_video(self):
        webbrowser.open(self.link)

