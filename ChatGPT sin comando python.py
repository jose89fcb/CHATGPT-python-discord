import discord
from discord.ext import commands
import openai

openai.api_key = "XXx" #API KEY https://platform.openai.com/account/api-keys
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Obtener el canal específico por su ID
    channel = bot.get_channel(1112178231437709402) #Aqui el id del canal de discord
    if channel:
        await channel.send("¡Bot conectado y listo para responder!")

@bot.event
async def on_message(message):
    if message.channel.id == 1112178231437709402: #Aqui el id del canal de discord
        if message.author == bot.user:
            return

        prompt = f"You: {message.content}\nBot:"

        # Mostrar estado "escribiendo"
        async with message.channel.typing():
            # Procesar la respuesta
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=50,
                temperature=0.7,
                n=1,
                stop=None,
            )

        # Obtener respuesta y enviarla al canal de Discord
        answer = response.choices[0].text.strip()
        await message.channel.send(answer)

    await bot.process_commands(message)

bot.run('Xxx') #TOKEN BOT https://discord.com/developers/applications