import discord
from discord.ext import commands
import string
import random

grunning=False
wordslist = []
with open('Words.txt', 'r') as f:
  wordslist = f.readlines()

for i in range(0, len(wordslist)):
  wordslist[i] = wordslist[i][:-1]


class hang(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def hangman(self, ctx):
    global wordslist
    global grunning
    if not grunning:
      grunning=True
      await ctx.send("Starting...")
  
      pos = random.randint(0, len(wordslist) - 1)
      word = wordslist[pos].split('|')[0]
      hint = wordslist[pos].split('|')[1]
      
      correct_guesses = 0
      misc = 0
  
      word = word.lower()
      word_letters = set(word)
      alphabet = set(string.ascii_lowercase)
      guessed_letters = set()
      word_guessed = set()
      lives = 5
      while lives > 0:
        empty = 0
  
        await ctx.send("Word: " + " ".join(letter if letter in word_guessed else "[]"
                       for letter in word))
        for letter in word:
          if letter in word_guessed:
            empty += 0
          else:
            empty += 1
  
        if empty == 0:
          break
  
        if lives == 5 and correct_guesses == 0 and misc == 0:
          await ctx.send(f"Hint: {hint}")
          await ctx.send(f"Lives: {lives} \n")
  
        def check(m):
          return m.author == ctx.author
  
        user_input = await self.client.wait_for('message', check=check)
        if user_input.content.lower() in guessed_letters:
          await ctx.send("You already guessed that letter, Try again ")
          misc += 1
          continue
  
        elif user_input.content.lower() in alphabet - guessed_letters:
          user_input = user_input.content.lower()
          guessed_letters.add(user_input)
  
        elif user_input.content!="$hangman":
          await ctx.send("Please enter a single letter")
          misc += 1
          continue
  
        if user_input in word_letters:
          correct_guesses += 1
          word_guessed.add(user_input)
          word_letters.discard(user_input)
          await ctx.send("Correct!")
  
        else:
          await ctx.send("Incorrect")
          lives -= 1
  
          if lives == 1:
            await ctx.send("You have " + str(lives) + " life left")
          else:
            await ctx.send("You have " + str(lives) + " lives left")
  
      if lives > 0:
        await ctx.send("Congratulations! You won.\n")
        grunning = False
  
      else:
        await ctx.send(f"Sorry, you lost. The word was {word}.\n")
        grunning = False
    else:
      await ctx.send("Game already running!!")

async def setup(client):
  await client.add_cog(hang(client))
