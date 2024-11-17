import requests
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

def fetch_data():
    # Fetch data from APIs
    url1 = "https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
    headers1 = {"Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"}
    viewed_posts = requests.get(url1, headers=headers1).json()

    url2 = "https://api.socialverseapp.com/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
    headers2 = {"Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"}
    liked_posts = requests.get(url2, headers=headers2).json()

    url3 = "https://api.socialverseapp.com/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
    headers3 = {"Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"}
    ratings = requests.get(url3, headers=headers3).json()

    url4 = "https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000"
    headers4 = {"Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"}
    posts = requests.get(url4, headers=headers4).json()

    url5 = "https://api.socialverseapp.com/users/get_all?page=1&page_size=1000"
    headers5 = {"Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"}
    users = requests.get(url5, headers=headers5).json()

    # Convert JSON data to DataFrames
    viewed_posts = pd.DataFrame(viewed_posts)
    liked_posts = pd.DataFrame(liked_posts)
    ratings = pd.DataFrame(ratings)
    posts = pd.DataFrame(posts)
    users = pd.DataFrame(users)

    full_data = pd.concat([viewed_posts, liked_posts, ratings, users, posts], ignore_index=True)
    posts_df = pd.json_normalize(full_data['posts'])
    full_df = pd.concat([full_data.drop(columns='posts'), posts_df], axis=1)
    return full_df

def preprocess_data(full_df):
    # Aggregate data and create a user-item matrix
    aggregated_df = full_df.groupby(['username', 'id'])['view_count'].sum().reset_index()
    user_item_matrix = aggregated_df.pivot(index='username', columns='id', values='view_count').fillna(0)
    return user_item_matrix

def recommend_posts(user_item_matrix, user_index, num_recommendations):
    # Apply Truncated SVD
    interaction_matrix = user_item_matrix.values
    svd = TruncatedSVD(n_components=50)
    svd_matrix = svd.fit_transform(interaction_matrix)
    svd_matrix = np.dot(svd_matrix, svd.components_)

    user_similarity = cosine_similarity(svd_matrix)

    # Find similar users
    similarity_scores = user_similarity[user_index]
    similar_users = similarity_scores.argsort()[::-1][1:]

    # Find unseen posts and recommend
    user_interactions = interaction_matrix[user_index]
    unseen_posts = np.where(user_interactions == 0)[0]

    recommended_posts = []
    for similar_user in similar_users:
        similar_user_interactions = interaction_matrix[similar_user]
        for post in unseen_posts:
            if similar_user_interactions[post] > 0:
                if post in recommended_posts:
                    pass
                else :
                    recommended_posts.append(post)
            if len(recommended_posts) >= num_recommendations:
                return recommended_posts
    return recommended_posts

def get_post_details(full_df, recommendations):
    recommended_details = []
    for post_index in recommendations:
        if post_index in full_df['id'].values:
            post_data = full_df.loc[full_df['id'] == post_index]
            recommended_details.append(post_data[['title', 'video_link']])
    return recommended_details
