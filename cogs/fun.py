import discord
from discord.ext import commands, tasks
import random


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #8Ball
    @commands.command(aliases= ['8BALL', '8ball'])
    async def _8ball(self, ctx, *, question: str):
        respostas = [
            'Of course',
            'Yes',
            'Just yes',
            'probably yes',
            'Only time will tell',
            'Impossible to say',
            'You\'re too dumb to understand',
            'Your mind knows the answer',
            'Probably not',
            'Just no',
            'No',
            'Of course not'
        ]

        embed_var = discord.Embed(title= '8Ball', description= f'Question: {question}\nAnswer: {random.choice(respostas)}', color= 0xc1818f)
        embed_var.set_thumbnail(url= self.client.user.avatar_url)
        embed_var.set_footer(icon_url= ctx.author.avatar_url, text=f'Requested by: {ctx.author}')
        await ctx.send(embed= embed_var)

    #Ship
    @commands.command(aliases= ['SHIP'])
    async def ship(self, ctx, user_1, user_2):
        pct = random.randint(0, 100)

        embed_var = discord.Embed(title= f'Ship:', description= f'{user_1} & {user_2}', color= 0xc1818f)
        
        if pct <= 5:
            embed_var.add_field(name= ':cold_face: I am sorry, but it\'s impossible :cold_face: ', value= f'{pct}% - [..........]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/google/android-pie/512px/1f494.png')
        elif pct < 15:
            embed_var.add_field(name= ':confounded: I\'m sorry, but it\'s too hard to happen :confounded: ', value= f'{pct}% - [█.........]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/google/android-pie/512px/1f494.png')
        elif pct < 25:
            embed_var.add_field(name= ':confounded: I\'m sorry, but it\'s too hard to happen :confounded: ', value= f'{pct}% - [██........]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/google/android-pie/512px/1f494.png')
        elif pct < 35:
            embed_var.add_field(name= ':worried: It\'s very unlikely :worried: ', value= f'{pct}% - [███.......]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/google/android-pie/512px/1f494.png')
        elif pct < 45:
            embed_var.add_field(name= ':frowning2: It\'s unlikely :frowning2: ', value= f'{pct}% - [████......]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/google/android-pie/512px/1f494.png')
        elif pct < 55:
            embed_var.add_field(name= ':face_with_monocle: 50/50. Maybe :face_with_monocle: ', value= f'{pct}% - [█████.....]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/twitter/512px/2764.png')
        elif pct < 65:
            embed_var.add_field(name= ':hugging: Probably, but I\'m not sure :hugging: ', value= f'{pct}% - [██████....]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/twitter/512px/2764.png')
        elif pct < 75:
            embed_var.add_field(name= ':smirk: It\'s very probably to happen :smirk: ', value= f'{pct}% - [███████...]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/twitter/512px/2764.png')
        elif pct < 85:
            embed_var.add_field(name= f':partying_face: I\'m {pct}% sure! Go ahead :partying_face: ', value= f'{pct}% - [████████..]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/twitter/512px/2764.png')
        elif pct < 95:
            embed_var.add_field(name= ':smiling_face_with_3_hearts: It\'s impossible to not happen! Go ahead! :smiling_face_with_3_hearts: ', value= f'{pct}% - [█████████.]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/twitter/512px/2764.png')
        else:
            embed_var.add_field(name= ':heart_eyes: :notes: OH, LOVE ME, MISTER, OH, MISTER\nyume janai nara kikasete:notes: :heart_eyes: ', value= f'{pct}% - [██████████]')
            embed_var.set_thumbnail(url= 'https://images.emojiterra.com/twitter/512px/2764.png')
        embed_var.set_footer(icon_url= ctx.author.avatar_url, text=f'Requested by: {ctx.author}')

        await ctx.send(embed= embed_var)
    
    #Falar
    @commands.command(aliases= ['SAY'])
    @commands.has_permissions(send_tts_messages= True)
    async def say(self, ctx, *, msg):
        await ctx.send(msg, tts= True)


def setup(client):
    client.add_cog(Fun(client))
