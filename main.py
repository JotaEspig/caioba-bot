import discord
from discord.ext import commands, tasks
import datetime
from itertools import cycle
import os
import json
from discord.ext.commands import MissingPermissions


#Token e prefixo
with open('TOKEN.txt') as file:
    TOKEN = file.readline().strip('\n')
    PREFIX = file.readline()


#Cria bot com prefixo e remove o comando help padrão
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix= PREFIX, intents= intents)
client.remove_command('help')


#BOT DISCORD
#Comandos que são executados quando o Bot iniciar
@client.event
async def on_ready():
    status = cycle(['cb!help', f'on {len(client.guilds)} servers'])

    change_status.start(status)  
    memes_loop.start()
    dankmemes_loop.start()
    update_json_loop.start()

    print("#==========  BOT ONLINE  ==========#\n")
    print(f'BOT:        {client.user.name}')
    print(f'ID:         {client.user.id}\n')
    print(f'Online on:  {len(client.guilds)} servers\n')
    print(f'Version:     BETA 1.1.7\n')
    print('#==========  BOT ONLINE  ==========#')
#<--==--==--==-->#

#Mudança de Status
@tasks.loop(seconds= 30)
async def change_status(status):
    await client.change_presence(activity= discord.Game(next(status)))

#Auto Meme
@tasks.loop(minutes= 60)
async def memes_loop():
    if (datetime.datetime.utcnow().hour) % 6 == 0:
        from cogs.reddit import Reddit

        #PEGA UM CANAL DE UM SERVIDOR DO BANCO DE DADOS PARA MANDAR X
        servers = []
        file = open('bd/AutoMemes.txt', 'r')
        for line in file:
            servers.append(line)
        file.close()

        for server in servers:
            id_channel = int(server.strip('\n'))
            channel = client.get_channel(id= id_channel)

        #<------------------------><------------------------># 
            if channel != None:
                await Reddit.search_reddit(channel, 'memes', True)

#AutoDankMemes
@tasks.loop(minutes= 60)
async def dankmemes_loop():
    if (datetime.datetime.utcnow().hour) % 6 == 0:
        from cogs.reddit import Reddit

        #PEGA UM CANAL DE UM SERVIDOR DO BANCO DE DADOS PARA MANDAR X
        servers = []
        file = open('bd/AutoDankMemes.txt', 'r')
        for line in file:
            servers.append(line)
        file.close()

        for server in servers:
            id_channel = int(server.strip('\n'))
            channel = client.get_channel(id= id_channel)

        #<------------------------><------------------------># 
            if channel != None:
                await Reddit.search_reddit(channel, 'dankmemes', True)

#Update users.json
@tasks.loop(minutes= 60)
async def update_json_loop():
    if datetime.datetime.utcnow().hour == 0:
        from cogs.profile import Profile
        with open('bd/users.json') as file:
            users = json.loads(file.read())

        for user in users.keys():
            user_obj = client.get_user(id= int(user))
            await Profile.update_json(user_obj)
#<--==--==--==-->#

#Load Cog
@client.command(aliases= ['LOAD'])
async def load(ctx, extension: str):
    if ctx.author.id == 720686657950711909:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'\"{extension}\" loaded')

#Unload Cog
@client.command(aliases= ['UNLOAD'])
async def unload(ctx, extension: str):
    if ctx.author.id == 720686657950711909:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'\"{extension}\" unloaded')

#Reload Cog
@client.command(aliases= ['RELOAD'])
async def reload(ctx, extension: str):
    if ctx.author.id == 720686657950711909:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'\"{extension}\" reloaded')

#Load em todos automaticamente
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Erros
@client.event
async def on_command_error(ctx, erro):
    if isinstance(erro, MissingPermissions):
        await ctx.send(f':hand_splayed: You are not allowed to use this command\n:hand_splayed: {erro}')
    else:
        member = ctx.author
        await member.send(erro)

#Iniciar Bot
client.run(TOKEN)