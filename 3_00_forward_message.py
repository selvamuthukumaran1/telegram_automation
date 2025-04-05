import asyncio
from telethon.sync import TelegramClient, events
from datetime import datetime, timedelta

api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

source_channel = "t.me/MarketPrimeDaily"
target_channel = ["Trade_Proooo", "CliffCapital", "AlphaInvest0", "tradesavvy999","FinFlex0", "t.me/+M4WgsaOvIYExMWE1","t.me/+rD5KolqapallNmRl","t.me/+H-YpbIqETXEyYTc1"]

client = TelegramClient("session_name",api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    try:
        
        for accounts in target_channel:
            await client.forward_messages(accounts, event.message)

    except Exception as e:
        print(f'An error occured : {e}')

print("Bot is running.....")
with client:
    client.run_until_disconnected()