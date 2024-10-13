import pandas as pd
import numpy as np

data = {'The Matrix': [5, 4, 1, 0],
        'Titanic': [4, 0, 5, 2],
        'Inception': [5, 0, 0, 3],
        'Avatar': [0, 3, 4, 4],
        'The Godfather': [0, 5, 4, 3]}

df = pd.DataFrame(data, index=['User1', 'User2', 'User3', 'User4'])

def find_similar_user(target_user):
    target_ratings = df.loc[target_user]
    best_similarity = 0
    best_user = None

    for user in df.index:
        if user != target_user:
            common_movies = (target_ratings != 0) & (df.loc[user] != 0)
            if any(common_movies):
                similarity = np.dot(target_ratings[common_movies], df.loc[user][common_movies])
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_user = user

    return best_user

def recommend_movies(target_user):
    similar_user = find_similar_user(target_user)
    recommendations = []

    if similar_user:
        for movie in df.columns:
            if df.loc[target_user, movie] == 0 and df.loc[similar_user, movie] > 0:
                recommendations.append(str(movie))

    return recommendations

recommended_movies = recommend_movies('User3')

print(f"Movies recommended for User3: {recommended_movies}")
