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

    for item in watchlist:
        if item["title"] == title:
            #Remove item of type dict from watchlist of type list
            watchlist.remove(item)
            watched_movies.append(item)
            return user_data
    
    # If the title wasn't found, return the original data
    return user_data


# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    sum_rating = 0
    count = 0

    
    #In case when watched_movies is an empty list
    if watched_movies == []:
        return 0.0
    # Iterate through list of dicts called watched_movies
    else:
        for movie in watched_movies:
            sum_rating += movie["rating"]
            count += 1
    # Access the rating key in that dict
    # Sum every rating and calculate average
    
        return sum_rating/count

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    genre_dict = {}

    #In case when watched_movies is an empty list
    if watched_movies == []:
        return None
    # Iterate through list of dicts called watched_movies
    else:
        for movie in watched_movies:
            if movie["genre"] not in genre_dict:
                genre_dict[movie["genre"]] = 1
            else:
                genre_dict[movie["genre"]] += 1

    print(genre_dict)

    #Get the key with the maximum value 
    most_watched_genre_count = 0
    most_watched_genre = ""

    # Iterate through list of dicts called genre_dict
    for genre in genre_dict.keys():
        if genre_dict[genre] > most_watched_genre_count:
            most_watched_genre_count = genre_dict[genre]
            most_watched_genre = genre
    return most_watched_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
#How to get friend's dictionary? - Must access element from friends list, watched key from dict, and title key from dict.
# Friends is a list of friends of watched dictionaries of movie dictionaries
# Watched is a list of movie dictionaries

def get_unique_watched(user_data):
    #Get the user watched dictionaries
    user_watched_movies = user_data["watched"]
    #Get the friend watched dictionaries
    friends = user_data["friends"]
    
    friends_watched_movies = set()
    #For every friend in list of friends:
    for friend in friends:
        #For every movie in watched dictionary:
        for  movie in friend['watched']:
            #Add movie title to a set
            friends_watched_movies.add(movie["title"])

    only_user_watched = []
    #For every movie in watched list:
    for movie in user_watched_movies:
        #--- Looking at dictionary now ----#
        #Query if the title of the movie dict is not in the set of movie titles watched by friend
        if movie["title"] not in friends_watched_movies:
            #Add the dictionary to a list (of movies only watched by user)
            only_user_watched.append(movie)

    #Return list of dicts representing movies that only user has watched.
    return only_user_watched

# user_data = {
    #     "watched": [
    #         {
    #             "title": MOVIE
    #             "genre": FANTASY
    #             "rating": 2.0
    #         },
    #         {
    #             "title": MOVIE
    #             "genre": COMEDY
    #             "rating": 2.0
    #         }
    #     ]
    #     "friends": [
    #         {
    #             "watched": [
    #                 {       
    #                 "title": MOVIE
    #                 "genre": HORROR
    #                 "rating": 2.0
    #                 },
    #                 {
    #                 "title": MOVIE
    #                 "genre": HORROR
    #                 "rating": 2.0
    #                 }
    #             ]

    #         }

    #     ]

    # }


#Put the diff from user's set and friend's set 

#The movie that the user has watched but that the friend has not watched.
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

