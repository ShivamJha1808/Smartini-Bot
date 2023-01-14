import discord
from discord.ext import commands
import requests
import json
import asyncio

def get_question(nq=1):
  response = requests.get("https://the-trivia-api.com/api/questions?categories=food_and_drink&limit=9&region=IN&difficulty=medium")
  dict = response.json()
  l = []
  for i in range(0, nq):
    q = "Question:\n " + dict[i]['question'] + "\n"
    ans = dict[i]['correctAnswer']
    ansList = dict[i]['incorrectAnswers']
    ansList.extend([ans])
    ansList.sort()
    id = 1
    rght = 1
    for j in range(0, 4):
      q = q + str(id) + ". " + ansList[j] + "\n"
      if (ansList[j] == ans):
        rght = id
      id += 1
    l.extend([q, rght])

  return l

class Quiz(commands.Cog):
  def __init__(self, client):
    self.client=client

    
  
  @commands.command()
  async def askMe(self,ctx):
    ques=get_question()
    await ctx.send(ques[0])

    def check(m):
      return m.author == ctx.author and m.content.isdigit()

    try:
      guess = await self.client.wait_for('message', check=check, timeout=60)
    except asyncio.TimeoutError:
      return await ctx.send(f"Sorry, you ran out of time!!\nThe correct answer was {ques[1]}")

    if int(guess.content) == ques[1]:
      await ctx.send('Woohoo, Correct answer')
    else:
      await ctx.send(f"Oops, Incorrect answer\nThe correct answer was {ques[1]}")


  
  @commands.command()
  async def rapid(self,ctx):
    score = 0
    nq = 9
    ques = get_question(nq)
    for i in range(0, 2 * nq, 2):
      await ctx.send(ques[i])

      def check(m):
        return m.author == ctx.author and m.content.isdigit()

      try:
        guess = await self.client.wait_for('message', check=check, timeout=15)
      except asyncio.TimeoutError:
        await ctx.send(f'Sorry, you ran out of time!!\nThe correct answer was {ques[i+1]}')
        continue

      if int(guess.content) == ques[i + 1]:
        await ctx.send('Woohoo, Correct answer')
        score += 1
      else:
        await ctx.send(f'Oops, Incorrect answer\nThe correct answer was {ques[i+1]}')

    await ctx.send(f'Your final score is {score}')
  
  


async def setup(client):
  await client.add_cog(Quiz(client))