import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

target_accounts = ["Trade_Proooo", "CliffCapital", "AlphaInvest0", "tradesavvy999","FinFlex0", "t.me/+M4WgsaOvIYExMWE1","t.me/+rD5KolqapallNmRl","t.me/+H-YpbIqETXEyYTc1"]
# Define the target channel
account_messages = '''Daily Market Prime Newsletter will be shared here https://t.me/MarketPrimeDaily

Do join to Stay ahead, trade smarter, and dominate the markets with Market Prime! 🔥'''

# Start Telethon client
client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
     # Wait until the scheduled time
        # Send message
        for destination_channel in target_accounts:
            await client.send_message(destination_channel, account_messages)
  # Prevent double sending

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())
