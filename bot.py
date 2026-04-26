import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv("token.env")

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello")
    
bot.run(TOKEN)