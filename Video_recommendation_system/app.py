import streamlit as st
import pandas as pd
from vid_rec import prepare_recommendation_matrix, recommend_posts

# Set up Streamlit title
st.title('Socialverse Post Recommendations')

# Prepare data and recommendation matrix
full_df, user_item_matrix, user_similarity = prepare_recommendation_matrix()

# Sidebar for user selection
user_index = st.sidebar.slider('Select User Index', 0, len(user_item_matrix) - 1, 0)

# Get top recommendations for the selected user
num_recommendations = st.sidebar.slider('Select Number of Recommendations', 1, 10, 5)

# Display user index and number of recommendations
st.write(f"Showing top  {num_recommendations} recommendations for User  : {user_index + 1}.")

# Get recommended post indices
recommended_posts = recommend_posts(user_index=user_index, interaction_matrix=user_item_matrix.values, user_similarity=user_similarity, num_recommendations=num_recommendations)

# Display the recommended posts
for post_index in recommended_posts:
    post_data = full_df[full_df['id'] == post_index]
    if not post_data.empty:
        st.write(f"Title: {post_data['title'].values[0]}")
        st.write(f"Video Link: {post_data['video_link'].values[0]}")
    else:
        st.write("No data available for this post.")
