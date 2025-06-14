# 🏡 AirBnB Sentiment Analysis Dashboard

An interactive web dashboard that performs **sentiment analysis on Airbnb reviews** using a TF-IDF + Logistic Regression pipeline, and presents the results with beautiful, responsive Plotly charts.

---

## 📖 Overview

This Dash application loads a CSV of Airbnb reviews, cleans and preprocesses the text, applies a pre-trained sentiment model to classify each review as **Positive**, **Neutral**, or **Negative**, and visualizes the data with:

- **Indicator Cards** showing totals, averages, and percentage breakdowns  
- **Bar Charts** of sentiment counts by reviewer and by sentiment  
- **Treemap “Word-Cloud”** of the top 100 most frequent words  
- **Doughnut (Pie) Chart**, **Bubble Chart**, and **Polar Area Chart** for sentiment distributions  
- **Time-Series Line Charts** tracking review volume and sentiment trends over time

---

## 🚀 Features

- **Data Loading & Cleaning**  
  - Reads `reviews.csv`, drops duplicates & nulls  
  - Strips punctuation, lowercases, removes stopwords  

- **Sentiment Model**  
  - TF-IDF vectorizer + Logistic Regression  
  - Trainable pipeline saved as `Models/tfidf_vectorizer.pkl` & `Models/logistic_regression_model.pkl`  

- **Live Review Submission**  
  - Users can enter new text and see an immediate sentiment prediction  

- **Interactive Dash Layout**  
  - Responsive Bootstrap grid via **dash-bootstrap-components**  
  - Spinner indicators for loading states  
  - Route-based pages: Home, Raw Data, Cleaned Data, Sentiment Analysis, Submit Review  

---

## ⚙️ Prerequisites

- **Python 3.8+**  
- **Git** (to clone the repo)  
- A terminal (macOS/Linux) or PowerShell/CMD (Windows)

---

## 🛠️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/EdwardZ069/AirBnb-Sentiment-Analysis.git
   cd AirBnb-Sentiment-Analysis
