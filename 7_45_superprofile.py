import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

# Define the target channel
account_messages = {'t.me/tradesavvy999':'''📊 Secure short-term equity wins! Finish the week with top-notch insights for quick gains in premium stocks. Fast-track your success! 🏦🎯

✨ Start the weekend on a high note with returns you’ll celebrate !!!

**Join Premium with Launch Offer FLAT 80% OFF + Extra 50%OFF :**
https://superprofile.bio/tradesavyy

Know about our premium @TradeSavvy_bot (Fast replies)

If above is not useful, can message at @tradesavvyyy (24 hours late reply)''', 


't.me/Trade_Proooo':'''📊 Secure short-term equity wins! Finish the week with top-notch insights for quick gains in premium stocks. Fast-track your success! 🏦🎯

✨ Start the weekend on a high note with returns you’ll celebrate !!!

**Join Premium with Offer FLAT 80% OFF:** https://superprofile.bio/tradeprooo

Learn about our premium at @Tradeprooo_bot (Fast replies)

For more questions, you can message us at @TradeProooooo (Slow replies)''', 


't.me/CliffCapital':'''📊 Secure short-term equity wins! Finish the week with top-notch insights for quick gains in premium stocks. Fast-track your success! 🏦🎯

✨ Start the weekend on a high note with returns you’ll celebrate !!!

**Join Premium with Launch Offer FLAT 80% OFF:**
https://superprofile.bio/cliffcapital

Learn about our plans at @Cliff_Capital_premium_bot (Quick replies)

If above is not useful, can connect at @premium20245 (Expect delay in response)''',


't.me/AlphaInvest0':'''📊 Secure short-term equity wins! Finish the week with top-notch insights for quick gains in premium stocks. Fast-track your success! 🏦🎯

✨ Start the weekend on a high note with returns you’ll celebrate !!!

**Join Premium with Launch Offer FLAT 80% OFF:** https://superprofile.bio/alphainvest

Learn about our plans at @Invest_Alpha_Premium_Bot (Fast replies)

For more questions, you can message us at @Investoralph (Response in 24 hours)''',


't.me/FinFlex0':'''📊 Secure short-term equity wins! Finish the week with top-notch insights for quick gains in premium stocks. Fast-track your success! 🏦🎯

✨ Start the weekend on a high note with returns you’ll celebrate !!!

**Join Premium with FLAT 80% OFF:** https://superprofile.bio/finflex

Learn about our premium at @FinFlex_Premium_bot (Fast replies)

For more questions, you can message us at @finflexx (Slow replies)'''}

# Start Telethon client
client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
        now = datetime.now()
        target_time = now.replace(hour=7, minute=56, second=0, microsecond=0)  

        if now > target_time:
            target_time += timedelta(days=1)  

        wait_time = (target_time - now).total_seconds()
        print(f"Waiting for {wait_time} seconds until {target_time}")

        await asyncio.sleep(wait_time)  # Wait until the scheduled time
        # Send message
        for destination_channel, messages in account_messages.items():
            await client.send_message(destination_channel, messages, link_preview=False)

        await asyncio.sleep(65)  # Prevent double sending

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())
