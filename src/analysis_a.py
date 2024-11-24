from textblob import TextBlob

def analyze_sentiment(text):
    
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    
    return score 

