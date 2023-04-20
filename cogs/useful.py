import discord
from discord.ext import commands, tasks


class Useful(commands.Cog):

    def __init__(self, client):
        self.client = client

    #ChatClear
    @commands.command(aliases= ['CHATCLEAR'])
    @commands.has_permissions(manage_messages= True)
    async def chatclear(self, ctx, user, amount= 1000):
        def is_author(m):
            if user == '@here' or user == '@everyone':
                return True
            user_id = ''
            for char in user:
                if char.isnumeric():
                    user_id += char
            try:
                if m.author.id == int(user_id):
                    return True
                else:
                    return False
            except ValueError:
                return False
        await ctx.channel.purge(limit= amount+1, check= is_author)

    #Ping
    @commands.command(aliases= ['PING'])
    async def ping(self, ctx):
        embed_var = discord.Embed(title= 'Ping', description= f'{round(self.client.latency * 1000)}ms', color= 0xc1818f)
        embed_var.set_thumbnail(url= self.client.user.avatar_url)
        await ctx.send(embed= embed_var)

    #Vote
    @commands.command(aliases= ['VOTE'])
    async def vote(self, ctx):
        await ctx.send('https://top.gg/bot/818875382769909830/vote')


def setup(client):
    client.add_cog(Useful(client))
