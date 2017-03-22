import movie
import tvshow

toy_story = movie.Movie("Toy Story", "Toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
this_is_us = tvshow.TV_Show("This Is Us", "A dramedy about a millennial family",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgzMTcyMTE0MF5BMl5BanBnXkFtZTgwOTk1ODY5MDI@._V1_.jpg",
                            "https://www.youtube.com/watch?v=MQ86ycli47w",
                            "http://titantv.com/search/search.aspx?stxt=this+is+us")
this_is_us.show_video()
