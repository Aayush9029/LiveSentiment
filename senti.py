from webbrowser import get
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from rich import print

def get_color(score):
    if score < -0.05:
        return 'red'
    elif score > -0.5 and score < 0.05:
        return 'yellow'
    else:
        return 'green'

def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return get_color(score['compound'])



def print_chat(message=""):
    color = get_sentiment(message)
    print(f"[{color}] {message}")