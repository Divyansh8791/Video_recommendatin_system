import streamlit as st
from vid_rec import fetch_data, preprocess_data, recommend_posts, get_post_details

# Streamlit App
st.title("Video Recommendation System")

# Fetch and preprocess data
st.write("Fetching data from APIs...")
full_df = fetch_data()
user_item_matrix = preprocess_data(full_df)
st.success("Data successfully fetched and preprocessed!")

# User input for recommendations
user_indices = list(range(len(user_item_matrix.index)))
selected_user_index = st.selectbox("Select a User Index", user_indices)

num_recommendations = st.slider(
    "Number of Recommendations", min_value=1, max_value=20, value=5
)

# Generate recommendations on button click
if st.button("Generate Recommendations"):
    st.write(f"Generating recommendations for User {selected_user_index}...")
    recommended_posts = recommend_posts(user_item_matrix, selected_user_index, num_recommendations)
    
    # Fetch post details
    st.write("Fetching details for recommended posts...")
    recommended_details = get_post_details(full_df, recommended_posts)
    
    # Display recommendations
    st.subheader(f"Top {num_recommendations} Recommendations for User {selected_user_index}:")
    if recommended_details:
        for details in recommended_details:
            st.write(details)
    else:
        st.write("No recommendations found.")
