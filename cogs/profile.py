import discord
from discord.ext import commands
import datetime
import json


class Profile(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Verifica se o usuário está no banco de dados
    def verify_user(self, user: discord.Member):
        with open('bd/users.json') as file:
            users = json.loads(file.read())
        if str(user.id) not in users.keys():
            self.create_profile(user)
            with open('bd/users.json') as file:
                users = json.loads(file.read())
        return users

    #Criador Perfil
    def create_profile(self, user: discord.Member):
        usuário = {
            str(user.id): {
                'nickname': user.name,
                'desc': '*Use `cb!set_desc <desc>`*',
                'avatar': str(user.avatar_url),
                'gender': 'Unknown',
                'age': {
                    'age': 'Unknown',
                    'birth': None
                },
                'marital status': {
                    'status': 'Single',
                    'partner': None,
                    'requests': []
                }
            }
        }

        with open('bd/users.json') as file:
            users = json.loads(file.read())
        users.update(usuário)
        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

    #Update json
    @staticmethod
    async def update_json(user: discord.Member):
        with open('bd/users.json') as file:
            users = json.loads(file.read())
        #Nickname
        if user.name != users[str(user.id)]['nickname']:
            users[str(user.id)]['nickname'] = user.name
        #Avatar
        if str(user.avatar_url) != users[str(user.id)]['avatar']:
            users[str(user.id)]['avatar'] = str(user.avatar_url)
        #Age
        user_age = users[str(user.id)]['age']
        if user_age['birth'] != None:
            str_birth = user_age['birth']
            #Passa o str_birth para um objeto datetime, que passa para a função find_age
            age_for_verify = Profile.find_age(Profile.to_datetime(str_birth))
            if age_for_verify != user_age['age']:
                users[str(user.id)]['age']['age'] = age_for_verify
        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

    #Passa string da data para um objeto do datetime
    #dd/mm/aaaa
    @staticmethod
    def to_datetime(string_date: str):
        string_date = string_date.split('/')
        mes = int(string_date[0])
        dia = int(string_date[1])
        ano = int(string_date[2])
        return datetime.datetime(ano, mes, dia)

    #Descobre a age
    @staticmethod
    def find_age(nasc):
        hoje = datetime.date.today()
        return hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))

    #Visualizador Perfil
    @commands.command(aliases= ['PROFILE'])
    async def profile(self, ctx, user= None):
        with open('bd/users.json') as file:
            users = json.loads(file.read())
        if user == None:
            user_id = str(ctx.author.id)
        else:
            #Filtra apenas os números, para ter o id do usuário
            user_id = ''
            for char in user:
                if char.isnumeric():
                    user_id += char
        #Verifica se o usuário já está no banco de dados
        if user_id not in users.keys():
            if int(user_id) == ctx.author.id:
                self.create_profile(ctx.author)
                with open('bd/users.json') as file:
                    users = json.loads(file.read())
            else:
                user = self.client.get_user(int(user_id))
                self.create_profile(user)
                with open('bd/users.json') as file:
                    users = json.loads(file.read())

        user_profile = users[user_id]
        status = user_profile['marital status']['status']

        if user_profile['gender'] == 'Male':
            embed_var = discord.Embed(title= user_profile['nickname'], description= user_profile['desc'], color= 0x00f2ff)
        elif user_profile['gender'] == 'Female':
            embed_var = discord.Embed(title= user_profile['nickname'], description= user_profile['desc'], color= 0xff00dd)
        else:
            embed_var = discord.Embed(title= user_profile['nickname'], description= user_profile['desc'], color= 0xffffff)

        embed_var.set_thumbnail(url= user_profile['avatar'])
        embed_var.add_field(name= 'Gender', value= user_profile['gender'], inline= False)
        embed_var.add_field(name= 'Age', value= user_profile['age']['age'], inline= False)
        if user_profile['age']['birth'] != None:
            embed_var.add_field(name= 'Birthday', value= user_profile['age']['birth'])

        if status == 'Single':
            embed_var.add_field(name= 'Marital Status', value= status, inline= False)
        else:
            cônjuge_id = user_profile['marital status']['partner']
            cônjuge = users[cônjuge_id]['nickname']
            embed_var.add_field(name= 'Marital Status', value= f'{status} / {cônjuge}', inline= False)
        await ctx.send(embed= embed_var)
        
    #Definir desc
    @commands.command(aliases= ['SET_DESC'])
    async def set_desc(self, ctx, *, desc: str):
        if len(desc) > 150:
            await ctx.send('Your description can\'t have more than 150 characters')
            return

        #Verfifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)

        users[str(ctx.author.id)]['desc'] = desc

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send('description setted')

    #Definir Gender
    @commands.command(aliases= ['SET_GENDER'])
    async def set_gender(self, ctx, gender: str):
        if gender.lower() != 'm' and gender.lower() != 'f':
            await ctx.send('An error occured, use `cb!comando def_gender`')
            return

        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)

        if gender.lower() == 'm':
            users[str(ctx.author.id)]['gender'] = 'Male'
        elif gender.lower() == 'f':
            users[str(ctx.author.id)]['gender'] = 'Female'
        
        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send('Gender setted')

    #Definir Nascimento/age
    @commands.command(aliases= ['SET_BIRTH'])
    async def set_birth(self, ctx, nasc: str):
        string_date = nasc.split('/')

        if len(string_date) > 3:
            await ctx.send('An error ocurred, use `cb!comando def_birth`')
            return

        mes = string_date[0]
        dia = string_date[1]
        ano = string_date[2]

        nascimento = self.to_datetime(nasc)

        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)

        users[str(ctx.author.id)]['age']['age'] = self.find_age(nascimento)
        users[str(ctx.author.id)]['age']['birth'] = f'{mes}/{dia}/{ano}'

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send('Age and birthday setted')

    #Casar
    @commands.command(aliases= ['MARRY'])
    async def marry(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)

        pedido_enviado = False
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Sended':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Marriage':
                        pedido_enviado = True
        
        if pedido_enviado == True:
            await ctx.send(' You already proposed to this user')
            return
        
        if users[str(ctx.author.id)]['marital status']['partner'] == str(user.id):
            if users[str(ctx.author.id)]['marital status']['status'] == 'Married':
                await ctx.send(' You already married with this user')
                return
            elif users[str(ctx.author.id)]['marital status']['status'] != 'Dating':
                await ctx.send('You must be dating the user to propose to it')
                return
        else:
            await ctx.send('You must be dating the user to propose to it')
            return

        users[str(ctx.author.id)]['marital status']['requests'].append({
            'user': str(user.id),
            'type': 'Marriage',
            'status': 'Sended'
        })
        users[str(user.id)]['marital status']['requests'].append({
            'user': str(ctx.author.id),
            'type': 'Marriage',
            'status': 'Received'
        })

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> propose to <@!{user.id}>. To accept use `cb!accept_marriage <user>`' )

    #Aceitar Casamento
    @commands.command(aliases= ['ACCEPT_MARRIAGE'])
    async def accept_marriage(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        pedido_recebido = False
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Received':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Marriage':
                        pedido_recebido = True
        if pedido_recebido == False:
            await ctx.send('This user didn\'t propose to you')
            return
        
        users[str(ctx.author.id)]['marital status']['status'] = 'Married'
        users[str(ctx.author.id)]['marital status']['partner'] = str(user.id)
        
        users[str(user.id)]['marital status']['status'] = 'Married'
        users[str(user.id)]['marital status']['partner'] = str(ctx.author.id)

        users[str(ctx.author.id)]['marital status']['requests'] = []
        users[str(user.id)]['marital status']['requests'] = []

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> e <@!{user.id}> are married! Congratulations to the couple!:heart_eyes:')

    #Recusar Casamento
    @commands.command(aliases= ['REJECT_MARRIAGE'])
    async def reject_marriage(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        pedido_recebido = {}
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Received':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Marriage':
                        pedido_recebido.update(pedido)
        if pedido_recebido == {}:
            await ctx.send('This user didn\'t propose to you')
            return
        pedido_enviado = {}
        for pedido in users[str(user.id)]['marital status']['requests']:
            if pedido['status'] == 'Sended':
                if pedido['user'] == str(ctx.author.id):
                    if pedido['type'] == 'Marriage':
                        pedido_enviado.update(pedido)
        if pedido_enviado == {}:
            await ctx.send('This user didn\'t propose to you')
            return
        
        users[str(ctx.author.id)]['marital status']['requests'].remove(pedido_recebido)
        users[str(user.id)]['marital status']['requests'].remove(pedido_enviado)

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> rejected <@!{user.id}>!:cry:')

    #Cancelar Casamento
    @commands.command(aliases= ['CANCEL_MARRIAGE'])
    async def cancel_marriage(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        pedido_enviado = {}
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Sended':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Marriage':
                        pedido_enviado.update(pedido)
        if pedido_enviado == {}:
            await ctx.send('You didn\'t propose to this user')
            return
        pedido_recebido = {}
        for pedido in users[str(user.id)]['marital status']['requests']:
            if pedido['status'] == 'Received':
                if pedido['user'] == str(ctx.author.id):
                    if pedido['type'] == 'Marriage':
                        pedido_recebido.update(pedido)
        if pedido_recebido == {}:
            await ctx.send('You didn\'t propose to this user')
            return
        
        users[str(ctx.author.id)]['marital status']['requests'].remove(pedido_enviado)
        users[str(user.id)]['marital status']['requests'].remove(pedido_recebido)

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send('Marriage cancelled')

    #Namorar
    @commands.command(aliases= ['DATE'])
    async def date(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)

        pedido_enviado = False
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Sended':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Date':
                        pedido_enviado = True
        
        if pedido_enviado == True:
            await ctx.send(f'You already propose to this user')
            return
        if users[str(ctx.author.id)]['marital status']['status'] != 'Single':
            await ctx.send('You are already dating a user')
            return
        if users[str(user.id)]['marital status']['status'] != 'Single':
            await ctx.send('This user is already dating a other user')
            return
        
        users[str(ctx.author.id)]['marital status']['requests'].append({
            'user': str(user.id),
            'type': 'Date',
            'status': 'Sended'
        })
        users[str(user.id)]['marital status']['requests'].append({
            'user': str(ctx.author.id),
            'type': 'Date',
            'status': 'Received'
        })

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> propose to <@!{user.id}>. To accept, use `cb!accept_date <user>`' )

    #Aceitar Namoro
    @commands.command(aliases= ['ACCEPT_DATE'])
    async def accept_date(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        pedido_recebido = False
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Received':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Date':
                        pedido_recebido = True
        if pedido_recebido == False:
            await ctx.send('This user didn\'t propose to you')
            return
        
        users[str(ctx.author.id)]['marital status']['status'] = 'Dating'
        users[str(ctx.author.id)]['marital status']['partner'] = str(user.id)
        
        users[str(user.id)]['marital status']['status'] = 'Dating'
        users[str(user.id)]['marital status']['partner'] = str(ctx.author.id)

        users[str(ctx.author.id)]['marital status']['requests'] = []
        users[str(user.id)]['marital status']['requests'] = []

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> e <@!{user.id}> are dating! Congratulations to the couple!:heart_eyes:')

    #Recusar Namoro
    @commands.command(aliases= ['REJECT_DATE'])
    async def reject_date(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        pedido_recebido = {}
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Received':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Date':
                        pedido_recebido.update(pedido)
        if pedido_recebido == {}:
            await ctx.send('This user didn\'t propose to you')
            return
        pedido_enviado = {}
        for pedido in users[str(user.id)]['marital status']['requests']:
            if pedido['status'] == 'Sended':
                if pedido['user'] == str(ctx.author.id):
                    if pedido['type'] == 'Date':
                        pedido_enviado.update(pedido)
        if pedido_enviado == {}:
            await ctx.send('This user didn\'t propose to you')
            return
        
        users[str(ctx.author.id)]['marital status']['requests'].remove(pedido_recebido)
        users[str(user.id)]['marital status']['requests'].remove(pedido_enviado)

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> rejected <@!{user.id}>!:cry:')

    #Cancelar Namoro
    @commands.command(aliases= ['CANCEL_DATE'])
    async def cancel_date(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        pedido_enviado = {}
        for pedido in users[str(ctx.author.id)]['marital status']['requests']:
            if pedido['status'] == 'Sended':
                if pedido['user'] == str(user.id):
                    if pedido['type'] == 'Date':
                        pedido_enviado.update(pedido)
        if pedido_enviado == {}:
            await ctx.send('You didn\'t propose to this user')
            return
        pedido_recebido = {}
        for pedido in users[str(user.id)]['marital status']['requests']:
            if pedido['status'] == 'Received':
                if pedido['user'] == str(ctx.author.id):
                    if pedido['type'] == 'Date':
                        pedido_recebido.update(pedido)
        if pedido_recebido == {}:
            await ctx.send('You didn\'t propose to this user')
            return
        
        users[str(ctx.author.id)]['marital status']['requests'].remove(pedido_enviado)
        users[str(user.id)]['marital status']['requests'].remove(pedido_recebido)

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'Date cancelled')

    #Seperar
    @commands.command(aliases= ['SEPARAR'])
    async def breakup(self, ctx, user: discord.Member):
        #Verifica se o usuário está no banco de dados
        users = self.verify_user(ctx.author)
        users = self.verify_user(user)
        
        if users[str(ctx.author.id)]['marital status']['status'] == 'Single':
            await ctx.send('You are already single at the moment')
            return

        users[str(ctx.author.id)]['marital status']['status'] = 'Single'
        users[str(ctx.author.id)]['marital status']['partner'] = None
        
        users[str(user.id)]['marital status']['status'] = 'Single'
        users[str(user.id)]['marital status']['partner'] = None

        users[str(ctx.author.id)]['marital status']['requests'] = []
        users[str(user.id)]['marital status']['requests'] = []

        with open('bd/users.json', 'w') as file:
            file.write(json.dumps(users, indent= 4))

        await ctx.send(f'<@!{ctx.author.id}> e <@!{user.id}> break up!:sob:')

    
def setup(client):
    client.add_cog(Profile(client))
