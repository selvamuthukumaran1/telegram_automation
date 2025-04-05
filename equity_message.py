import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

message ='''Short Term

Buy PNBHOUSING Above 949
Target 5%.............1020
SL 900'''

# Define the target channel
account_messages = {'t.me/tradesavvy999':'''**Equity Premium Analysis**

Exit signals will be given in premium only. Join Premium for more calls  :
https://superprofile.bio/tradesavyy \n\n''' + message, 


't.me/Trade_Proooo':'''**Equity Premium Analysis**

Exit signals will be given in premium, More calls only in premium. Join Premium: https://superprofile.bio/tradeprooo \n\n''' + message, 


't.me/CliffCapital':'''**Equity Premium Analysis**

Exit signals will be given in premium, More calls only in premium. Join Premium : https://superprofile.bio/cliffcapital \n\n''' + message,


't.me/AlphaInvest0':'''**Equity Premium Analysis**

Exit given in premium, More singals only in premium. Join Premium : https://superprofile.bio/alphainvest \n\n''' + message,


't.me/FinFlex0':'''**Equity Premium Analysis :**

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
