import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot()

@bot.event
async def on_message(message):
    for user in message.mentions:
        if user.id == 287938558407344129:
            await message.add_reaction(random.choice(["\U00002B06", "\U00002B07"]))


async def main():

    # Get the token out of the secret token doc
    with open("Token.txt", "r", encoding="utf-8") as tokenDoc:
        TOKEN = tokenDoc.readline()


    await bot.start(TOKEN)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
