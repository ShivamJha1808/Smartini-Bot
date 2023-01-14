import discord
from discord.ext import commands
import os
import asyncio

intent = discord.Intents().all()
client = commands.Bot(command_prefix="$", intents=intent)


@client.event
async def on_ready():

  print('We are logged in as {0.user}'.format(client))


async def main():
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      await client.load_extension(f'cogs.{file[:-3]}')
  return


asyncio.run(main())
client.run("MTA2MjY1MjA5MjA1OTIyMjA3Ng.GkFVSZ.vwcSwWczAor5vOMmfWX2XB45Y2Hgp9Sj20b8Rk")