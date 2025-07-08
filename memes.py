import discord
from discord.ext import commands
import random
import os

# Intents (requerido en la versión moderna de discord.py)
intents = discord.Intents.default()
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)

# Carpeta con memes ecológicos
MEME_FOLDER = './memes_ecologicos'

@bot.event
async def on_ready():
    print(f'EcoBot conectado como {bot.user}')

@bot.command()
async def eco(ctx):
    """Envía un meme ecológico aleatorio"""
    try:
        memes = [f for f in os.listdir(MEME_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not memes:
            await ctx.send("🌱 No hay memes ecológicos disponibles.")
            return

        meme_file = random.choice(memes)
        file_path = os.path.join(MEME_FOLDER, meme_file)
        file = discord.File(file_path, filename=meme_file)

        embed = discord.Embed(
            title="🌍 ¡Hora de reír y reflexionar!",
            description="Un meme sobre el cambio climático para compartir conciencia 💡",
            color=0x34d399  # Verde menta (paleta EcoFun)
        )
        embed.set_image(url=f"attachment://{meme_file}")
        embed.set_footer(text="EcoFun • Memes Ecológicos")

        await ctx.send(file=file, embed=embed)
    except Exception as e:
        await ctx.send("😢 Ocurrió un error al cargar el meme.")
        print(f"Error: {e}")

# Inicia el bot (reemplaza 'TU_TOKEN_AQUI' por el token real)
bot.run('TU_TOKEN_AQUI')
