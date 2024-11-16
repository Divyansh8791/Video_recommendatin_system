# import requests

# url = "https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# headers = {
#     "Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# viewed_posts = requests.get(url, headers=headers).json()

# url = "https://api.socialverseapp.com/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# headers = {
#     "Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# liked_posts = requests.get(url, headers=headers).json()

# url = "https://api.socialverseapp.com/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# headers = {
#     "Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# ratings = requests.get(url, headers=headers).json()

# url = "https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000"
# headers = {
#     "Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# posts = requests.get(url, headers=headers).json()

# url = "https://api.socialverseapp.com/users/get_all?page=1&page_size=1000"
# headers = {
#     "Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# users = requests.get(url, headers=headers).json()


# import pandas as pd

# viewed_posts_df = pd.DataFrame(viewed_posts)
# liked_posts_df = pd.DataFrame(liked_posts)
# ratings_df = pd.DataFrame(ratings)
# posts_df = pd.DataFrame(posts)
# users_df = pd.DataFrame(users)

# posts_df = pd.json_normalize(viewed_posts_df['posts'])

# full_df = pd.concat([viewed_posts_df.drop(columns='posts'), posts_df], axis=1)

# aggregated_df = full_df.groupby(['username', 'id'])['view_count'].sum().reset_index()
# user_item_matrix = aggregated_df.pivot(index='username', columns='id', values='view_count').fillna(0)
 
# from sklearn.decomposition import TruncatedSVD
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np


# interaction_matrix = user_item_matrix.values
# #print(interaction_matrix)


# svd = TruncatedSVD(n_components=50)  
# svd_matrix = svd.fit_transform(interaction_matrix)

# #print(svd_matrix)
# svd_matrix = np.dot(svd_matrix, svd.components_)
# # print(svd_matrix)
# # 

# user_similarity = cosine_similarity(svd_matrix) 

# def recommend_posts(user_index, num_recommendations=5):
    
#     similarity_scores = user_similarity[user_index]
    
#     similar_users = similarity_scores.argsort()[::-1][1:]
    
    
#     user_interactions = interaction_matrix[user_index]
    
    
#     unseen_posts = np.where(user_interactions == 0)[0]
    
    
#     recommended_posts = []
#     for similar_user in similar_users:
#         similar_user_interactions = interaction_matrix[similar_user]
#         for post in unseen_posts:
#             if similar_user_interactions[post] > 0:  
#                 recommended_posts.append(post)
                
#             if len(recommended_posts) >= num_recommendations:
#                 return recommended_posts

#     return recommended_posts


# recommended_posts = recommend_posts(user_index=0, num_recommendations=5)
# print(f"Recommended posts for user 0: {recommended_posts}") 

# from sklearn.decomposition import TruncatedSVD
# n_latent_features = 9  
# svd = TruncatedSVD(n_components=n_latent_features)  

# svd_matrix = svd.fit_transform(interaction_matrix)  

# predicted_ratings = np.dot(svd_matrix, svd.components_)

# top_5_recommendations = np.argsort(predicted_ratings, axis=1)[:, -5:]


# for user_index, recommendations in enumerate(top_5_recommendations):
#     print(f"Top 5 recommendations for User {user_index + 1}: {recommendations}")


# for user_index, recommendations in enumerate(top_5_recommendations):
#     print(f"Top 5 recommendations for User {user_index + 1}:")
#     for post_index in recommendations:
#         post_data = full_df.loc[full_df['id'] == post_index]  
#         print(post_data[['title', 'video_link']])    



# import requests
# import pandas as pd
# from sklearn.decomposition import TruncatedSVD
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import sys

# # Ensure UTF-8 encoding for output
# sys.stdout.reconfigure(encoding='utf-8')

# # Fetch viewed posts
# url = "https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# headers = {
#     "Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# viewed_posts = requests.get(url, headers=headers).json()

# # Fetch liked posts
# url = "https://api.socialverseapp.com/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# liked_posts = requests.get(url, headers=headers).json()

# # Fetch ratings
# url = "https://api.socialverseapp.com/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# ratings = requests.get(url, headers=headers).json()

# # Fetch posts summary
# url = "https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000"
# headers = {
#     "Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# posts = requests.get(url, headers=headers).json()

# # Fetch users
# url = "https://api.socialverseapp.com/users/get_all?page=1&page_size=1000"
# users = requests.get(url, headers=headers).json()

