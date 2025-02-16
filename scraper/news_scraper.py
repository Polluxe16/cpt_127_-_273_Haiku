# scraper/news_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_news_headlines():
    """Fetches the latest news headlines from Google News RSS."""
    rss_url = "https://news.google.com/rss"

    try:
        response = requests.get(rss_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch news: {e}")
        return []

    soup = BeautifulSoup(response.content, "lxml-xml")  # Explicitly use lxml
    news_items = soup.find_all("item")

    #  Debugging: Print total number of items found
    print(f"DEBUG: Found {len(news_items)} news items.")

    headlines = [item.title.text for item in news_items[:10]]

    # Debugging: Print fetched headlines
    print("DEBUG: Fetched Headlines:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

    return headlines

