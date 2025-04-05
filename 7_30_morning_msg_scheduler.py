import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

# Define the target channel
account_messages = {'t.me/tradesavvy999':'''🚀 Welcome, Traders! 🚀

😊 Happy Morning 😊

👉🏻 Before diving into our trading signals, let's ensure we're all on the same page for success:

🔹 Guidelines are Key: Not following our guidelines / Rules may result in 100% financial loss. 

Let's trade smartly!

🔹 Free vs. Premium: Understand the difference:

👉 Free Channel: Insights into our premium calls analysis quality.

👉 Premium: Unlock our strategy toolkit for detailed rules , premium calls and analysis behind each trade.

Don't trade from free channel , you get delayed signals , and the exit and call guidance is only shared in premium.

🔹 Multiply Opportunities:

Free Channel: 1 signal daily.
Premium: 4-5 high-quality signals daily, to diversify and boost potential returns.

🔹 Gain Confidence:

Premium offers in-depth  analysis and data breakdowns.
Understand the "why" behind each signal for informed decisions.

🔹 Maximize Profits:

Exclusive exit strategies in Premium to lock in gains and minimize risk. 

Join our Premium channel and let's embark on this journey to financial success together! 📈 💼 and we are SEBI Reg: INH000015871.''', 


't.me/Trade_Proooo':'''Good Morning, Traders ✔️

Our journey over the last 3 years has led to the development of 3 algorithms ensuring consistent monthly returns. and we are SEBI Reg: INH000015871.

If you don’t follow following you will lose money. Please don’t trade from this free channel. This channel is only to see our quality of analysis. Following are only provided in premium. 

1️⃣ Access to trading rules: Exclusive access to the specific rules and algorithms we utilize for generating trade signals is available only through our premium service. Without these, achieving success is improbable.

2️⃣ Number of signals: Free channel users receive one signal per day. Premium members enjoy 4-5 daily signals.

3️⃣ Signal explanation: We provide a breakdown of the rationale behind each signal, including charts and data, exclusively for premium members.

4️⃣ Exit strategy: While we guide on entry points for free signals, premium members receive guidance on exit strategies as well.''', 


't.me/CliffCapital':'''Good Morning Everyone 🙂

We are coders, who started trading in market 5 years back and we are SEBI Reg: INH000015871. And now we have developed 3 algos, which generate consistent returns every month. We use algos to share signals here.  

If you don’t follow these you will lose money. Please don’t trade from this free channel. This channel is only to see our quality of analysis. Following are only provided in premium. 

✅ Rules required to trade along with our algo only given in premium, without rules and premium support, you will loose money.

✅ Here we share only 1 free signal per day, In premium we share 4-5 signals daily. 

✅ The concept on which some signals given is thoroughly discussed (charts, data etc.) only in premium.

✅ When to exit? Is not given here. Only given in Premium.''',


't.me/AlphaInvest0':'''Good Morning Dear Fellow Traders ✔️

Our last 3 years journey has led to the development of 3 algorithms giving reliable monthly returns, and we are SEBI Reg: INH000015871.

Disregarding these guidelines risks financial loss; refrain from trading in this free channel, which solely showcases our analysis quality of our algorithms. Following is difference between Free vs. Premium:

1️⃣ Access to trading rules: Only our premium service provides the specific rules & algorithms we use for generating trade signals. Without these, success is unlikely.

2️⃣ Number of signals: You get one free signal per day. Premium members receive 4-5 daily signals.

3️⃣ Signal explanation: We break down the rationale behind each signal (charts, data) only for premium members.

4️⃣ Exit strategy: We only guide on entry points for free signals. Premium members receive exit strategy guidance as well.''',


't.me/FinFlex0':'''Good Morning Everyone 🙂

We are coders, who started trading in market 5 years back and we are SEBI Reg: INH000015871. And now we have developed 3 algos, which generate consistent returns every month. We use algos to share signals here.  

If you don’t follow these you will lose money. Please don’t trade from this free channel. This channel is only to see our quality of analysis. Following are only provided in premium. 

✅ Rules required to trade along with our algo only given in premium, without rules and premium support, you will loose money.

✅ Here we share only 1 free signal per day, In premium we share 4-5 signals daily. 

✅ The concept on which some signals given is thoroughly discussed (charts, data etc.) only in premium.

✅ When to exit? Is not given here. Only given in Premium.'''}

# Start Telethon client
client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
        now = datetime.now()
        target_time = now.replace(hour=7, minute=54, second=0, microsecond=0)  # 9:00 AM

        if now > target_time:
            target_time += timedelta(days=1)  # Move to the next day if already past 9 AM

        wait_time = (target_time - now).total_seconds()
        print(f"Waiting for {wait_time} seconds until {target_time}")

        await asyncio.sleep(wait_time)  # Wait until the scheduled time
        # Send message
        for destination_channel, messages in account_messages.items():
            await client.send_message(destination_channel, messages, link_preview=False)

        await asyncio.sleep(60)  # Prevent double sending

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())
