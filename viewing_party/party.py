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

    for movie in watchlist:
        if movie["title"] == title:
            #Remove item of type dict from watchlist of type list
            watchlist.remove(movie)
            watched_movies.append(movie)
    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    sum_rating = 0
    count = 0
    average_rating = 0.0
    
    #In case when watched_movies is an empty list
    if watched_movies == []:
        return average_rating
    # Iterate through list of dicts called watched_movies
    else:
        for movie in watched_movies:
            sum_rating += movie["rating"]
            count += 1
    # Access the rating key in that dict
    # Sum every rating and calculate average
    average_rating = sum_rating/count
    return average_rating

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

    #Get the key with the maximum value 
    most_watched_genre_count = 0
    most_watched_genre = ""

    # Iterate through list of dicts called genre_dict
    for genre in genre_dict.keys():
        if genre_dict[genre] > most_watched_genre_count:
            most_watched_genre_count = genre_dict[genre]
            most_watched_genre = genre
    return most_watched_genre


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    
    friends_watched_set = set()
    unique_watched = []

    #Iterate through the movies in nested friends_list
    for friend in friends_list:
        for movie in friend["watched"]:  
            if movie in user_watched_list:
                friends_watched_set.add(movie["title"])

    #Iterate through the movies in user_watched_list
    for movie in user_watched_list:
        if movie["title"] not in friends_watched_set:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    
    user_watched_set = set()
    unique_watched = []

    #Get set of movie titles watched by user
    for movie in user_watched_list:
        user_watched_set.add(movie["title"])

    #Iterate through each friend in friends_list
    for friend in friends_list:
        #For every movie dict in friend dict
        for movie in friend["watched"]: 
            #If title is not in user_watched_set AND title is not in unique_watched_set:
            if movie["title"] not in user_watched_set and movie not in unique_watched:
                unique_watched.append(movie)
    return unique_watched
    


# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    unique_movie = get_friends_unique_watched(user_data)
    recommended_movies = []
    
    for movie in unique_movie:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    unique_movie = get_friends_unique_watched(user_data)
    user_watched_list = user_data["watched"]
    genre_dict = {}
    recommended_movies = []

    for movie in user_watched_list:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        else:
            genre_dict[movie["genre"]] += 1
    
    most_watched_genre = ""
    most_count = 0
    for genre, count in genre_dict.items():
        if count > most_count:
            most_count = count
            most_watched_genre = genre

    for movie in unique_movie:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):
    favorites_dict = user_data["favorites"]
    unique_movie = get_unique_watched(user_data)
    recommended_movies = []

    for movie in favorites_dict:
        if movie in unique_movie:
            recommended_movies.append(movie)
    return recommended_movies