from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    
    if request.method == 'POST':
        # Get the input from the form
        user_input = request.form['user_input']
        
        # Perform sentiment analysis
        sentiment_scores = analyzer.polarity_scores(user_input)
        
        # Determine sentiment based on compound score
        if sentiment_scores['compound'] >= 0.05:
            sentiment = 'Positive'
        elif sentiment_scores['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        
        return render_template('index.html', result=user_input, sentiment=sentiment)
    
    # If it's a GET request or the initial visit, render the form
    return render_template('index.html', result=None, sentiment=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
