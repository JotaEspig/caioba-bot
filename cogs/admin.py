import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Kick
    @commands.command(aliases= ['KICK'])
    @commands.has_permissions(kick_members= True)
    async def kick(self, ctx, user: discord.Member, *, reason= None):
        await user.kick(reason= reason)
        await ctx.send(f'{user.name} was kicked')

    #Ban
    @commands.command(aliases= ['BAN'])
    @commands.has_permissions(ban_members= True)
    async def ban(self, ctx, user: discord.Member, *, reason= None):
        await user.ban(reason= reason)
        await ctx.send(f'{user.name} is banned')

    #Unban
    @commands.command(aliases= ['UNBAN'])
    @commands.has_permissions(ban_members= True)
    async def unban(self, ctx, user: str):
        banned_users = await ctx.guild.bans()
        user_name, user_discriminator = user.split('#') #Nome e discriminador passados

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (user_name, user_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user} was unbanned')
                return
        await ctx.send(f'{user} isn\'t banned')


def setup(client):
    client.add_cog(Admin(client))
