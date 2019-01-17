import discord
from discord.ext import commands
import random
import datetime
import asyncio

client = discord.Client()

timeout = 60 * random.randint(30,60)  # 5 minutes

messeges = ['Ktoś, coś?',
            'It\'s snuff time!',
            'Góra panowie',
            'https://i.pinimg.com/originals/88/e4/b2/88e4b2efc3c8f2f1740049c749977fa2.jpg',\
            'https://i.gifer.com/24CD.gif',
            'https://youtu.be/Y-Hv4GvvHkQ?t=50',
            'Sypniem?',
            'Wysypało mi się coś',
            'Jest {}:{}, wiecie co to oznacza?'.format(datetime.datetime.now().hour,datetime.datetime.now().minute)
            ]

async def my_background_task():
    await client.wait_until_ready()

    channel = discord.Object(id='407965766772719618')

    while True:
        if 16 < datetime.datetime.now().hour or datetime.datetime.now().hour < 2:
            await client.send_message(channel, random.choice(messeges))
            await asyncio.sleep(timeout)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.loop.create_task(my_background_task())
client.run('NTM1MTE2NDQ3ODIzOTUzOTMx.DyDmoA.QPfv7qUJ_WM9JyE-UVJxXDTFeXU')