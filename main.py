# main.py

import requests
from scraper.news_scraper import fetch_news_headlines
from haiku_generator.haiku_bot import construct_haiku
from config.settings import DISCORD_WEBHOOK_URL

GROUP_NUMBER = 10  # Group number for the haiku signature

def send_to_discord(haiku):
    """Sends the haiku to a Discord channel using a webhook."""
    haiku_with_group = f"{haiku}\n~ {GROUP_NUMBER}"  
    payload = {"content": haiku_with_group}
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("✅ Haiku successfully posted to Discord!")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send haiku. Error: {e}")

# Run the bot
if __name__ == "__main__":
    try:
        headlines = fetch_news_headlines()
        haiku = construct_haiku(headlines)
        send_to_discord(haiku)
        print("\nGenerated Haiku:\n", haiku + f"\n~ {GROUP_NUMBER}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
