import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Auto(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Cadastro AutoMemes
    @commands.command(aliases= ['AUTOMEMES'])
    @commands.has_permissions(administrator= True)
    async def automemes(self, ctx, name_channel: str):
        channel = discord.utils.get(ctx.message.guild.channels, name=name_channel)

        if channel == None:
            await ctx.send(f':hand_splayed:The channel \"{name_channel}\" doesn\'t exist')
        file = open('bd/AutoMemes.txt')
        
        if f'{channel.id}\n' in file:
            file.close()
            with open('bd/AutoMemes.txt', 'r') as file:
                lines = file.readlines()
            with open('bd/AutoMemes.txt', 'w') as file:
                for line in lines:
                    if line.strip("\n") != f'{channel.id}':
                        file.write(line)
            await ctx.send(f'AutoMemes was disabled on the channel: \"{name_channel}\"')
        else:
            file.close()

            with open('bd/AutoMemes.txt', 'a') as file:
                file.write(f'{channel.id}\n')
            embed_var = discord.Embed(title= 'AutoMemes enabled', color= 0xc1818f)
            embed_var.add_field(name= f'AutoMemes was enabled on "{name_channel}"', value= 'To disable, use the same command')
            embed_var.set_thumbnail(url= self.client.user.avatar_url)
            embed_var.set_footer(icon_url= ctx.author.avatar_url, text= f'Requested by: {ctx.author}')
            await ctx.send(embed= embed_var)

    #Cadastro AutoDankMemes
    @commands.command(aliases= ['AUTODANKMEMES'])
    @commands.has_permissions(administrator= True)
    async def autodankmemes(self, ctx, name_channel: str):
        channel = discord.utils.get(ctx.message.guild.channels, name=name_channel)

        if channel == None:
            await ctx.send(f':hand_splayed:The channel \"{name_channel}\" doesn\'t exist')
        file = open('bd/AutoDankMemes.txt')

        if f'{channel.id}\n' in file:
            file.close()
            with open('bd/AutoDankMemes.txt', 'r') as file:
                lines = file.readlines()
            with open('bd/AutoDankMemes.txt', 'w') as file:
                for line in lines:
                    if line.strip("\n") != f'{channel.id}':
                        file.write(line)
            await ctx.send(f'AutoDankMemes was disabled on the channel: \"{name_channel}\"')

        else:
            file.close()
            
            with open('bd/AutoDankMemes.txt', 'a') as file:
                file.write(f'{channel.id}\n')
            embed_var = discord.Embed(title= 'AutoDankMemes enabled', color= 0xc1818f)
            embed_var.add_field(name= f'AutoDankMemes was enabled on the channel "{name_channel}"', value= 'To disable, use the same command')
            embed_var.set_thumbnail(url= self.client.user.avatar_url)
            embed_var.set_footer(icon_url= ctx.author.avatar_url, text= f'Requested by: {ctx.author}')
            await ctx.send(embed= embed_var)

    #Cadastro AutoWelcome
    @commands.command(aliases= ['AUTOWELCOME'])
    @commands.has_permissions(administrator= True)
    async def autowelcome(self, ctx):
        guild = ctx.guild
        
        file = open('bd/AutoWelcome.txt')
        if f'{guild.id}\n' in file:
            file.close()
            with open('bd/AutoWelcome.txt', 'r') as file:
                lines = file.readlines()
            with open('bd/AutoWelcome.txt', 'w') as file:
                for line in lines:
                    if line.strip("\n") != f'{guild.id}':
                        file.write(line)

            await ctx.send('AutoWelcome was disabled')

        else:
            file.close()

            with open('bd/AutoWelcome.txt', 'a') as file:
                file.write(f'{guild.id}\n')

            embed_var = discord.Embed(title= 'AutoWelcome enabled', color= 0xc1818f)
            embed_var.add_field(name= 'AutoWelcome was enabled', value= 'To disable, use the same command')
            embed_var.set_thumbnail(url= self.client.user.avatar_url)
            embed_var.set_footer(icon_url= ctx.author.avatar_url, text= f'Requested by: {ctx.author}')
            await ctx.send(embed= embed_var)


def setup(client):
    client.add_cog(Auto(client))
