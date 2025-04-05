import asyncio
from telethon.sync import TelegramClient
from datetime import datetime, timedelta


api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

client = TelegramClient("session_name", api_id, api_hash)

accounts_messages = {
    't.me/+M4WgsaOvIYExMWE1':'''Hope all booked profits in today's calls , please send your profit screenshots @tony00071''',
    't.me/+rD5KolqapallNmRl':'''Those who booked good profits avoid over trading 

Please share your profits screenshots @premium20245'''}

async def send_scheduled_message():
        now = datetime.now()
        target = now.replace(hour=15, minute=27, second=0, microsecond=0)

        if now > target:
            target += timedelta(days=1)
    
        wait_time = (target - now).total_seconds()
        print(f'Waiting for {wait_time} seconds until {target}')

        await asyncio.sleep(wait_time)

        for accounts, messages in accounts_messages.items():
              await client.send_message(accounts, messages, link_preview=False)

        await asyncio.sleep(65)

with client:
      client.loop.run_until_complete(send_scheduled_message())  

