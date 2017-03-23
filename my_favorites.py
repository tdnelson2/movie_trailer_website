import movie
import fresh_tomatoes


# Create objects for each title
arrival = movie.Movie("Arrival",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=ZLO4X6UI8OY")

finding_nemo = movie.Movie("Finding Nemo",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=SPHfeNgogVs")

la_la_land = movie.Movie("La La Land",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # NOQA
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

passengers = movie.Movie("Passengers",
                         "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

petes_dragon = movie.Movie("Pete's Dragon",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Petes_dragon_2016_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=fPOamb6d_20")

wilderpeople = movie.Movie("Hunt for the Wilderpeople",
                           "https://upload.wikimedia.org/wikipedia/en/4/44/Hunt_for_the_Wilderpeople.png",  # NOQA
                           "https://www.youtube.com/watch?v=lfT2uq_rNms")

the_lobster = movie.Movie("The Lobster",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BNDQ1NDE5NzQ1NF5BMl5BanBnXkFtZTgwNzA5OTM2NTE@._V1_UY268_CR3,0,182,268_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=iFDncw9-1yw")

the_martian = movie.Movie("The Martian",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=ej3ioOneTy8&t=61s")

the_revenant = movie.Movie("The Revenant",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

mad_max = movie.Movie("Mad Max: Fury Road",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

star_wars = movie.Movie("Star Wars: The Force Awakens",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

bridge_of_spies = movie.Movie("Bridge of Spies",
                              "https://upload.wikimedia.org/wikipedia/en/f/fa/Bridge_of_Spies_poster.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=7JnC2LIJdR0")

movies = [arrival, finding_nemo, la_la_land, passengers, petes_dragon,
          wilderpeople, the_lobster, the_martian, the_revenant, mad_max,
          star_wars, bridge_of_spies]

# Build the movie trailer website
fresh_tomatoes.open_movies_page(movies)
