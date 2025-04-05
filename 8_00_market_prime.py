import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

target_accounts = ["Trade_Proooo", "CliffCapital", "AlphaInvest0", "tradesavvy999","FinFlex0", "t.me/MarketPrimeDaily","t.me/+M4WgsaOvIYExMWE1","t.me/+rD5KolqapallNmRl","t.me/+H-YpbIqETXEyYTc1"]
# Define the target channel
account_messages = '''Welcome to MarketPrime! 

Start your day with in-depth pre-market reports, key market trends, and expert analysis on global and Indian indices. Stay ahead, trade smarter, and dominate the markets with MarketPrime! 

**Launching Daily Newsletter "Market Prime"** 🚀

This NewsLetter is just posted in our Market Prime Premium Channel 🤩

Covering Following 🙂 

**A. Market Sentiment: The Big Picture**

1. Sentiment Index
2. Global Markets
3. FII & DII Activity
4. Global Economic Events

**B. Trader’s Toolkit: Today Key Insights**

1. Today's Market Outlook
2. Technical Analysis
3. Options Data
4. Weekly Expiry PCR
5. Stocks in Focus: Bullish & Bearish

**C. Opportunities: What’s on the Radar?**

1. Upcoming IPOs
2. Market Decoder

**Grab your copy now  to enhance your daily trades by joining our Premium Channel by clicking on the link below :**

https://superprofile.bio/vig/67c431f18e42300013724ab2

@ just Rs.1999/- per year 😊'''

# Start Telethon client
client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
        now = datetime.now()
        target_time = now.replace(hour=8, minute=0, second=0, microsecond=0)  # 9:00 AM

        if now > target_time:
            target_time += timedelta(days=1)  # Move to the next day if already past 9 AM

        wait_time = (target_time - now).total_seconds()
        print(f"Waiting for {wait_time} seconds until {target_time}")

        await asyncio.sleep(wait_time)  # Wait until the scheduled time
        # Send message
        for destination_channel in target_accounts:
            await client.send_message(destination_channel, account_messages, link_preview=False)

        await asyncio.sleep(60)  # Prevent double sending

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())
