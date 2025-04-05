import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient
import os

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"
client = TelegramClient("session_name", api_id, api_hash)
# 🔹 List of 5 channel IDs/usernames
target_accounts = ["tradesavvy999", "Trade_Proooo", "CliffCapital", "AlphaInvest0", "FinFlex0"]

# 🔹 List of 10 images (Each channel gets 2 images)

IMAGES = [
    "TradeSavvy1.jpg","TradeSavvy2.jpg",
    "TradePro1.jpg", "TradePro2.jpg",
    "CliffCapital1.jpg", "CliffCapital2.jpg",
    "AlphaInvest1.jpg", "AlphaInvest2.jpg",
    "FinFlex1.jpg","FinFlex2.jpg",
]

async def upload_images():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        for i, channel in enumerate(target_accounts):
            try:
                # Select 2 images per channel
                image1 = IMAGES[i * 2]
                image2 = IMAGES[i * 2 + 1]

                # Upload first image
                await client.send_file(channel, image1)
                await asyncio.sleep(2)  # Wait 2 seconds to avoid spam

                # Upload second image
                await client.send_file(channel, image2)
                await asyncio.sleep(2)  # Wait 2 seconds to avoid spam

                print(f"✅ Successfully uploaded images to {channel}")

            except Exception as e:
                print(f"❌ Failed to upload images to {channel}: {e}")

# 🔹 Run the async function
asyncio.run(upload_images())
