# Video Recommendation System

The **Video Recommendation System** is a Python-based project that leverages machine learning to recommend posts to users based on their interaction data. This application utilizes collaborative filtering and matrix factorization techniques to analyze user preferences and deliver personalized recommendations. Built with Streamlit, the project provides an intuitive web-based interface for easy interaction.

---

## Key Features

- **API-Driven Data Fetching**: Retrieves data for users, posts, and interactions like views, likes, and ratings from APIs.
- **Data Aggregation & Normalization**: Combines raw data into structured DataFrames for analysis and modeling.
- **Recommendation Algorithm**: Employs collaborative filtering using Truncated SVD and cosine similarity to predict unseen post preferences.
- **Interactive Frontend**: Offers a user-friendly dashboard to explore recommendations and inspect post details.

---

## Technologies Used

- **Python**: Core programming language.
- **Pandas**: Data manipulation and processing.
- **Scikit-learn**: Machine learning for recommendations.
- **Streamlit**: Web framework for building the frontend.
- **APIs**: Data fetching for user interactions and post metadata.
