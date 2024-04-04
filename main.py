from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands
from random import randint
from slots import play_slots
import asyncio 
from discord.ext.commands import Context

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='pong')
async def ping(ctx):
    await ctx.send('Ping!')
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello there!')
@bot.command(name='roll_dice')
async def roll_dice(ctx):
    await ctx.send(f'You rolled: {randint(1, 6)}')
@bot.command(name='slots')
async def slots(ctx):
    await ctx.send(play_slots())
@bot.command(name='zoom')
async def zoom(ctx):
    await ctx.send('https://ucsd.zoom.us/j/97779724320')

@bot.command(name='whisper')
async def whisper(ctx, *, message: str = "This is a secret message..."):
    try:
        await ctx.author.send(message)
        await ctx.message.add_reaction("✉️")  
    except Exception as e:
        print(f"Error sending DM: {e}")
        await ctx.send(f"Couldn't send a whisper to you. Do you have DMs disabled for non-friends?")

@bot.command(name='trivia')
async def trivia(ctx: Context):
    await ctx.send('What is the capital of France?')

    def check(m):
        return m.channel == ctx.channel and not m.author.bot

    try:
        while True:
            msg = await bot.wait_for('message', check=check, timeout=30.0)  # Wait for a message for 30 seconds
            if msg.content.lower() == 'paris':
                await ctx.send('Correct!')
                break  # Exit the loop if the answer is correct
            else:
                await ctx.send('Incorrect, try again!')

    except asyncio.TimeoutError:
        await ctx.send('Sorry, time is up! The correct answer was Paris.')

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
