# Movie Trailer Website
The purpose of this project is to populate a website template using a data structure written in python.
## Use
Currently all the movie title data is in `my_favorites.py`. In the future, the data will be in a separate mySQL database.
## Installation
* In Terminal run `git clone https://github.com/tdnelson2/movie_trailer_website.git`
* Open `my_favorites.py` in a Python interpreter running Python 2.7
* Run the module
* If the module executes correctly, the website should appear automatically
## Customization
To add additional movies to the website, append this to the end of the `movies` list in `my_favorites.py` substituting everything within the quotes with the appropriate data:
~~~
,
          movie.Movie("<<MOVIE TITLE HERE>>",
                      "<<URL TO MOVIE POSTER IMAGE HERE>>",  # NOQA
                      "<<URL TO MOVIE TRAILER ON YOUTUBE HERE>>")
~~~