# # Create dataframes
# viewed_posts_df = pd.DataFrame(viewed_posts)
# liked_posts_df = pd.DataFrame(liked_posts)
# ratings_df = pd.DataFrame(ratings)
# posts_df = pd.DataFrame(posts)
# users_df = pd.DataFrame(users)

# # Normalize and process data
# posts_df = pd.json_normalize(viewed_posts_df['posts'])
# full_df = pd.concat([viewed_posts_df.drop(columns='posts'), posts_df], axis=1)
# aggregated_df = full_df.groupby(['username', 'id'])['view_count'].sum().reset_index()
# user_item_matrix = aggregated_df.pivot(index='username', columns='id', values='view_count').fillna(0)

# # Collaborative filtering with SVD
# interaction_matrix = user_item_matrix.values
# svd = TruncatedSVD(n_components=50)
# svd_matrix = svd.fit_transform(interaction_matrix)
# svd_matrix = np.dot(svd_matrix, svd.components_)
# user_similarity = cosine_similarity(svd_matrix)

# # Recommendation function
# def recommend_posts(user_index, num_recommendations=5):
#     similarity_scores = user_similarity[user_index]
#     similar_users = similarity_scores.argsort()[::-1][1:]
#     user_interactions = interaction_matrix[user_index]
#     unseen_posts = np.where(user_interactions == 0)[0]
#     recommended_posts = []
#     for similar_user in similar_users:
#         similar_user_interactions = interaction_matrix[similar_user]
#         for post in unseen_posts:
#             if similar_user_interactions[post] > 0:
#                 recommended_posts.append(post)
#             if len(recommended_posts) >= num_recommendations:
#                 return recommended_posts
#     return recommended_posts

# # Recommend posts for a user
# recommended_posts = recommend_posts(user_index=0, num_recommendations=5)
# print(f"Recommended posts for user 0: {recommended_posts}")

# # Predict top recommendations using SVD
# n_latent_features = 9
# svd = TruncatedSVD(n_components=n_latent_features)
# svd_matrix = svd.fit_transform(interaction_matrix)
# predicted_ratings = np.dot(svd_matrix, svd.components_)
# top_5_recommendations = np.argsort(predicted_ratings, axis=1)[:, -5:]

# # Display top 5 recommendations for each user
# for user_index, recommendations in enumerate(top_5_recommendations):
#     print(f"Top 5 recommendations for User {user_index + 1}: {recommendations}")

#     print(f"Top 5 recommendations for User {user_index + 1}:")
#     for post_index in recommendations:
#         post_data = full_df.loc[full_df['id'] == post_index]
#         print(post_data[['title', 'video_link']])


# import requests
# import pandas as pd
# from sklearn.decomposition import TruncatedSVD
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import sys

# # Ensure UTF-8 encoding for output
# sys.stdout.reconfigure(encoding='utf-8')

# # Fetch viewed posts
# url = "https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# headers = {
#     "Authorization": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# viewed_posts = requests.get(url, headers=headers).json()

# # Fetch liked posts
# url = "https://api.socialverseapp.com/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# liked_posts = requests.get(url, headers=headers).json()

# # Fetch ratings
# url = "https://api.socialverseapp.com/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
# ratings = requests.get(url, headers=headers).json()

# # Fetch posts summary
# url = "https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000"
# headers = {
#     "Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
# }
# posts = requests.get(url, headers=headers).json()

# # Fetch users
# url = "https://api.socialverseapp.com/users/get_all?page=1&page_size=1000"
# users = requests.get(url, headers=headers).json()

# # Create dataframes
# viewed_posts_df = pd.DataFrame(viewed_posts)
# liked_posts_df = pd.DataFrame(liked_posts)
# ratings_df = pd.DataFrame(ratings)
# posts_df = pd.DataFrame(posts)
# users_df = pd.DataFrame(users)

# # Normalize and process data
# posts_df = pd.json_normalize(viewed_posts_df['posts'])
# full_df = pd.concat([viewed_posts_df.drop(columns='posts'), posts_df], axis=1)
# aggregated_df = full_df.groupby(['username', 'id'])['view_count'].sum().reset_index()
# user_item_matrix = aggregated_df.pivot(index='username', columns='id', values='view_count').fillna(0)

