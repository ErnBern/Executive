import discord
from discord.ext import commands

class Hello_Cmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello Cog is ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        username = str(message.author).split('#')[0]
        if message.author == self.client.user:
            return

        if message.content.startswith('hello') or message.content.startswith('Hello') or message.content.startswith(
                'hi') or message.content.startswith('Hi'):
            username = str(message.author).split('#')[0]
            await message.channel.send(f'Hello, {username}!')


        if message.content.startswith('bye') or message.content.startswith('Bye') or message.content.startswith(
                'goodbye') or message.content.startswith('Goodbye'):
            username = str(message.author).split('#')[0]
            await message.channel.send(f'Goodbye, {username}!')


def setup(client):
    client.add_cog(Hello_Cmds(client))