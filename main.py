import discord
import typing
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

bad_words = ["estupido", "imbecil", "idiota"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} caracteres: {arguments}')

@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="agua"):
    await ctx.send(f'{amount} botellas de {liquid} en el muro!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(bad_word in message.content.lower() for bad_word in bad_words):
        await message.channel.send(f'{message.author.mention}, por favor, evita usar mal vocabulario.')
