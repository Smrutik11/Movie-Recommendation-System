# Movie Recommendation System

A movie recommendation system built using the **MovieLens 100K dataset**. The project explores different collaborative filtering approaches and uses **SVD Matrix Factorization** to predict movie ratings and generate Top-N recommendations for users.

The final model is connected to a simple **Streamlit application** where a user can enter a User ID and get personalized movie recommendations.

---

## Why I Built This

I wanted to understand how recommendation systems work beyond simply recommending the most popular movies.

This project helped me work through the complete process — from exploring user-rating data and building collaborative filtering models to evaluating the models and turning the final model into a small interactive application.

---

## What the Project Does

The system:

- Analyzes movie rating patterns
- Explores user and movie activity
- Builds User-Based Collaborative Filtering
- Builds Item-Based Collaborative Filtering
- Trains an SVD Matrix Factorization model
- Evaluates the recommendation models
- Generates Top-N movie recommendations
- Provides an interactive Streamlit interface

---

## Dataset

The project uses the **MovieLens 100K dataset** from GroupLens Research.

The dataset contains:

- **100,000 ratings**
- **943 users**
- **1,682 movies**
- Ratings from **1 to 5**

The main files used are:

```text
u.data
u.item
