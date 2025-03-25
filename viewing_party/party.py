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
    #Check if "watched" key exists:
    if "watched" not in user_data:
        #Set the "watched" key to the list of watched movies as a value
        user_data["watched"] = []  
    #Add movie to the watched list
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #Add movie to watchlist inside of user_data
    if "watchlist" not in user_data:
        user_data["watchlist"] = movie

    user_data["watchlist"].append(movie)
    return user_data


janes_data = {
    "watchlist": [{
        "title": "MOVIE_TITLE_1",
        "genre": "GENRE_1",
        "rating": 4.5
    }],
    "watched": []
}

def watch_movie(user_data, title):
    #Iterate through user_data dictionary by its keys
    for _ in user_data["watchlist"]:
        #If the title is in a movie in the user's watchlist
        if title in user_data["watchlist"]:
            print(f"THE MOVIE TITLE IS: ***** ",{title})
            #add that movie to watched
            #user_data["watched"].append(title)
            
            #remove that movie from the watchlist
            user_data["watchlist"].remove(title)

            return user_data
        else:
            return user_data
        

result = watch_movie(janes_data, "MOVIE_TITLE_1")
print(result)



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

