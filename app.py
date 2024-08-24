from Scripts.web_scraping import main as scrape_main
from Scripts.sentiment_analysis import main as sentiment_main

if __name__ == "__main__":
    # run web scraping
    print("Starting web scraping...")
    scrape_main()
    
    # Run sentiment analysis
    print("Starting sentiment analysis...")
    sentiment_main()
