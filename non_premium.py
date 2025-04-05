import asyncio
from telethon import TelegramClient, events
from telethon.sync import TelegramClient

api_id = '28178981'
api_hash = '92dac09b406e93e836e8b9b5e6ce5e80'
channel_id = 't.me/jobformyselfonly'  # Premium channel
list_of_accounts =['t.me/DeepakRaghava', 't.me/iamsmk12','t.me/copyofjobupdatesmyself']

client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage(chats=channel_id))
async def copy_to_account(event):
    for account_id in list_of_accounts:
        if event.message.text:  # If it's a text message
            await client.send_message(account_id, event.message.text)
        elif event.message.media:  # If it's an image, video, or other media
            await client.send_file(account_id, event.message.media, caption=event.message.text)

async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())  # Normal execution


