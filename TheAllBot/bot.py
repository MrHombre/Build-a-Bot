import discord
from discord.ext.commands import Bot

from SecretStuff import secrets

RoBoTo = Bot(command_prefix="!")

@RoBoTo.event
async def on_read():
    print("Client logged in")


@RoBoTo.command()
async def hello(*args):
    return await RoBoTo.say("Hello World!")

RoBoTo.run(secrets.BOT_TOKEN)
