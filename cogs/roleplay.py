import discord
from discord.ext import commands
import random


class Roleplay(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Angry
    @commands.command(aliases= ['ANGRY'])
    async def angry(self, ctx, user= None):
        gifs_url = []
        with open('roleplay/angry.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        if user == None:
            embed_var = discord.Embed(description= f'{author} is angry', color= 0xc1818f)
        else:
            embed_var = discord.Embed(description= f'{author} is angry with {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Call
    @commands.command(aliases= ['CALL'])
    async def call(self, ctx, user):
        gifs_url = []
        with open('roleplay/call.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} calls {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Cry
    @commands.command(aliases= ['CRY'])
    async def cry(self, ctx):
        gifs_url = []
        with open('roleplay/cry.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} is crying', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Dance
    @commands.command(aliases= ['DANCE'])
    async def dance(self, ctx):
        gifs_url = []
        with open('roleplay/dance.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} is dancing', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Happy
    @commands.command(aliases= ['HAPPY'])
    async def happy(self, ctx):
        gifs_url = []
        with open('roleplay/happy.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} is happy', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Hug
    @commands.command(aliases= ['HUG'])
    async def hug(self, ctx, user):
        gifs_url = []
        with open('roleplay/hug.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} hugs {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Kill
    @commands.command(aliases= ['KILL'])
    async def kill(self, ctx, user):
        gifs_url = []
        with open('roleplay/kill.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} kills {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Kiss
    @commands.command(aliases= ['KISS'])
    async def kiss(self, ctx, user):
        gifs_url = []
        with open('roleplay/kiss.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} kisses {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Laugh
    @commands.command(aliases= ['LAUGH'])
    async def laugh(self, ctx):
        gifs_url = []
        with open('roleplay/laugh.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} is laughing', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Morning
    @commands.command(aliases= ['MORNING'])
    async def morning(self, ctx, user= None):
        gifs_url = []
        with open('roleplay/morning.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        if user == None:
            embed_var = discord.Embed(description= f'{author} says good morning to everyone', color= 0xc1818f)
        else:
            embed_var = discord.Embed(description= f'{author} says good morning to {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Punch
    @commands.command(aliases= ['PUNCH'])
    async def punch(self, ctx, user):
        gifs_url = []
        with open('roleplay/punch.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} punches {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Sad
    @commands.command(aliases= ['SAD'])
    async def sad(self, ctx):
        gifs_url = []
        with open('roleplay/sad.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} is sad', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Scared
    @commands.command(aliases= ['SCARED'])
    async def scared(self, ctx):
        gifs_url = []
        with open('roleplay/scared.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} is scared', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Shoot
    @commands.command(aliases= ['SHOOT'])
    async def shoot(self, ctx, user):
        gifs_url = []
        with open('roleplay/shoot.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} shoots {user}', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)

    #Shy
    @commands.command(aliases= ['SHY'])
    async def shy(self, ctx):
        gifs_url = []
        with open('roleplay/shy.txt') as file:
            for item in file:
                gifs_url.append(item.strip('\n'))

        author = f'<@!{ctx.author.id}>'
        embed_var = discord.Embed(description= f'{author} shies', color= 0xc1818f)
        embed_var.set_image(url= random.choice(gifs_url))
        await ctx.send(embed= embed_var)


def setup(client):
    client.add_cog(Roleplay(client))
