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



def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched_movies = user_data["watched"]

    #print(watchlist[0]["title"])
    for item in watchlist:
        if item["title"] == title:
            #Remove item of type dict from watchlist of type list
            watchlist.remove(item)
            watched_movies.append(item)
            return user_data
    
    # If the title wasn't found, return the original data
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

