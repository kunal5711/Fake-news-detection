from flask import Flask, request, render_template
import pandas as pd
import pickle
import re

app = Flask(__name__)

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as file1:
    vectorizer = pickle.load(file1)

# Load the model
with open('model.pkl', 'rb') as file2:
    model = pickle.load(file2)
    
def word(text):
    # Convert into lowercase
    text = text.lower()
    # Remove urls
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    # Remove punctations
    text = re.sub(r'[^\w\s]', "", text)
    # Remvoe digits
    text = re.sub(r"\d", "", text)
    # Remove newline characters
    text = re.sub(r"\n", " ", text)
    return text

def manual_testing(news):
    df_test = {"text": pd.Series([news])}
    df_test['text'] = df_test['text'].apply(word)
    df_test['text'] = vectorizer.transform(df_test['text'])
    y_preds = model.predict(df_test['text'])
    if y_preds == 0:
        return "It is a fake news"
    else:
        return "It is a genuine news"
    


@app.route("/", methods = ["GET", "POST"])
def home():
    
    if request.method == "POST":
        news = request.form['article']       
        result = manual_testing(news)
        return render_template("index.html", result = result)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)