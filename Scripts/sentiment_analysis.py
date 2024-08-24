
import pandas as pd
from textblob import TextBlob  

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def main():

    df = pd.read_csv('Data/output/scraped_data.csv')
    
    
    df['sentiment'] = df['content'].apply(analyze_sentiment)
    
    
    df.to_csv('data/output/sentiment_results.csv', index=False)
    print("Sentiment analysis completed and saved to 'data/output/sentiment_results.csv'.")

if __name__ == "__main__":
    main()
