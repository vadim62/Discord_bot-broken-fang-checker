import os

import discord
import requests
from dotenv import load_dotenv


load_dotenv('.env')

prices = []
different = []

cookie = {
    'steamLoginSecure': os.environ.get('steamLoginSecure')}


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!history'):
            try:
                response = requests.get(
                    'https://steamcommunity.com/market/pricehistory/?currency=5&country=ru&appid=730&market_hash_name=Operation%20Broken%20Fang%20Case', cookies=cookie)
                resp = response.json()['prices']
                prices.append(float("%.2f" % resp[-1][1]))
                prices.append(float("%.2f" % resp[-25][1]))
                prices.append(float("%.2f" % resp[-73][1]))
                prices.append(float("%.2f" % resp[-169][1]))
                for i in range(1, 4):
                    a = prices[i]
                    b = prices[0]
                    if b < a:
                        different.append("%.2f" % ((a - b) / b * 100))
                    else:
                        different.append("%.2f" % ((b - a) / a * 100))
                await message.channel.send(
                    f'Изменение цены: день {different[0]}%, 3 дня {different[1]}%, 7 дней {different[2]}%')
            except:
                await message.channel.send('Я сломался')

        if message.content.startswith('!case'):
            try:
                response = requests.get(
                    'https://steamcommunity.com/market/priceoverview/?currency=5&country=ru&appid=730&market_hash_name=Operation%20Broken%20Fang%20Case')
                res = response.json()['lowest_price']
                await message.channel.send(f'Цена кейса сломанный клык: {res}')
            except:
                await message.channel.send('Я сломался')


client = MyClient()
client.run(os.environ.get('Discord_Token'))
