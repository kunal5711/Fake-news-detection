# Fake News Detection

This is a web-based application that detects whether a given news article is real or fake. The application uses machine learning and natural language processing (NLP) techniques to classify the news as "Fake" or "Genuine".

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [How to Use](#how-to-use)
- [Screenshots](#screenshots)

## Overview

Fake news is a serious problem in today’s digital age, leading to the spread of misinformation. This project aims to help mitigate this problem by using a machine learning model to identify fake news articles based on their content.

## Features

- **User-friendly Interface**: Enter news content and receive an instant result.
- **Real-time Prediction**: Utilizes a trained model to classify news as either Fake or Genuine.
- **Input Cleaning**: Text preprocessing to remove URLs, HTML tags, digits, and punctuation for accurate predictions.

## Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, Pandas, TfidfVectorizer, Decision Tree Classifier Model
- **Frontend**: HTML, CSS, Jinja2
- **Data Storage**: Vectorizer and Model saved using Pickle

## Project Setup

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/fake-news-detection.git
    cd fake-news-detection
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask app**:

    ```bash
    python app.py
    ```

6. **Open your web browser** and go to `http://127.0.0.1:5000/`.

## How to Use

1. Open the web application.
2. Enter the news article text into the input box.
3. Click the **"Check Now"** button.
4. The application will return the result as either **"It is a fake news"** or **"It is a genuine news"**.


## Screenshots

![Fake News Detection Screenshot](Screenshot.png)

## Future Improvements

- **Model Improvements**: Implement additional machine learning models to improve accuracy.
- **More Preprocessing**: Enhance text preprocessing techniques.
- **Data Updates**: Keep the model updated with new datasets to stay current with evolving news trends.

## Acknowledgements

- Thanks to the open-source community for providing valuable datasets and tools.
- **scikit-learn**, **Flask**, and **Jinja2** are used extensively in this project.