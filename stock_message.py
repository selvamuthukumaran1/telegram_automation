import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

message ='''Buy BSE 24 APR 2025 CE 5600 Above 270
Target 5%.......340
SL 240'''

# Define the target channel
account_messages = {'t.me/tradesavvy999':'''**Stocks F&O Premium [Intraday] Analysis :**

Exit signals will be given only given in premium, More calls only in premium. Join Premium :
https://superprofile.bio/tradesavyy \n\n''' + message, 


't.me/Trade_Proooo':'''**Stock F&O [ Intraday ] Premium Analysis**

Exit signals will be given in premium, More calls only in premium. Join Premium: https://superprofile.bio/tradeprooo \n\n''' + message, 


't.me/CliffCapital':'''**Stocks F&O [ Intraday ] Premium Analysis :**

Exit signals will be given in premium, More calls only in premium. Join Premium : https://superprofile.bio/cliffcapital \n\n''' + message,


't.me/AlphaInvest0':'''**Stocks F&O [Intraday ] Premium Analysis**

Exit given in premium, More singals only in premium. Join Premium : https://superprofile.bio/alphainvest \n\n''' + message,


't.me/FinFlex0':'''**Stocks F&O Premium [ Intraday ] Analysis**

Exit & support only given in premium, More calls only in premium. Join Premium : https://superprofile.bio/finflex \n\n''' + message}

# Start Telethon client
client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
    for destination_channel, messages in account_messages.items():
        await client.send_message(destination_channel, messages, link_preview=False)

# Prevent double sending

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())
