import asyncio
from datetime import datetime, timedelta
from telethon.sync import TelegramClient

# Your API credentials
api_id = "27647645"
api_hash = "2cdcf90271ae9b647a9561f5f2b0aade"

account_messages = {'t.me/+M4WgsaOvIYExMWE1':'''<b><u>Must Read before trading:</u>
Index Futures & Options: If you don't follow these, you will loose 100% money. Following guidelines are made from 5 years of experience in Trading by considering all ups & downs in market</b>

<u><i>Basic rules to be followed always for Intraday Options</i></u>

✅ Less than 20% of my Portfolio is in Index Options, It comes with very high volatility. 

✅ If safe exit given, never enter the trade again

✅ Never average your loss position. If SL hit, book loss and move to next trade.

✅ Every single call will go up for 5%, we dont give calls with less than 5% upside. so for trading safe, just keep 5% upside on all calls and trade 🙂

✅ For index options, can take nifty 2 lots, bank nifty 4 lots. For Stock Options, Can take 1 lot.

✅ Million is not made in 1 day, it over time, but a million can be lost in a single hour in market 

✅ Its okay to miss jackpot, keep emotions aside, if you wanna build wealth. Get emotional, if you wanna loose capital

✅ Options are high risk in nature. Don't hold any option more than 5 trading days and safe traders can avoid holding over weekend.

✅ When we say - Safe Trader please book now. Please book, it means direction of stock is not clear further as per technical analysis.

Risk Management for beginners for Intraday Options :

✅ <u>There are 3 type of calls.</u> 

1. <b>Medium Risk</b> - Calls with current price given to enter, ex: Nifty 18000 ce 35, 

2. <b>Low Risk</b> - Another type will be Nifty 18000 ce ABOVE 35. 

3. <b>High Risk</b> - Hero Zero Calls 

First format is given when the momentum is already started, In this case enter the trade if current market price when you checked is lower than first 2 targets (Nifty 10 points, BankNifty 20 points) of given price in the channel . If it is above wait for the re-entry

Second format - ABOVE level is given in case the stock is showing momentum but it will go big once it crosses the above level, in this case, never enter below the price, always enter above the price level given. Entering below will lead to 90% chance of loss. 

Hero Zero Calls - Mainly given on expiry, so it comes with high risk. If it goes to Zero, you will loose all your capital, so always play safe on this. Keep trailing profits and book sooner.

<b><u>When to book profits & how to maximize profits in this channel for Intraday Options :</u></b>

✅ If you are a new trader to this premium channel, always follow SL strictly and follow 5% upside as traget for initial 1 month 

✅ As you get comfortable on the format, start trailing profits further from 5%, Once 5% upside is done, move your SL to +5% to protect profits and start moving 10% more for every 10% upside movement. ex: 20%  upside done, move SL from 5% to 15% and so on.
——————————————————————————
<u><i>Basic rules to be followed always for Futures along with above rules</i></u>

✅ Always have Floating capital of 5 lakhs to suffice the margin.

✅ Always with 5% SL or the given SL, Target can be 1%  or High of next day. 

✅ There will be min 2 targets given, Safe traders can stick to target 1 or next one as per their risk capacity If safe exit given, never enter the trade again

✅ If you are not able exit any stock for any reason, don't worry. We recommend momentum stocks, which are trying to go up, so with in next 5 days, you can sell

Risk Management for beginners for Futures along with above rules:

✅ For first 1 month, Risk reward: 1:1 ratio, trade & book profits at one target 1 and strictly hold with SL given or a lower SL,  For 2nd month, Risk reward: 1:2 ratio, For 3rd month, Risk reward: 1:3 ratio..

——————————————————————————

<u><i>Basic rules to be followed always for Positional Options along with above rules</i></u>

✅ Less than 10% of my Portfolio is in 2X F&O Positional, It comes with very high risk & high rewards. 

✅ Every single call will go up for 20%, we dont give calls with less than 5% upside. so for trading safe, just keep 20% upside on all calls and trade 🙂''', 


't.me/+rD5KolqapallNmRl':'''<b><u>Must Read before trading</u>
Stock Futures & Options: If you don't follow these, you will loose 100% money. Following guidelines are made from 5 years of experience in Trading by considering all ups & downs in market</b>

Basic rules to be followed always for Stock Options

✅ Less than 20% of my Portfolio is in Stock Options, It comes with very high volatility. 

✅ If safe exit given, never enter the trade again

✅ Every single call will go up for 5%, we dont give calls with less than 5% upside. so for trading safe, just keep 5% upside on all calls and trade 🙂

✅ Never average your loss position. If SL hit, book loss and move to next trade.

✅ For index options, can take nifty 2 lots, bank nifty 4 lots. For Stock Options, Can take 1 lot.

✅ Million is not made in 1 day, it over time, but a million can be lost in a single hour in market 

✅ Its okay to miss jackpot, keep emotions aside, if you wanna build wealth. Get emotional, if you wanna loose capital

✅ Options are high risk in nature. Don't hold any option more than 5 trading days and safe traders can avoid holding over weekend.

✅ When we say - Safe Trader please book now. Please book, it means direction of stock is not clear further as per technical analysis.

Risk Management for beginners for Stock Options:

✅ There are 3 type of calls. 

1. Medium Risk - Calls with current price given to enter, ex: Relaince 2000 ce 35, 

2. Low Risk - Another type will be Relaince 2000 ce ABOVE 35. 

3. High Risk - Hero Zero Calls 

First format is given when the momentum is already started, In this case enter the trade if current market price when you checked is lower than first 2 targets of given price in the channel . If it is above wait for the re-entry

Second format - ABOVE level is given in case the stock is showing momentum but it will go big once it crosses the above level, in this case, never enter below the price, always enter above the price level given. Entering below will lead to 90% chance of loss. 

Hero Zero Calls - Mainly given on expiry, so it comes with high risk. If it goes to Zero, you will loose all your capital, so always play safe on this. Keep trailing profits and book sooner.

When to book profits & how to maximize profits in this channel for Stock Options:

✅ If you are a new trader to this premium channel, always follow SL strictly and follow 5% upside as traget for initial 1 month 

✅ As you get comfortable on the format, start trailing profits further from 5%, Once 5% upside is done, move your SL to +5% to protect profits and start moving 10% more for every 10% upside movement. ex: 20%  upside done, move SL from 5% to 15% and so on.
——————————————————————————
Basic rules to be followed always for Futures along with above rules

✅ Always have Floating capital of 5 lakhs to suffice the margin.

✅ Always with 5% SL or the given SL, Target can be 1%  or High of next day. 

✅ There will be min 2 targets given, Safe traders can stick to target 1 or next one as per their risk capacity If safe exit given, never enter the trade again

✅ If you are not able exit any stock for any reason, don't worry. We recommend momentum stocks, which are trying to go up, so with in next 5 days, you can sell

Risk Management for beginners for Futures along with above rules:

✅ For first 1 month, Risk reward: 1:1 ratio, trade & book profits at one target 1 and strictly hold with SL given or a lower SL,  For 2nd month, Risk reward: 1:2 ratio, For 3rd month, Risk reward: 1:3 ratio..
——————————————————————————
Basic rules to be followed always for Positional Options along with above rules

✅ Less than 10% of my Portfolio is in 2X F&O Positional, It comes with very high risk & high rewards. 

✅ Every single call will go up for 20%, we dont give calls with less than 5% upside. so for trading safe, just keep 20% upside on all calls and trade 🙂

<b><u>Must Read before trading</u></b>''', 


't.me/+H-YpbIqETXEyYTc1':'''<b><u>Must Read before trading :</u></b> 
Equity BTST, Intraday & Short Term: If you don't follow these, you will loose 100% money. Following guidelines are made from 5 years of experience in Trading by considering all ups & downs in market

Basic rules to be followed always in BTST/Intraday

✅ Always with 2% SL or the given SL, Target can be 1%  or High of next day. We Invest 50K in each stock.(You can invest as low as 5K)

✅ Every single call will go up for 1%, we dont give calls with less than 1% upside. so for trading safe, just keep 1% upside on all calls and trade 🙂

✅ There will be min 2 targets given, Safe traders can stick to target 1 or next one as per their risk capacity If safe exit given, never enter the trade again

✅ Recommended lot for every BTST is 50K, you can plan to invest less or more as per your capital

✅ If safe exit given, never enter the trade again

✅ Never average your loss position. If SL hit, book loss and move to next trade.

✅ If you are not able exit any stock for any reason, don't worry. We recommend momentum stocks, which are trying to go up, so with in next 5 days, you can sell

✅ Million is not made in 1 day, it over time, but a million can be lost in a single hour in market 

✅ Its okay to miss jackpot, keep emotions aside, if you wanna build wealth. Get emotional, if you wanna loose capital

✅ When we say - Safe Trader please book now. Please book, it means direction of stock is not clear further as per technical analysis.

✅ For tips on how to do position sizing of the stocks you buy, please checked the pinned messages.

✅ All the stoploss given here are based on Closing Basis ( Please refer to the pinned messages to know what is "Stoploss on Closing Basis" mean ).

For Short Term:

✅ We invest 50K in each stock (You can invest as low as 5K). We hold 100+ stocks at one moment. 80% of our portfolio is in Short-term/Swing trading.

✅ Only recommended when there is momentum, Avg holding period of these stocks are 40 trading days. (Last 6 M data)

✅ We never booked loss in short-term trades. SL are only for safe traders, we hold them. ~3% of these stocks has holding period of 120 days

Risk Management for beginners:

✅ For first 1 month, Risk reward: 1:1 ratio, trade & book profits at 1% from CMP and strictly hold with SL given or a lower SL

✅ For 2nd month, Risk reward: 1:2 ratio, trade & book profits at 2% from CMP and strictly hold with SL given or a lower SL

✅ For 3rd month, Risk reward: 1:3 ratio, trade & book profits at 3% from CMP and strictly hold with SL given or a lower SL and slowly go on as you get comfortable.

<b><u>Must Read before trading</u></b> ✅'''

}

client = TelegramClient("session_name", api_id, api_hash)

async def send_scheduled_message():
        now = datetime.now()
        target_time = now.replace(hour=8, minute=45, second=0, microsecond=0)  # 9:00 AM

        if now > target_time:
            target_time += timedelta(days=1)  # Move to the next day if already past 9 AM

        wait_time = (target_time - now).total_seconds()
        print(f"Waiting for {wait_time} seconds until {target_time}")

        await asyncio.sleep(wait_time)  # Wait until the scheduled time
        # Send message
        for destination_channel, messages in account_messages.items():
            await client.send_message(destination_channel, messages, link_preview=False, parse_mode='html')

        await asyncio.sleep(65)  # Prevent double sending

# Run the script
with client:
    client.loop.run_until_complete(send_scheduled_message())