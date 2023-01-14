import discord
from discord.ext import commands
import random


grunning=False
p1=""
p2=""
currTurn=0
t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}


def showboard():
  s = "[" + t[1] + "][" + t[2] + "][" + t[3] + "]\n"
  s+= "[" + t[4] + "][" + t[5] + "][" + t[6] + "]\n"
  s+= "[" + t[7] + "][" + t[8] + "][" + t[9] + "]"
  return s


def isempty(index):
  if t[index] == '   ':
    return True
  else:
    return False


def insert(ctx,letter, index):
  if (isempty(index)):
    t[index] = letter
    return True
  return False
    


def win(letter):
  if (t[1] == t[2] and t[1] == t[3] and t[1] == letter):
    return True
  elif (t[4] == t[5] and t[4] == t[6] and t[4] == letter):
    return True
  elif (t[7] == t[8] and t[7] == t[9] and t[7] == letter):
    return True
  elif (t[1] == t[4] and t[1] == t[7] and t[1] == letter):
    return True
  elif (t[2] == t[5] and t[2] == t[8] and t[2] == letter):
    return True
  elif (t[3] == t[6] and t[3] == t[9] and t[3] == letter):
    return True
  elif (t[1] == t[5] and t[5] == t[9] and t[1] == letter):
    return True
  elif (t[3] == t[5] and t[5] == t[7] and t[3] == letter):
    return True
  else:
    return False


def draw():
  for key in t.keys():
    if t[key]=='   ':
      return False
  return True







class TiTaTo(commands.Cog):
  def __init__(self, client):
    self.client=client


  @commands.command()
  async def tictactoe(self,ctx, arg1:discord.Member, arg2:discord.Member):
    global grunning
    global p1
    global p2
    global t
    global currTurn
  
    if not grunning:
      grunning=True
      p1=arg1
      p2=arg2
      t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}
      currTurn=random.randint(1,2)
      await ctx.send(f"<@{p1.id}> You are X\n<@{p2.id}> You are O")
      await ctx.send(showboard())
      if(currTurn==1):
        await ctx.send(f"<@{p1.id}> Play")
      else:
        await ctx.send(f"<@{p2.id}> Play")
        
    else:
      await ctx.send(f"Already <@{p1.id}> and <@{p2.id}> are playing!!")
  
  
      
  @commands.command()
  async def put(self,ctx, pos:int):
      global currTurn
      global p1
      global p2
      global t
      global grunning
  
      if not grunning:
        await ctx.send("No one is playing!!\nStart a game to play")
      else:
        if pos<1 or pos>9:
          await ctx.send("Wrong input, Enter a number between 1 and 9")
          return
        if(currTurn==1 and ctx.author==p2):
          await ctx.send(f"Not your turn <@{p2.id}>!!")
        elif(currTurn==2 and ctx.author==p1):
          await ctx.send(f"Not your turn <@{p1.id}>!!")
        elif(currTurn==1 and ctx.author==p1):
          flag = insert(ctx,'X',pos)
          if flag:
            await ctx.send(showboard())
            if win('X'):
              await ctx.send(f"<@{p1.id}> Won!!")
              t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}
              p1=""
              p2=""
              currTurn=0
              grunning=False
            elif draw():
              await ctx.send(f"Its a draw <@{p1.id}> <@{p2.id}>")
              t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}
              p1=""
              p2=""
              currTurn=0
              grunning=False
            else:
              await ctx.send(f"<@{p2.id}> Play")
              currTurn=2
          else:
            await ctx.send("Wrong input, already occupied!!")
        elif(currTurn==2 and ctx.author==p2):
          flag = insert(ctx,'O',pos)
          if flag:
            await ctx.send(showboard())
            if win('O'):
              await ctx.send(f"<@{p2.id}> Won!!")
              t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}
              p1=""
              p2=""
              currTurn=0
              grunning=False
            elif draw():
              await ctx.send(f"Its a draw <@{p1.id}> <@{p2.id}>")
              t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}
              p1=""
              p2=""
              currTurn=0
              grunning=False
            else:
              await ctx.send(f"<@{p1.id}> Play")
              currTurn=1
          else:
            await ctx.send("Wrong input, already occupied!!")
  
  
  
  @commands.command()
  async def stopTictactoe(self,ctx):
    global currTurn
    global p1
    global p2
    global t
    global grunning
    if grunning:
      await ctx.send(f"Game ended <@{p1.id}> <@{p2.id}>")
      t = {1:'   ', 2:'   ', 3:'   ', 4:'   ', 5:'   ', 6:'   ', 7:'   ', 8:'   ', 9:'   '}
      p1=""
      p2=""
      currTurn=0
      grunning=False
    else:
      await ctx.send("No game running!!")
    
  
  
  @tictactoe.error
  async def tictactoe_error(ctx, error):
      print(error)
      await ctx.send("Please tag Player 1 and Player 2!!")
      # if isinstance(error, commands.MissingRequiredArgument):
      # elif isinstance(error, commands.BadArgument):
      #     await ctx.send("Please tag Player 1 and Player 2!!")
  
  @put.error
  async def place_error(ctx, error):
      if isinstance(error, commands.BadArgument):
          await ctx.send("Please enter a valid position")
      elif isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Please enter a position to put "+ "X" if currTurn==1 else "O")


async def setup(client):
  await client.add_cog(TiTaTo(client))