# # Collaborative filtering with SVD
# interaction_matrix = user_item_matrix.values
# svd = TruncatedSVD(n_components=50)
# svd_matrix = svd.fit_transform(interaction_matrix)
# svd_matrix = np.dot(svd_matrix, svd.components_)
# user_similarity = cosine_similarity(svd_matrix)

# # Recommendation function
# def recommend_posts(user_index, num_recommendations=5):
#     similarity_scores = user_similarity[user_index]
#     similar_users = similarity_scores.argsort()[::-1][1:]  # Exclude self
#     user_interactions = interaction_matrix[user_index]
#     unseen_posts = np.where(user_interactions == 0)[0]
#     recommended_posts = []
#     for similar_user in similar_users:
#         similar_user_interactions = interaction_matrix[similar_user]
#         for post in unseen_posts:
#             if similar_user_interactions[post] > 0:
#                 recommended_posts.append(post)
#             if len(recommended_posts) >= num_recommendations:
#                 return recommended_posts
#     return recommended_posts

# # Recommend posts for a user
# recommended_posts = recommend_posts(user_index=0, num_recommendations=5)
# print(f"Recommended posts for user 0: {recommended_posts}")

# # Predict top recommendations using SVD
# n_latent_features = 9
# svd = TruncatedSVD(n_components=n_latent_features)
# svd_matrix = svd.fit_transform(interaction_matrix)
# predicted_ratings = np.dot(svd_matrix, svd.components_)
# top_5_recommendations = np.argsort(predicted_ratings, axis=1)[:, -5:]

# # Display top 5 recommendations for each user
# for user_index, recommendations in enumerate(top_5_recommendations):
#     print(f"Top 5 recommendations for User {user_index + 1}: {recommendations}")
    
#     # Check each recommendation and print post data if available
#     for post_index in recommendations:
#         post_data = full_df[full_df['id'] == post_index]
#         if not post_data.empty:
#             print(post_data[['title', 'video_link']])
#         else:
#             print("no data.")


import requests
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Fetch data functions
def fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    return response.json()


# Prepare DataFrames and data processing
def prepare_data():
    headers = {
    "Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
     }
    # Fetch data
    viewed_posts = fetch_data("https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if", headers)
    liked_posts = fetch_data("https://api.socialverseapp.com/posts/like?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if", headers)
    ratings = fetch_data("https://api.socialverseapp.com/posts/rating?page=1&page_size=5&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if", headers)
    posts = fetch_data("https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000", headers)
    users = fetch_data("https://api.socialverseapp.com/users/get_all?page=1&page_size=1000", headers)
    
    # Create DataFrames
    viewed_posts_df = pd.DataFrame(viewed_posts)
    posts_df = pd.DataFrame(posts)
    
    # Normalize and process data
    posts_df = pd.json_normalize(viewed_posts_df['posts'])
    full_df = pd.concat([viewed_posts_df.drop(columns='posts'), posts_df], axis=1)
    
    return full_df

# Collaborative filtering and recommendation logic
def recommend_posts(user_index, interaction_matrix, user_similarity, num_recommendations=5):
    similarity_scores = user_similarity[user_index]
    similar_users = similarity_scores.argsort()[::-1][1:]  # Exclude self
    user_interactions = interaction_matrix[user_index]
    unseen_posts = np.where(user_interactions == 0)[0]
    recommended_posts = []
    for similar_user in similar_users:
        similar_user_interactions = interaction_matrix[similar_user]
        for post in unseen_posts:
            if similar_user_interactions[post] > 0:
                recommended_posts.append(post)
            if len(recommended_posts) >= num_recommendations:
                return recommended_posts
    return recommended_posts

# Function to prepare recommendation matrix
def prepare_recommendation_matrix():
    full_df = prepare_data()
    
    aggregated_df = full_df.groupby(['username', 'id'])['view_count'].sum().reset_index()
    user_item_matrix = aggregated_df.pivot(index='username', columns='id', values='view_count').fillna(0)
    interaction_matrix = user_item_matrix.values
    svd = TruncatedSVD(n_components=50)
    svd_matrix = svd.fit_transform(interaction_matrix)
    svd_matrix = np.dot(svd_matrix, svd.components_)
    user_similarity = cosine_similarity(svd_matrix)
    
    return full_df, user_item_matrix, user_similarity
