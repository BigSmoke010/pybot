from discord.ext import commands
import discord
import sqlite3 as sql
import random
import datetime

class economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='register')
    async def register(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users(username,id,balance)')
        cursor.execute('CREATE TABLE IF NOT EXISTS workcooldown(userid,expiredate)')
        cursor.execute('CREATE TABLE IF NOT EXISTS betcooldowns (memberid, expiration)')
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        tmplist = []
        for i in valid:
            tmplist.append(i[1])
        if ctx.author.id in tmplist:
            await ctx.send('you are already registered in the database')
        elif ctx.author.id not in tmplist:
            cursor.execute(
                "INSERT INTO users (username,id,balance) VALUES (:name, :userid, 0)",
                {
                    'name': ctx.author.name,
                    'userid': ctx.author.id
                })
            await ctx.send('succesfully registered into the db')
            db.commit()
            cursor.close()
            db.close()

    @commands.command(name='balance')
    async def bal(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        for i in valid:
            if i[1] == user.id:

                embed = discord.Embed(color=7377330,
                                    title=user.name + '\'s balance',
                                    description='**Balance**\n`' +
                                    str(i[2]) + '`')
                await ctx.send(embed=embed)
                cursor.close()
                db.close()


    @commands.command(name='work')
    async def work(self, ctx):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        valid = cursor.fetchall()
        listofworks = ['you have killed hitler and won ', 'some random rich nigga saw you at the street and gave you ', 'you convinced stam to sell you his gpu and got ', 'you have joined filippas and stam in robbing a fucking bank and got ', 'you became a prostitute and gained ', 'super thought you were yasmin and gave you ', 'you worked for andrew tate for 30 minutes and he generousely gave you ', 'you started an onlyfans and got ', 'you sued fortnite and got ']
        for i in valid:
            if i[1] == ctx.author.id:
                currenttime = datetime.datetime.now()
                plusonehour = currenttime + datetime.timedelta(minutes=5)
                tmplist = []
                cursor.execute("SELECT * FROM workcooldown")
                allcooldowns = cursor.fetchall()
                for x in allcooldowns:
                    tmplist.append(x[0])

                if ctx.author.id in tmplist:
                    if datetime.datetime.strptime(allcooldowns[tmplist.index(ctx.author.id)][1], '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.now():
                        cursor.execute('DELETE FROM workcooldown WHERE userid ='+ str(ctx.author.id))
                        probablity = random.randrange(0, 100)
                        if probablity < 1:
                            amount = random.choice(range(10000, 100000))
                            await ctx.send(random.choice(listofworks) + str(amount))
                        if probablity < 30 and not probablity<1:
                            amount = random.choice(range(1000, 2000))
                            await ctx.send(random.choice(listofworks) + str(amount))
                        if probablity < 60 and not probablity< 30 and not probablity<1:
                            amount = random.choice(range(551, 900))
                            await ctx.send(random.choice(listofworks) + str(amount))
                        if probablity < 100 and not probablity < 60 and not probablity< 30 and not probablity<1:
                            amount = random.choice(range(200, 550))
                            await ctx.send(random.choice(listofworks) + str(amount))
                        cursor.execute('SELECT * FROM users WHERE id ='  + str(ctx.author.id))
                        selecteduser = cursor.fetchone()
                        total = selecteduser[2] + amount
                        cursor.execute('UPDATE users SET balance = :total WHERE id = :authorid',
                        {
                            'total' : total,
                            'authorid' : ctx.author.id
                        })
                        cursor.execute('INSERT INTO workcooldown VALUES (:userid,:plusonehour)',
                        {
                            'userid' : ctx.author.id,
                            'plusonehour' : plusonehour
                        })
                        db.commit()
                    elif datetime.datetime.strptime(allcooldowns[tmplist.index(ctx.author.id)][1], '%Y-%m-%d %H:%M:%S.%f')  > datetime.datetime.now():
                        diftime = datetime.datetime.strptime(allcooldowns[tmplist.index(ctx.author.id)][1], '%Y-%m-%d %H:%M:%S.%f')  - datetime.datetime.now()
                        seconds = diftime.seconds
                        minutes = (seconds//60) % 60
                        if minutes == 0:
                            await ctx.send('you are on cooldown, **' + str(seconds) + ' Seconds** left')
                        else:
                            await ctx.send('you are on cooldown, **' + str(minutes)  + ' Minutes** left')

                        cursor.close()
                        db.close()
                elif ctx.author.id not in tmplist:
                    x = random.randrange(0, 100)
                    if x < 1:
                        amount = random.choice(range(10000, 100000))
                        await ctx.send(random.choice(listofworks) + str(amount))
                    if x < 30 and not x<1:
                        amount = random.choice(range(1000, 2000))
                        await ctx.send(random.choice(listofworks) + str(amount))
                    if x < 60 and not x< 30 and not x<1:
                        amount = random.choice(range(551, 999))
                        await ctx.send(random.choice(listofworks) + str(amount))
                    if x < 100 and not x < 60 and not x< 30 and not x<1:
                        amount = random.choice(range(0, 550))
                        await ctx.send(random.choice(listofworks) + str(amount))

                    cursor.execute('SELECT * FROM users WHERE id ='  + str(ctx.author.id))
                    selecteduser = cursor.fetchone()
                    total = selecteduser[2] + amount
                    cursor.execute('UPDATE users SET balance = :total WHERE id = :authorid',
                    {
                        'total' : total,
                        'authorid' : ctx.author.id
                    })
                    cursor.execute('INSERT INTO workcooldown VALUES (:userid,:plusonehour)',
                    {
                        'userid' : ctx.author.id,
                        'plusonehour' : plusonehour
                    })

                    db.commit()
                    cursor.close()
                    db.close()
    @commands.command(name='bet')
    async def bet(self, ctx, amountbet):
        db = sql.connect('economydb.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        allusers = cursor.fetchall()
        for i in allusers:
            if i[1] == ctx.author.id:
                cursor.execute('SELECT * FROM betcooldowns')
                allcools = cursor.fetchall()
                tmplist = []
                for x in allcools:
                    tmplist.append(x[0])
                if ctx.author.id in tmplist:
                    if datetime.datetime.strptime(allcools[tmplist.index(ctx.author.id)][1], '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.now():
                        cursor.execute('DELETE FROM betcooldowns WHERE memberid =' + str(ctx.author.id))
                        if amountbet == 'all':
                            amountbet = i[2]
                        if i[2] >= int(amountbet):
                            prob = random.randrange(0,100)
                            if prob < 50:
                                newbal = int(i[2]) + int(amountbet)
                                cursor.execute('UPDATE users SET balance = :newbal WHERE id = :userid',
                                {
                                    'newbal' : newbal,
                                    'userid' : i[1]
                                })
                                currenttime = datetime.datetime.now()
                                nexttime = datetime.timedelta(minutes = 1   ) + currenttime
                                cursor.execute('INSERT INTO  betcooldowns VALUES (:userid,:expirationdate)',
                                {
                                    'userid' : ctx.author.id,
                                    'expirationdate' : nexttime
                                })
                                db.commit()
                                cursor.close()
                                db.close()

                                await ctx.send('you have won **'+ str(amountbet) + 'pc**')
                            else:
                                newbal = int(i[2]) - int(amountbet)
                                cursor.execute('UPDATE users SET balance = :newbal WHERE id = :userid',
                                {
                                    'newbal' : newbal,
                                    'userid' : i[1]
                                })
                                currenttime = datetime.datetime.now()
                                nexttime = datetime.timedelta(minutes = 1   ) + currenttime
                                cursor.execute('INSERT INTO  betcooldowns VALUES (:userid,:expirationdate)',
                                {
                                    'userid' : ctx.author.id,
                                    'expirationdate' : nexttime
                                })
                                db.commit()
                                cursor.close()
                                db.close()

                                await ctx.send('you have lost **'+ str(amountbet) + 'pc**')
                        else:
                            await ctx.send('you betted more money than you have!')
                            cursor.close()
                            db.close()
                    else:
                        await ctx.send('you are on cooldown')
                else:
                    if amountbet == 'all':
                        amountbet = i[2]
                    if i[2] >= int(amountbet):
                        prob = random.randrange(0,100)
                        if prob < 50:
                            newbal = int(i[2]) + int(amountbet)
                            cursor.execute('UPDATE users SET balance = :newbal WHERE id = :userid',
                            {
                                'newbal' : newbal,
                                'userid' : i[1]
                            })
                            currenttime = datetime.datetime.now()
                            nexttime = datetime.timedelta(minutes=1) + currenttime
                            cursor.execute('INSERT INTO  betcooldowns VALUES (:userid,:expirationdate)',
                            {
                                'userid' : ctx.author.id,
                                'expirationdate' : nexttime
                            })
                            db.commit()
                            cursor.close()
                            db.close()

                            await ctx.send('you have won **'+ str(amountbet) + 'pc**')
                        else:
                            print(i)
                            newbal = int(i[2]) - int(amountbet)
                            cursor.execute('UPDATE users SET balance = :newbal WHERE id = :userid',
                            {
                                'newbal' : newbal,
                                'userid' : i[1]
                            })
                            currenttime = datetime.datetime.now()
                            nexttime = datetime.timedelta(minutes = 1   ) + currenttime
                            cursor.execute('INSERT INTO  betcooldowns VALUES (:userid,:expirationdate)',
                            {
                                'userid' : ctx.author.id,
                                'expirationdate' : nexttime
                            })
                            db.commit()
                            cursor.close()
                            db.close()

                            await ctx.send('you have lost **'+ str(amountbet) + 'pc**')
                    else:
                        await ctx.send('you betted more money than you have!')
                        cursor.close()
                        db.close()

async def setup(bot):
    await bot.add_cog(economy(bot))
