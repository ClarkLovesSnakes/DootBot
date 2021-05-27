import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix = "?")

@bot.event
async def on_message(message):

    reply = ""

    for user in message.mentions:
        if user.id == 287938558407344129:

            if "gone" in message.content.lower() or message.content == "https://www.youtube.com/watch?v=LDU_Txk06tM":
                reply = "\U0001F980"

            else:
                reactions = ["\U00002B06", "\U00002B07"]

                reply = reactions[random.randint(0, 1)]
        
            await message.add_reaction(reply)


@bot.command()
async def quit(ctx):
    """quit() takes no arguments, returns nothing, and simply closes the bot, as well as ending relevant processes"""

    print("test")
    await ctx.send("Logging Off!")
    await bot.close()
    loop.stop()
    print("test")
    return


@bot.event
async def on_ready():

    print("Bot is logged in as {0.user}".format(bot))
    print("All systems are online. Awaiting orders.")


async def main():

    # Get the token out of the secret token doc
    with open("Token.txt", "r", encoding="utf-8") as tokenDoc:
        TOKEN = tokenDoc.readline()


    await bot.start(TOKEN)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
