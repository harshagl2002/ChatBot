from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea", help="gets ideas for side projects")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should")
    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)}'
    await ctx.send(idea)

@bot.command(name="calc", help="Performs calculations based on following operations: +-*/**")
async def calc(ctx, x, fcn, y):
    x = float(x)
    y = float(y)
    if fcn == '+':
       await ctx.send(x + y)
    elif fcn == '-':
        await ctx.send(x - y)
    elif fcn == '*':
       await ctx.send(x * y)
    elif fcn == '/':
       await ctx.send(x / y)
    elif fcn ==  '**':
        await ctx.send(x ** y)
    else:
        await ctx.send("We only support 4 functional operators")


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token File Read")
    bot.run(TOKEN)