import asyncio
from telethon import TelegramClient, events

api_id = 27647645
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

source_channel = "FinFlex0"  # Try using a username first
target_accounts = ["Trade_Proooo", "CliffCapital", "AlphaInvest0", "tradesavvy999"]

client = TelegramClient("session_name", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def copy_to_account(event):
    print(f"📩 New message detected in {source_channel}: {event.message.text or '[MEDIA]'}")

    for account in target_accounts:
        try:
            if event.message.text:
                await client.send_message(account, event.message.text)
            elif event.message.media:
                await client.send_file(account, event.message.media, caption=event.message.text)
            print(f"✅ Message forwarded to {account}")
        except Exception as e:
            print(f"❌ Error sending to {account}: {e}")

async def main():
    await client.start()
    print("🚀 Bot is running...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
