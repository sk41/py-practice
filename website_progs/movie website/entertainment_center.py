import media
import fresh_tomatoes


sanju= media.Movie("sanju","Coming from a family of cinematic legends, East Indian actor Sanjay Dutt reaches dizzying heights of success "
                           "-- but also battles numerous addictions and other personal demons.","https://upload.wikimedia.org/wikipedia/en/e/e5/Sanju_-"
                                                                                                "_Theatrical_poster.jpg","https://www.youtube.com/watch?v=1J76wN0TPI4")
#sanju.poster_image_url
padmavat=media.Movie("Padmavat","story of queen padmavati","https://upload.wikimedia.org/wikipedia/en/7/73/Padmaavat_poster.jpg","https://www.youtube.com/watch?v=X_5_BLt76c0")

race3=media.Movie("Race 3","Race 3 is an internationally mounted saga of a family that deals in borderline crime but is ruthless and vindictive to the core",
                  "https://upload.wikimedia.org/wikipedia/en/8/8a/Race_3_-_Poster.jpg","https://www.youtube.com/watch?v=xBht9TG7ySw")

raazi=media.Movie("Raazi","An Indian spy marries a Pakistani man during the Indo-Pakistan War of 1971.","https://upload.wikimedia.org/wikipedia/en/2/2f/Raazi_-_Poster.jpg",
                  "https://www.youtube.com/watch?v=YjMSttRJrhA")

movies=[sanju,padmavat,race3,raazi]
fresh_tomatoes.open_movies_page(movies)





