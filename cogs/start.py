import discord
from discord.ext import commands


class Iniciar(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Entrada de um Membro
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not member.bot:
            with open('bd/AutoBemVindo.txt') as file:
                if f'{member.guild.id}\n' in file:
                    embed_var = discord.Embed(title= 'Welcome!', description= 'Please, enjoy and follow the server rules!\n', color= 0xc1818f)
                    embed_var.set_thumbnail(url= self.client.user.avatar_url)
                    embed_var.set_footer(icon_url= 'https://cdn.discordapp.com/avatars/720686657950711909/6fda15865e1aeed96ee1b3d4e9098391.webp?size=1024', text='Bot by: JotaEspig#4394')
                    await member.send(embed= embed_var)


def setup(client):
    client.add_cog(Iniciar(client))