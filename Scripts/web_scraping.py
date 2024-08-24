import pandas as pd
import requests
from bs4 import BeautifulSoup


df_urls = pd.read_excel(r'C:\Users\vdtul\OneDrive\Documents\GitHub\NewsMoodAnalyzer\Data\input\Input.xlsx')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}


def scrape_url(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        
        
        title = soup.find("h1", attrs={'class': "entry-title"})
        content = soup.find("div", attrs={'class': "td-post-content tagdiv-type"})
        
    
        if not title or not content:
            title = soup.find("h1")
            content = soup.find("div", attrs={'class': "content-area"})
        
        return title.text.strip(), content.text.strip()
    except Exception as e:
        print(f"Failed to scrape {url}: {str(e)}")
        return None, None

def main():
    
    data = []
    
    
    for index, row in df_urls.iterrows():
        title, content = scrape_url(row['URL'])  # Adjust this line based on actual column name
        if title and content:
            data.append({'title': title, 'content': content})
    
    
    df_data = pd.DataFrame(data)
    df_data.to_csv('data/output/scraped_data.csv', index=False)
    print("Data scraping completed and saved to 'data/output/scraped_data.csv'.")

if __name__ == "__main__":
    main()
