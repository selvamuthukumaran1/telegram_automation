import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

# Define the target channel
account_messages = {'t.me/tradesavvy999':'''**Remaining calls will be given only in premium** 

**Join Premium FLAT 50% OFF before the offer expires :** https://superprofile.bio/tradesavyy

Learn more about our premium at @Tradesavvy_bot (Fast replies)

For more questions, or for guidance joining the premium you can message us at @tradesavvyyy (Slow replies)''', 


't.me/Trade_Proooo':'''**Rest calls will be given only in premium** 

**Join Premium with Offer FLAT 50% OFF:** https://superprofile.bio/tradeprooo

Learn about our premium at @Tradeprooo_bot (Fast replies)

For more questions, you can message us at @TradeProooooo (Slow replies)''', 


't.me/CliffCapital':'''**Rest calls will be given only in premium** 

**Join Premium with Launch Offer FLAT 50% OFF:** https://superprofile.bio/cliffcapital

Learn about our plans at @Cliff_Capital_premium_bot (Quick replies)

If above is not useful, can connect at @premium20245 (Expect delay in response)''',


't.me/AlphaInvest0':'''**Rest signals for the day only in premium**

**Join Premium with FLAT 50% OFF:** https://superprofile.bio/alphainvest

Learn about our plans at @Invest_Alpha_Premium_Bot (Fast replies)

For more questions, you can message us at @Investoralph (Response in 24 hours)''',


't.me/FinFlex0':'''**Remaining signals only in premium** 

**Join Premium with Launch Offer FLAT 50% OFF:** https://superprofile.bio/finflex

Learn about our premium at @FinFlex_Premium_bot (Fast replies)

For more questions, you can message us at @finflexx (Slow replies)'''}

# Start Telethon client
client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
    if datetime.today().weekday() in [5, 6]:
        return
    else:
        now = datetime.now()
        target_time = now.replace(hour=12, minute=0, second=0, microsecond=0)  # 9:00 AM

        if now > target_time:
            target_time += timedelta(days=1)  # Move to the next day if already past 9 AM

        wait_time = (target_time - now).total_seconds()
        print(f"Waiting for {wait_time} seconds until {target_time}")

        await asyncio.sleep(wait_time)  # Wait until the scheduled time
        # Send message
        for destination_channel, messages in account_messages.items():
            await client.send_message(destination_channel, messages, link_preview=False)

        await asyncio.sleep(60)  # Prevent double sending'''

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())
