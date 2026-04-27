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
    
    
DNP_ENABLED = True

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.reference:
        try:
            replied_message = await message.channel.fetch_message(message.reference.message_id)
        except:
            return
        
        replied_user = replied_message.author
        role_names = [role.name for role in replied_user.roles]
        
        if "DoNotPing" in role_names and DNP_ENABLED:
            await message.channel.send(
                f"Please do not ping users with the No Ping role!"
            )
    
    await bot.process_commands(message)
    
bot.run(TOKEN)