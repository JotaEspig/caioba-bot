import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    #dict comandos com explicações
    comandos = {
        #Admin
        'kick': 'Kicks an user. Mark the user with @',
        'ban': 'Ban an user. Mark the user with @',
        'unban': 'Unban an user. Type the nickname + tag. Ex.: JotaEspig#4394',
        #Useful
        'chatclear': 'Cleans the chat. Mark a user or @here. Clean by default: 1000',
        'ping': 'Shows the ping',
        'vote': 'Sends the link to vote for me',
        #Profile
        'profile': 'Shows your profile or from other user',
        'set_desc': 'Sets your description. Max characters: 150',
        'set_gender': 'Sets your gender. Type only \"m\" or \"f\". m = Male e f = Female ',
        'set_birth': 'Sets your age and your birthday. Correct format: \"mm/dd/aaaa\" with the bars. Ex.: `cb!set_birth 01/01/2000`',
        'marry': 'Propose a marriage',
        'accept_marriage': 'Accept a marriage',
        'reject_marriage': 'Reject a marriage',
        'cancel_marriage': 'Cancel a marriage that you proposed',
        'date': 'Propose a date',
        'accept_date': 'Accept a date',
        'reject_date': 'Reject a date',
        'cancel_date': 'Cancel a date that you proposed',
        'breakup': 'Breakup with the user',
        #Reddit
        'rmemes': 'Posts a meme from r/memes',
        'rdankmemes': 'Posts a meme from r/dankmemes',
        'rpics': 'Post a pic from r/pics',
        'rfiftyfifty': 'Posts a \"50/50\" from r/fiftyfifty',
        'subr': 'Posts something about the subreddit that you typed. Ex.: `cb!subr memes`. \nP.S.: Vidoes aren\'t supported',
        #Reddit NSFW
        'rhentai': 'Posts a hentai from r/hentai. Needs NSFW-Channel',
        'recchi': 'Posts an ecchi anime from r/ecchi. Needs NSFW-Channel',
        'rboobs': 'Posts some boobs from r/boobs. Needs NSFW-Channel',
        'rbutt': 'Posts some butt from r/butt. Needs NSFW-Channel',
        'rule34': 'Posts a rule34 from r/rule34. Needs NSFW-Channel',
        #Roleplay
        'hug': 'You will hug someone in GIF. Mark the user with @',
        'scared': 'You will be scared in anime GIF',
        'shoot': 'You will shoot someone in anime GIF. Mark the user with @',
        'kiss': 'You will kiss someone in anime GIF. Mark the user with @',
        'morning': 'You will say \"Good morning\" to someone(or everyone) in anime GIF.',
        'angry': 'You will be angry in anime GIF.',
        'call': 'You will call an user in anime GIF. Mark the user with @',
        'cry': 'You will cry in anime GIF.',
        'dance': 'You will dance in anime GIF',
        'happy': 'You will be happy in anime GIF',
        'kill': 'You will kill someone in anime GIF. Mark the user with @',
        'laugh': 'You will laugh in anime GIF',
        'punch': 'You will punch someone in anime GIF. Mark the user with @',
        'sad': 'You will sad in anime GIF',
        'shy': 'You will be shy in anime GIF',
        #Jokes
        '8ball': 'You make a yes-no question and I\'ll answer it',
        'ship': 'You will ship someone, and I\'ll tell you the percentage',
        'say': 'Will send a tts message',
        #Auto
        'automemes': 'You will receive a meme 4 times a day from r/memes',
        'autodankmemes': 'You will receive a meme 4 times a day from r/dankmemes',
        'autowelcome': 'Who join on server will receive a welcome message in DM',
        #Help
        'help': 'Shows the available commands.\n\"<>\" specify a mandatory variable, \"[]\" specify an optional variable, and \"()\" specify the only options for the variable. Ex.: `cb!set_gender (m / f)` m and f are the only ones possibilities for the variable',
        'command': 'Are you trying to create a paradox?',
        'support': 'I will invite you for my own server, so I can help you with your question'
    }

    #HELP - COMANDOS
    @commands.command(aliases= ['HELP'])
    async def help(self, ctx):
        embed_var = discord.Embed(title= '⭐Commands⭐', color= 0xc1818f)
        embed_var.set_thumbnail(url= self.client.user.avatar_url)

        #Administração
        embed_var.add_field(name= '🧠Admin🧠', value= '`kick <user> [reason]`, `ban <user> [reason]`, `unban <nickname and tag>`', inline= False)
        #Úteis
        embed_var.add_field(name= '🔧Useful🔧', value= '`chatclear <user or @here> [quantity]`, `ping`, `vote`', inline= False)
        #Perfil
        embed_var.add_field(name= '📝Profile📝', value= '`profile [user]`, `set_desc <desc>`, `set_gender (m / f)`, `set_birth <mm/dd/aaaa>`, `marry <user>`, `accept_marriage <user>`, `reject_marriage <user>`, `cancel_marriage <user>`, `date <user>`, `accept_date <user>`, `reject_date <user>`, `cancel_date <user>`, `breakup <user>`', inline= False)
        #Reddit
        embed_var.add_field(name= '💥Reddit💥', value= '`rmemes`, `rdankmemes`, `rpics`, `rfiftyfifty`, `subr <subreddit>`', inline= False)
        #Reddit+18
        embed_var.add_field(name= '🔞Reddit (NSFW)🔞', value= '||`rhentai`, `recchi`, `rboobs`, `rbutt`, `rule34`||', inline= False)
        #RolePlay
        embed_var.add_field(name= '🎭RolePlay🎭', value= '`angry [user]`, `call <user>`, `cry`, `dance`, `happy`, `hug <user>`, `kill <user>`, `kiss <user>`, `laugh`, `morning [user]`, `punch <user>`, `sad`, `scared`, `shoot <user>`, `shy`', inline= False)
        #Zueira
        embed_var.add_field(name= '🤣Fun🤣', value= '`8ball <question>`, `ship <user> <user>`, `say <message>`', inline= False)
        #Auto
        embed_var.add_field(name= '⚙Auto⚙', value= '`automemes <channel name>`, `autodankmemes <channel name>`, `autowelcome`', inline= False)
        #Help
        embed_var.add_field(name= 'Help', value= '*Use `cb!command <command>` to get details about a specific command. Ex.: `cb!command help`*', inline= False)

        embed_var.set_footer(icon_url= 'https://cdn.discordapp.com/avatars/720686657950711909/6fda15865e1aeed96ee1b3d4e9098391.webp?size=1024', text= 'Bot by: JotaEspig#4394')
        await ctx.send(embed= embed_var)

    #Comando específico
    @commands.command(aliases= ['COMMAND'])
    async def command(self, ctx, nome_comando: str):
        nome_comando = nome_comando.lower()
        if nome_comando in self.comandos.keys():
            embed_var = discord.Embed(title= nome_comando.title(), description= f'*{self.comandos[nome_comando]}*', color= 0xc1818f)
            embed_var.set_thumbnail(url= self.client.user.avatar_url)
            embed_var.set_footer(icon_url= ctx.author.avatar_url, text=f'Requested by: {ctx.author}')
            await ctx.send(embed= embed_var)
        else:
            await ctx.send(f'\"{nome_comando}\" doesn\'t exist or it isn\'t in my database')

    #Servidor de suporte
    @commands.command(aliases= ['SUPPORT'])
    async def support(self, ctx):
        embed_var = discord.Embed(title= 'Support', description= '*Join for help!*\nhttps://discord.gg/SzU8XAqz', color= 0xc1818f)
        embed_var.set_thumbnail(url= self.client.user.avatar_url)
        embed_var.set_footer(icon_url= 'https://cdn.discordapp.com/avatars/720686657950711909/6fda15865e1aeed96ee1b3d4e9098391.webp?size=1024', text= 'Bot do: JotaEspig#4394')
        await ctx.send(embed= embed_var)


def setup(client):
    client.add_cog(Help(client))
