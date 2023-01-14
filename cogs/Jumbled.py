import discord
from discord.ext import commands
import random
import asyncio

wordslist = []
with open('Words.txt', 'r') as f:
  wordslist = f.readlines()

for i in range(0, len(wordslist)):
  wordslist[i] = wordslist[i][:-1]


def get_word():
  global wordslist
  pos = random.randint(0, len(wordslist) - 1)
  string2= wordslist[pos].split('|')[0]
  string2=string2.lower()
  list_char=[]
  string=""
  for i in range(0,len(string2)):
    list_char.append(string2[i])
    
  
  random.shuffle(list_char)
  for i in list_char:
    string=string+i
  
  if(string==string2):
    string=""
    list2=list(string)
    random.shuffle(list2)
    for i in list2:
      string=string+i
    
    
  l=[string,string2]
  return(l)

  
class Jumbled_word(commands.Cog):
  def __init__(self, client):
    self.client=client

    
  @commands.command()
  async def jumbleMe(self,ctx):
    jumble,ans = get_word()
    await ctx.send(jumble)
      
      
    def check(m):
      return m.author==ctx.author 
    try:
      guess = await self.client.wait_for('message', check=check, timeout=60)
    
        
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you ran out of time!!\nThe correct answer was {ans}')
      
    if (guess.content.lower() == ans):
          await ctx.send('Woohoo, Correct answer')
    else:
          await ctx.send(f'Oops, Incorrect answer\nThe correct answer was {ans}')

        
  
 


    
async def setup(client):
  await client.add_cog(Jumbled_word(client))