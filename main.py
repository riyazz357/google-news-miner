import requests
from bs4 import BeautifulSoup
import csv
import os

def get_google_news(topic):
    # 1. The URL (We use the RSS feed for stability)
    # %20 replaces spaces in the topic
    formatted_topic = topic.replace(" ", "%20")
    url = f"https://news.google.com/rss/search?q={formatted_topic}&hl=en-US&gl=US&ceid=US:en"

    print(f"🔄 Fetching news for: '{topic}'...")

    # 2. The Request
    # We pretend to be a browser so Google doesn't ignore us
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        
        # 3. Parsing the Data (XML)
        # We use BeautifulSoup to cut through the raw code
        soup = BeautifulSoup(response.content, features="xml")
        
        # Find all news items
        items = soup.find_all("item")
        
        news_list = []
        
        # Limit to top 20 results
        for item in items[:20]:
            title = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            
            news_list.append([title, pub_date, link])
            
        return news_list

    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def save_to_csv(news_data, topic):
    filename = f"{topic.replace(' ', '_')}_news.csv"
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Header Row
        writer.writerow(["Headline", "Date", "Link"])
        # Data Rows
        writer.writerows(news_data)
        
    print(f"✅ Success! Saved {len(news_data)} articles to '{filename}'")

# --- MAIN LOOP ---
if __name__ == "__main__":
    print("--- 📰 Google News Scraper ---")
    user_topic = input("Enter a topic to search (e.g., Python, SpaceX): ")
    
    if user_topic:
        data = get_google_news(user_topic)
        
        if data:
            save_to_csv(data, user_topic)
            
            # Preview top 3
            print("\n--- Top 3 Headlines ---")
            for i, article in enumerate(data[:3], 1):
                print(f"{i}. {article[0]}")
        else:
            print("No news found.")