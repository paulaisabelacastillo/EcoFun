import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv  

load_dotenv()  

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

MEME_FOLDER = './memes_ecologicos'
MEMES = ['meme_1.png', 'meme_2.png']

@bot.event
async def on_ready():
    print(f'✅ EcoBot conectado como {bot.user}')

@bot.command()
async def eco(ctx):
    """Envía uno de los dos memes ecológicos aleatorios"""
    try:
        meme_file = random.choice(MEMES)
        file_path = os.path.join(MEME_FOLDER, meme_file)

        if not os.path.isfile(file_path):
            await ctx.send("⚠️ El archivo del meme no se encontró.")
            return

        file = discord.File(file_path, filename=meme_file)

        embed = discord.Embed(
            title="🌍 ¡Hora de reír y reflexionar!",
            description="Un meme sobre el cambio climático para compartir conciencia 💡",
            color=0x34d399
        )
        embed.set_image(url=f"attachment://{meme_file}")
        embed.set_footer(text="EcoFun • Memes Ecológicos")

        await ctx.send(file=file, embed=embed)

    except Exception as e:
        print(f"❌ Error al enviar el meme: {e}")
        await ctx.send("😢 Ocurrió un error al cargar el meme.")

if __name__ == '__main__':
    TOKEN = ''  # Reemplaza con tu token de bot de Discord
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ Token no encontrado. Usa la variable de entorno DISCORD_BOT_TOKEN.")
