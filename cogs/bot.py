import discord
from discord.ext import commands


class Bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Adicionar gif num roleplay
    @commands.command(aliases= ['ADD_GIF'])
    async def add_gif(self, ctx, filename: str, url: str):
        if ctx.author.id == 720686657950711909:
            file = open(f'roleplay/{filename}.txt')
            if f'{url}\n' in file:
                file.close()
                await ctx.send(f'Esse GIF já existe no arquivo {filename}')
            elif not url.endswith('.gif'):
                await ctx.send('Isso não é um link de um GIF, por favor tente novamente')
            else:
                with open(f'roleplay/{filename}.txt', 'a') as file:
                    file.write(f'{url}\n')
                    await ctx.send('GIF adicionado com sucesso')
        else:
            ctx.author.send('Command "add_gif" is not found')

    #Remover gif num roleplay
    @commands.command(aliases= ['RM_GIF'])
    async def rm_gif(self, ctx, filename: str, url: str):
        if ctx.author.id == 720686657950711909:
            with open(f'roleplay/{filename}.txt', 'r') as file:
                lines = file.readlines()
            with open(f'roleplay/{filename}.txt', 'w') as file:
                for line in lines:
                    if line.strip("\n") != f'{url}':
                        file.write(line)
            await ctx.send('GIF removido com sucesso')
        else:
            ctx.author.send('Command "add_gif" is not found')


def setup(client):
    client.add_cog(Bot(client))
