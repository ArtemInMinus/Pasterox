import discord, random

from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    forty = random.randint(0, 2)
    author = message.author
    if message.author == client.user:
        return
    if message.content.startswith('Привет'):
        await message.channel.send("Дарова брат!")
    elif message.content.startswith('Бот'):
        await message.channel.send(":clown:")
    elif message.content.startswith('!Когда ты родился'):
        await message.channel.send(bot_info("DOB"))
    elif message.content == 'пон':
        await message.channel.send(str(author) + " непон")
    elif message.content == 'Краш':
        await message.channel.send(":hot_face:")
    elif message.content == 'smile':
        await message.channel.send(gen_emodji())
    elif message.content.startswith('Пока'):
        await message.channel.send(":saluting_face:")
    elif forty == 0:
        await message.channel.send(":skull:")
    elif forty == 1:
        pass
    else:
        await message.channel.send(message.content + "чо")



client.run("токен")
