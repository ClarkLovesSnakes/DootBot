import discord
from discord.ext import commands
import asyncio
import random
import logging

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(intents=intents, command_prefix="")

@bot.event
async def on_message(msg):
    for user in msg.mentions:
        if user.id == 287938558407344129:
            return await msg.add_reaction(random.choice(["⬆️", "⬇️"]))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("-------------------------------------------")


async def main():
    discord.utils.setup_logging(level=logging.INFO, root=False)

    with open("Token.txt", "r", encoding="utf-8") as fp:
        token = fp.read()

    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
