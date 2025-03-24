# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #Create a data structure for each movie
    movie = {}

    #Check if title, genre, rating parameters are TRUE
    if title and genre and rating != None:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie 

    #Check if title, genre, rating parameters are FALSE
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {}
    #Create a "watched" list
    watched = []

    #Set the "watched" key to the list of watched movies as a value
    user_data["watched"] = watched

    #Add movie to the watched list
    watched.append(movie)

    return user_data






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

