from twitchio.ext import commands
from dotenv import load_dotenv
from os import environ
import subprocess
import random
import os

load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=environ['TWITCH_TOKEN'],
            prefix=environ['TWITCH_PREFIX'],
            initial_channels=[environ['TWITCH_CHANNEL']]
        )

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return

        random.seed(message.author.color)

        cmd_arr = (
            'espeak', '-vbrazil-mbrola-4', message.content,
            '-p', str(random.randint(1, 200)), '-s', str(random.randint(90, 140))
        )
        subprocess.Popen(cmd_arr)

        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()
