import random

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content[:10] == '마법의 소라고동님 ':
            await message.channel.send(random.choice(["True", "False"]))


client = MyClient()
client.run('ODIwMzU5OTAyNjk3NDg4NDA0.YE0Bsg.TG3IWXDZL4hJORnfI8lCSGeM99w')
