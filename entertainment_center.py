import fresh_tomatoes
import media

# some information about rampage movie
rampage = media.movie(
    "Rampage",
    "is a 2018 American science fiction monster"
    "film directed by Brad Peyton",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQp"
    "TCKCvU_Fz0SwP_oyuSSKdf_unn88WWa5evQC4F3U7EfHyQVJ",
    "https://www.youtube.com/watch?v=k4jGZQIoknQ")
# some information about spiderman movie
spiderman = media.movie(
    "spiderMan",
    "s a 2017 American superhero film based on"
    " the Marvel Comics character Spider-Man,",
    "https://upload.wikimedia.org/wikipedia/en/"
    "f/f9/Spider-Man_Homecoming_poster.jpg",
    "https://www.youtube.com/watch?v=NbLP_SmhtuM"
    )
# some information about black_panther movie
black_panther = media.movie(
    "black panther",
    "s a 2018 American superhero film based on"
    "the Marvel Comics character of the same name",
    "https://upload.wikimedia.org/wikipedia/en"
    "/0/0c/Black_Panther_film_poster.jpg",
    "https://www.youtube.com/watch?v=iSwppsDP7jM"
    )
# some information about wonder movie
wonder = media.movie(
    "wonder",
    "s a 2017 American drama film directed by Stephen"
    " Chbosky and written by Jack Thorne, Steve Conrad,",
    "https://upload.wikimedia.org/wikipedia/"
    "en/6/67/Wonder_%28film%29.png",
    "https://www.youtube.com/watch?v=u2soKNPRALc"
    )
# some information about wondr_woman movie
wonder_woman = media.movie(
    "wonder woman",
    "is a 2017 American superhero film based on"
    "the DC Comics character of the same name",
    "https://upload.wikimedia.org/wikipedia/en/"
    "e/ed/Wonder_Woman_%282017_film%29.jpg",
    "https://www.youtube.com/watch?v=VSB4wGIdDwo"
    )
# some information about avengers_infinity_war movie
avengers_infinity_war = media.movie(
    "avengers infinity war",
    " Infinity War is a 2018 American superhero film based "
    "on the Marvel Comics superhero team the Avengers,",
    "https://upload.wikimedia.org/wikipedia/en/"
    "4/4d/Avengers_Infinity_War_poster.jpg",
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
    )
# name of the all movies will dispaly on website
movies = [
    rampage,
    spiderman,
    black_panther,
    wonder,
    wonder_woman,
    avengers_infinity_war]
# this file for to make website
fresh_tomatoes.open_movies_page(movies)
