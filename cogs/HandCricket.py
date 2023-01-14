import discord
from discord.ext import commands
import random
OVERS=0

class HCric(commands.Cog):
  def __init__(self, client):
    self.client=client


  @commands.command()
  async def cricket(self,ctx):
    global OVERS
    OVERS=0
    def check1(m):
      return m.author == ctx.author and m.content.isdigit()
    def check2(m):
      return m.author == ctx.author



    async def battingfirst():
      global OVERS
      await ctx.send("Batting Starts: \nEnter values from 1 to 6.\n")
      balls_played = 0
      score = 0
      while(True):
  
          BOT = random.randint(1,6)
          await ctx.send("Your Batting:")
          M = await self.client.wait_for('message', check=check1)
          MY=int(M.content)
          if MY > 6 or MY < 1:
              await ctx.send("INVALID INPUT.")
              score=score - MY
              balls_played=balls_played - 1
          await ctx.send(f"Bot Bowling: {BOT}")
          score=score + MY
          balls_played=balls_played + 1
  
          if(BOT==MY):
              score=score - MY
              await ctx.send("You are OUT.")
              await ctx.send(f"Score: {score}")
              await ctx.send(f"Balls delivered: {balls_played}")
              break
  
          if balls_played >= 6*OVERS:
              await ctx.send("No balls left.")
              await ctx.send(f"Score: {score}")
              break
  
      await ctx.send(f'The target for BOT is: {score+1}')
      bot_score = 0
      balls_played2=0
      while(True):
  
          BOT = random.randint(1,6)
          await ctx.send("Your Bowling:")
          M = await self.client.wait_for('message', check=check1) 
          MY=int(M.content)
          if MY > 6 or MY < 1:
              await ctx.send("INVALID INPUT.")
              bot_score=bot_score - BOT
              balls_played2=balls_played2 - 1
          await ctx.send(f"Bot Batting: {BOT}")
          bot_score = bot_score + BOT
          balls_played2=balls_played2 + 1
          if(BOT == MY):
              bot_score = bot_score - BOT
              await ctx.send("Bot is OUT.")
              await ctx.send(f"Bot Score: {bot_score}")
              await ctx.send(f"Balls delivered: {balls_played2}")
              if score > bot_score:
                  await ctx.send(f"You won by {(score)-(bot_score)} runs")
                  return
              else:
                  await ctx.send("MATCH DRAWN")
              break
          if bot_score>score:
              await ctx.send(f"Bot Score: {bot_score}")
              await ctx.send("Bot wins. You lose.")
              await ctx.send(f"Balls delivered: {balls_played2}")
              break
          if balls_played2 >= 6*OVERS:
              await ctx.send(f"Bot Score: {bot_score}")
              await ctx.send("No balls left.\n You win. Bot loses.")
              await ctx.send(f"You won by {(score)-(bot_score)} runs")
              break
  
  
    async def bowlingfirst():
        global OVERS
        await ctx.send("Bowling Starts: \nEnter values from 1 to 6.\n")
        bot_score = 0
        balls_played = 0
        while(True):
    
            BOT = random.randint(1,6)
            await ctx.send("Your Bowling:")
            M = await self.client.wait_for('message', check=check1)
            MY=int(M.content)
            if MY > 6 or MY < 1:
                print("INVALID INPUT.")
                bot_score=bot_score - BOT
                balls_played=balls_played - 1
            await ctx.send(f"Bot Batting: {BOT}")
            bot_score = bot_score + BOT
            balls_played=balls_played + 1
    
            if(BOT==MY):
                bot_score = bot_score - BOT
                await ctx.send("Bot is OUT.")
                await ctx.send(f"BOT Score: {bot_score}")
                await ctx.send(f"Balls delivered: {balls_played}")
                break
    
            if balls_played >= 6*OVERS:
                await ctx.send("No balls left.")
                await ctx.send(f"BOT Score: {bot_score}")
                break
    
        await ctx.send(f'Your target is: {bot_score+1}')
        score = 0
        balls_played2=0
        while(True):
    
            BOT = random.randint(1,6)
            await ctx.send("Your Batting: ")
            M = await self.client.wait_for('message', check=check1) 
            MY=int(M.content)
            await ctx.send(f"Bot Bowling: {BOT}")
            if MY > 6 or MY < 1:
                await ctx.send("INVALID INPUT.")
                score = score - MY
                balls_played2=balls_played2 - 1
            score = score + MY
            balls_played2=balls_played2 + 1
            if(BOT == MY):
                score = score - MY
                await ctx.send("You are OUT.")
                await ctx.send(f"Score: {score}")
                await ctx.send(f"Balls delivered: {balls_played2}")
                if bot_score > score:
                    await ctx.send(f"Bot won by {(bot_score)-(score)} runs")
                    return
                else:
                    await ctx.send("MATCH DRAWN")
                break
            if score>bot_score:
                await ctx.send(f"Score: {score}")
                await ctx.send("You win. Bot loses.")
                await ctx.send(f"Balls delivered: {balls_played2}")
                break
            if balls_played2 >= 6*OVERS:
                await ctx.send(f"Score: {score}")
                await ctx.send("No balls left.\n Bot wins. You lose.")
                await ctx.send(f"Bot won by {(bot_score)-(score)} runs")
                break


    
    async def toss():
      global OVERS
      await ctx.send("Enter numbers of overs (upto 5)")
      OV=await self.client.wait_for('message', check=check1)
      OVERS=int(OV.content)
      if OVERS > 5 or OVERS < 1:
          await ctx.send('Invalid input')
          await toss()

      await ctx.send("chose even or odd")
      TO = await self.client.wait_for('message', check=check2)
      TOSS = TO.content
      if TOSS.lower() == 'even':
          await ctx.send("Enter a number between 1 to 6:")
          ch = await self.client.wait_for('message', check=check1)
          choice=int(ch.content)
          if choice > 6 or choice < 1:    
              await ctx.send('Invalid input, game restarts')
              await toss()
          Bot_choice = random.randint(1,6)
          await ctx.send(f"Bot chooses a number: {Bot_choice}")
          await ctx.send(f'Sum of 2 numbers is: {(choice+Bot_choice)}')
          if((choice + Bot_choice)%2)==0:
              await ctx.send('You won the toss. Choose "1" to bat or "2" to bowl.\n1 or 2:')
              MY = await self.client.wait_for('message', check=check1)
              MYCHOICE=MY.content
              if MYCHOICE == '1':
                  await battingfirst()
              elif MYCHOICE == '2':
                  await bowlingfirst()
              else:
                  await ctx.send('Invalid Input, game restarts')
                  await toss()
          else:
              await ctx.send('You lost the toss.')
              BOTCHOICE = random.choice(['1','2'])
              if BOTCHOICE == '1':
                  await ctx.send('Bot chooses to Bat first')
                  await bowlingfirst()
              elif BOTCHOICE == '2':
                  await ctx.send('Bot chooses to Bowl first')
                  await battingfirst()
      elif TOSS.lower() == 'odd':
          await ctx.send("Enter a number between 1 to 6:")
          ch = await self.client.wait_for('message', check=check1)
          choice=int(ch.content)
          if choice > 6 or choice < 1:    
              await ctx.send('Invalid Input, game restarts')
              await toss()
          Bot_choice = random.randint(1,6)
          await ctx.send(f"Bot chooses a number: {Bot_choice}")
          await ctx.send(f'Sum of 2 numbers is: {(choice+Bot_choice)}')
          if((choice + Bot_choice)%2)!=0:
              await ctx.send('You won the toss.\n Choose "1" to bat or "2" to bowl.\n1 or 2: ')
              MY = await self.client.wait_for('message', check=check1)
              MYCHOICE=MY.content
              if MYCHOICE == '1':
                  await battingfirst()
              elif MYCHOICE == '2':
                  await bowlingfirst()
              else:
                  await ctx.send('Invalid input, game restarts')
                  await toss()
          else:
              await ctx.send('You lost the toss.')
              BOTCHOICE = random.choice(['1','2'])
              if BOTCHOICE == '1':
                  await ctx.send('Bot chooses to Bat first')
                  await bowlingfirst()
              else:
                  await ctx.send('Bot chooses to Bowl first')
                  await battingfirst()
      else:
          await ctx.send("Invalid input, game restarts")
          await toss()

    await toss()
    

async def setup(client):
  await client.add_cog(HCric(client))