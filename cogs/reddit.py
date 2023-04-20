import discord
from discord.ext import commands
import praw
import random


class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client

    #API Reddit
    # You must put your reddit info here
    reddit = praw.Reddit(client_id= "CLIENT_ID",
                        client_secret= "CLIENT_SECRET",
                        username= "USERNAME",
                        password= "PASSWORD",
                        user_agent= "USER_AGENT")

    @staticmethod
    async def search_reddit(ctx, subr_input: str, auto= False):
        """Função que procura e posta um post de determinado subreddit

        Args:
            ctx (discord.ext.commands.context.Context, discord.channel.TextChannel): Contexto do requerimento ou Canal para postagem automática.
            subr_input (str): nome do subreddit.
            auto (bool, optional): Verifica se o post é para ser automático ou não. Defaults to False.
        """
        
        tipos_arquivo = ['jpg', 'png', 'gif']

        subreddit = Reddit.reddit.subreddit(subr_input)
        if subreddit.over18 and not auto:
            if not ctx.channel.nsfw:
                await ctx.send(f':hand_splayed::underage:Not a NSFW-Channel:underage:')
                return

        all_posts = []

        hot = subreddit.hot(limit= 50)

        for post in hot:
            all_posts.append(post)

        random_post = random.choice(all_posts)

        last_pos = len(random_post.url) + 1
        i = 0
        while not (random_post.url[-3:last_pos] in tipos_arquivo):
            random_post = random.choice(all_posts)
            i += 1
            if i > 50:
                break

        if i > 50 and not auto:
            await ctx.send('An error occurred, try again or try another subreddit')
            return

        if random_post.over_18 and not auto:
            if not ctx.channel.nsfw:
                await ctx.send(':hand_splayed::underage:Not a NSFW-Channel:underage::hand_splayed:')
                return

        name = random_post.title
        url = random_post.url

        if not auto:
            embed_var = discord.Embed(title= name, color= 0xc1818f)
            embed_var.set_author(name= f'From r/{subr_input}')
            embed_var.set_image(url= url)
            embed_var.set_footer(icon_url= ctx.author.avatar_url, text=f'Requested by: {ctx.author}')
        else:
            embed_var = discord.Embed(title= name, color= 0xc1818f)
            embed_var.set_author(name= f'From r/{subr_input}')
            embed_var.set_image(url= url)
            embed_var.set_footer(icon_url= 'https://cdn.discordapp.com/avatars/720686657950711909/6fda15865e1aeed96ee1b3d4e9098391.webp?size=1024', text='Bot by: JotaEspig#4394')

        await ctx.send(embed= embed_var)

        if random_post.over_18 and not auto:
            if ctx.channel.nsfw:
                #Mendigador de votos
                if random.randint(1, 5) == 1:
                    msg = 'Help me! Vote for me!\nhttps://top.gg/bot/818875382769909830/vote\nThis help me a lot:blush:'
                    await ctx.author.send(msg)

    #SFW
    #r/memes
    @commands.command(aliases= ['RMEMES'])
    async def rmemes(self, ctx):
        await self.search_reddit(ctx, 'memes')

    #r/dankmemes
    @commands.command(aliases= ['RDANKMEMES'])
    async def rdankmemes(self, ctx):
        await self.search_reddit(ctx, 'dankmemes')

    #r/pics
    @commands.command(aliases= ['RPICS'])
    async def rpics(self, ctx):
        await self.search_reddit(ctx, 'pics')

    #r/FiftyFifty
    @commands.command(aliases= ['RFIFTYFIFTY'])
    async def rfiftyfifty(self, ctx):
        await self.search_reddit(ctx, 'fiftyfifty')

    #Subreddit qualquer
    @commands.command(aliases= ['SUBR'])
    async def subr(self, ctx, subr_input: str):
        await self.search_reddit(ctx, subr_input)
        
    #NSFW
    #r/hentai
    @commands.command(aliases= ['RHENTAI'])
    async def rhentai(self, ctx):
        await self.search_reddit(ctx, 'hentai')
    #r/ecchi
    @commands.command(aliases= ['RECCHI'])
    async def recchi(self, ctx):
        await self.search_reddit(ctx, 'ecchi')
    #r/boobs
    @commands.command(aliases= ['RBOOBS'])
    async def rboobs(self, ctx):
        await self.search_reddit(ctx, 'boobs')
    #r/butt
    @commands.command(aliases= ['RBUTT'])
    async def rbutt(self, ctx):
        await self.search_reddit(ctx, 'butt')
    #r/rule34
    @commands.command(aliases= ['RULE34'])
    async def rule34(self, ctx):
        await self.search_reddit(ctx, 'rule34')


def setup(client):
    client.add_cog(Reddit(client))
