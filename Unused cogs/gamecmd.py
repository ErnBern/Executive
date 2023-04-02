import discord, random, sqlite3
from discord.ext import commands

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

player1 = ""
player2 = ""
turn = ""
gameOver = True
accept1 = False

board = []

b = ""

mathequation = ""

mathgame = True

mathplayer = ""

db = sqlite3.connect('main.db')
cursor = db.cursor()



class Game_Cmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Game Cog is ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        global db
        global cursor
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        if message.channel in text_channel_list:
            if len(message.content) >= 3:
                if not message.author.bot:
                    cursor.execute(f"SELECT id FROM levels WHERE id = '{message.author.id}'")
                    stats = cursor.fetchone()
                    if stats is None:
                        userdata = (f"{message.author.id}", 0, f"{message.author}")
                        sql = ("INSERT INTO levels(id, xp, username) VALUES(?,?,?)")
                        cursor.execute(sql, userdata)
                        db.commit()
                    else:
                        cursor.execute(f"SELECT xp FROM levels WHERE id = '{message.author.id}'")
                        a = cursor.fetchone()
                        result = str(a).split('(')[1]
                        result2 = str(result).split(',')[0]
                        xp = int(result2)
                        xp += 1
                        cursor.execute(f"UPDATE levels SET xp = '{xp}' WHERE id = '{message.author.id}'")
                        db.commit()
                        try:
                            cursor.execute(f"UPDATE levels SET username = '{message.author}' WHERE id = '{message.author.id}''")
                            db.commit()
                        except:
                            pass

    @commands.command(invoke_without_command=True, aliases=['ttt'], name="tictactoe", help="Starts a tictactoe game")
    async def tic(self, ctx, p1: discord.Member, p2: discord.Member):
        global player1
        global player2
        global turn
        global gameOver
        global count
        global db
        global cursor
        global accept1

        if p1 == p2:
            await ctx.send("You can't play against yourself")
            return
        if ctx.author == p1 or ctx.author == p2:
            if gameOver:
                player1 = p1
                player2 = p2
                if p1 == ctx.author:
                    accept1 = player2
                    desc = f"{ctx.author.mention} has challenged {p2.mention} to a match of tictactoe. Do '!accept ttt' to accept"
                    emb = discord.Embed(title="Tictactoe", description=desc, colour=discord.Colour.red())
                    await ctx.send(embed=emb)
                elif p2 == ctx.author:
                    accept1 = player1
                    desc = f"{ctx.author.mention} has challenged {p1.mention} to a match of tictactoe. Do '!accept ttt' to accept"
                    emb = discord.Embed(title="Tictactoe", description=desc, colour=discord.Colour.red())
                    await ctx.send(embed=emb)
        else:
            await ctx.send("You aren't a player")

    @tic.error
    async def tictactoe(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to mention 2 players for this command")

        elif isinstance(error, commands.BadArgument):
            await ctx.send("You need to ping players")

    @commands.group(invoke_without_command=True)
    async def accept(self, ctx):
        await ctx.send("Invalid sub-command")

    @accept.command(aliases=["ttt"], name="tictactoe", help="accepts a match of tictactoe")
    async def _ttt_(self, ctx):
        global gameOver
        global count
        global turn
        global player1
        global player2

        if gameOver:
            if accept1 == ctx.author:
                    global board
                    turn = ""
                    board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                             ":white_large_square:", ":white_large_square:", ":white_large_square:",
                             ":white_large_square:", ":white_large_square:", ":white_large_square:"]
                    gameOver = False
                    count = 0
                    p1 = player1
                    p1: discord.Member
                    cursor.execute(f"SELECT wins FROM wins WHERE id = '{p1.id}'")
                    result = cursor.fetchone()
                    if result is None:
                        userdata = (f'{p1.id}', f"{p1}", 0, 0, 0)
                        sql = ("INSERT INTO wins(id, username, wins, loses, ties) VALUES(?,?,?,?,?)")
                        cursor.execute(sql, userdata)
                        db.commit()
                    else:
                        try:
                            cursor.execute(f"UPDATE wins SET username = {p1} WHERE id = '{p1.id}'")
                            db.commit()
                        except:
                            pass
                    p2 = player2
                    p2: discord.Member
                    cursor.execute(f"SELECT username FROM wins WHERE id = '{p2.id}'")
                    result = cursor.fetchone()
                    if result is None:
                        userdata = (f'{p2.id}', f"{p2}", 0, 0, 0)
                        sql = ("INSERT INTO wins(id, username, wins, loses, ties) VALUES(?,?,?,?,?)")
                        cursor.execute(sql, userdata)
                        db.commit()
                    else:
                        try:
                            cursor.execute(f"UPDATE wins SET username = {p2} WHERE id = '{p2.id}'")
                            db.commit()
                        except:
                            pass
                    
                    await ctx.send(f"""{board[0]}{board[1]}{board[2]}
{board[3]}{board[4]}{board[5]}
{board[6]}{board[7]}{board[8]}""")

                    start = random.randint(1, 2)
                    if start == 1:
                        turn = player1
                        p11 = player1
                        p11: discord.User
                        await ctx.send(f"It's {p11.mention}'s Turn")
                    elif start == 2:
                        turn = player2
                        p21 = player2
                        p21: discord.User
                        await ctx.send(f"It's {p21.mention}'s Turn")

            else:
                await ctx.send("You can't accept")
        elif not gameOver:
            await ctx.send("A game is already in progress")
            return
        else:
            await ctx.send("You can't accept")

    @commands.command(name="place", help="Places a X or O during a tictactoe game")
    async def place(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver
        global db
        global cursor

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if pos < 1 or pos > 9:
                    await ctx.send("Be sure to pick a number between 1 and 9 (including 1 and 9)")

                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1

                    await ctx.send(f"""{board[0]}{board[1]}{board[2]}
{board[3]}{board[4]}{board[5]}
{board[6]}{board[7]}{board[8]}""")

                    checkWinner(winningConditions, mark)
                    if gameOver:
                        await ctx.send(f"{mark} wins!")
                        if mark == ":regional_indicator_x:":
                            p1 = player1
                            p1: discord.Member
                            cursor.execute(f"SELECT wins FROM wins WHERE id = '{p1.id}'")
                            w = cursor.fetchone()
                            wi = str(w).split("(")[1]
                            win = str(wi).split(",")[0]
                            wins = int(win)
                            r = float(wins) + float(1)
                            res = int(r)
                            cursor.execute(f"UPDATE wins SET wins = '{res}' WHERE id = '{p1.id}'")
                            db.commit()
                            p2 = player2
                            p2: discord.Member
                            cursor.execute(f"SELECT loses from wins WHERE id = '{p2.id}'")
                            l = cursor.fetchone()
                            lo = str(l).split("(")[1]
                            lose = str(lo).split(",")[0]
                            loses = int(lose)
                            r3 = float(loses) + float(1)
                            res3 = int(r3)
                            cursor.execute(f"UPDATE wins SET loses = '{res3}' WHERE id = '{p2.id}'")
                            gameOver = True
                            db.commit()
                            db.close()
                        elif mark == ":o2:":
                            p2 = player2
                            p2: discord.Member
                            cursor.execute(f"SELECT wins FROM wins WHERE id = '{p2.id}'")
                            w1 = cursor.fetchone()
                            wi1 = str(w1).split("(")[1]
                            win1 = str(wi1).split(",")[0]
                            wins1 = int(win1)
                            r1 = float(wins1) + float(1)
                            res1 = int(r1)
                            cursor.execute(f"UPDATE wins SET wins = '{res1}' WHERE id = '{p2.id}'")
                            db.commit()
                            p1 = player1
                            p1: discord.Member
                            cursor.execute(f"SELECT loses from wins WHERE id = '{p1.id}'")
                            l1 = cursor.fetchone()
                            lo1 = str(l1).split("(")[1]
                            lose1 = str(lo1).split(",")[0]
                            loses1 = int(lose1)
                            r4 = float(loses1) + float(1)
                            res4 = int(r4)
                            gameOver = True
                            cursor.execute(f"UPDATE wins SET loses = '{res4}' WHERE id = '{p1.id}'")
                            db.commit()
                    elif count >= 9:
                        await ctx.send("The game has resulted in a tie")
                        gameOver = True
                        p1 = player1
                        p1: discord.Member
                        p2 = player2
                        p2: discord.Member
                        cursor.execute(f"SELECT ties FROM wins WHERE id = '{p1.id}'")
                        t = cursor.fetchone()
                        ti = str(t).split("(")[1]
                        tie = str(ti).split(",")[0]
                        ties = int(tie)
                        r = float(ties) + float(1)
                        res = int(r)
                        cursor.execute(f"UPDATE wins SET ties = '{res}' WHERE id = '{p1.id}'")
                        db.commit()
                        cursor.execute(f"SELECT ties FROM wins WHERE id = '{p2.id}'")
                        t1 = cursor.fetchone()
                        ti1 = str(t1).split("(")[1]
                        tie1 = str(ti1).split(",")[0]
                        ties1 = int(tie1)
                        r1 = float(ties1) + float(1)
                        res1 = int(r1)
                        gameOver = True
                        cursor.execute(f"UPDATE wins SET ties = '{res1}' WHERE id = '{p2.id}'")
                        db.commit()
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1

                elif board[pos - 1] == ":o2:" or board[pos - 1] == ":regional_indicator_x:":
                    await ctx.send("Please choose an unmarked tile")

            else:
                await ctx.send("It's not your turn")

        else:
            await ctx.send("There is no game in progress")


    @place.error
    async def place_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position")

        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please put a number between 1 - 9 (including 1 and 9)")


    @commands.command(name="forfeit", help="Forfeits a match of tictactoe")
    async def forfeit(self, ctx):
        global player2
        global player1
        global gameOver
        global mathplayer
        global mathgame
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in ctx.guild.text_channels:
                text_channel_list.append(channel)
        if ctx.channel in text_channel_list:
            if ctx.author == player1 or ctx.author == player2:
                gameOver = True
                user = ctx.author
                user: discord.Member
                if ctx.author == player1:
                    await ctx.send(f"{user.mention} has forfeited the match")
                    cursor.execute(f"SELECT loses FROM wins WHERE id = '{ctx.author.id}'")
                    l1 = cursor.fetchone()
                    lo1 = str(l1).split("(")[1]
                    lose1 = str(lo1).split(",")[0]
                    loses1 = int(lose1)
                    r4 = float(loses1) + float(1)
                    res4 = int(r4)
                    cursor.execute(f"UPDATE wins SET loses = '{res4}' WHERE id = '{ctx.author.id}'")
                    db.commit()
                    p2 = player2
                    p2: discord.Member
                    cursor.execute(f"SELECT wins FROM wins WHERE id = '{p2.id}'")
                    w1 = cursor.fetchone()
                    wi1 = str(w1).split("(")[1]
                    win1 = str(wi1).split(",")[0]
                    wins1 = int(win1)
                    r1 = float(wins1) + float(1)
                    res1 = int(r1)
                    cursor.execute(f"UPDATE wins SET wins = '{res1}' WHERE id = '{p2.id}'")
                    db.commit()
                if ctx.author == player2:
                    await ctx.send(f"@{user} has forfeited the match")
                    cursor.execute(f"SELECT loses FROM wins WHERE id = '{ctx.author.id}'")
                    l1 = cursor.fetchone()
                    lo1 = str(l1).split("(")[1]
                    lose1 = str(lo1).split(",")[0]
                    loses1 = int(lose1)
                    r4 = float(loses1) + float(1)
                    res4 = int(r4)
                    cursor.execute(f"UPDATE wins SET loses = '{res4}' WHERE id = '{ctx.author.id}'")
                    db.commit()
                    p1 = player1
                    p1: discord.Member
                    cursor.execute(f"SELECT wins FROM wins WHERE id = '{p1.id}'")
                    w1 = cursor.fetchone()
                    wi1 = str(w1).split("(")[1]
                    win1 = str(wi1).split(",")[0]
                    wins1 = int(win1)
                    r1 = float(wins1) + float(1)
                    res1 = int(r1)
                    cursor.execute(f"UPDATE wins SET wins = '{res1}' WHERE id = '{p1.id}'")
                    db.commit()
            elif ctx.author == mathplayer:
                await ctx.send("You forfeited the question")
                mathequation = ""
                b = ""
                mathgame = True
                cursor.execute(f"SELECT incorrect FROM mathgame WHERE id = '{ctx.author.id}'")
                c1 = cursor.fetchone()
                cor1 = str(c1).split('(')[1]
                corr1 = str(cor1).split(',')[0]
                corre1 = float(corr1) + float(1)
                correct1 = int(corre1)
                cursor.execute(F"UPDATE mathgame SET incorrect = '{correct1}' WHERE id = '{ctx.author.id}'")
                db.commit()
            else:
                await ctx.send("You are not in a match")

    @commands.command(aliases=['mq'], name="mathquestion", help="A random math question")
    async def mathquestion(self, ctx):
        global db
        global cursor
        global mathequation
        global b
        global mathgame
        global mathplayer
        mathplayer = ctx.author
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in ctx.guild.text_channels:
                text_channel_list.append(channel)
        if ctx.channel in text_channel_list:
            if mathgame:
                cursor.execute(f"SELECT id FROM mathgame WHERE id = '{ctx.author.id}'")
                result = cursor.fetchone()
                if result is None:
                    userdata = (f"{ctx.author.id}", f"{ctx.author}", 0, 0)
                    sql = (f"INSERT INTO mathgame(id, username, correct, incorrect) VALUES(?,?,?,?)")
                    cursor.execute(sql, userdata)
                    db.commit()
                else:
                    try:
                        cursor.execute(f"UPDATE levels SET username = '{ctx.author}' WHERE id = '{ctx.author.id}'")
                        db.commit()
                    except:
                        pass
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                z = random.randint(1, 4)

                if z == 1:
                    a = float(x) + float(y)
                    b = int(a)
                    mathequation = f'{x} + {y} = ?'
                    await ctx.send(mathequation)

                if z == 2:
                    a = float(x) - float(y)
                    b = int(a)
                    mathequation = f'{x} - {y} = ?'
                    await ctx.send(mathequation)

                if z == 3:
                    a = float(x) * float(y)
                    b = int(a)
                    mathequation = f'{x} × {y} = ?'
                    await ctx.send(mathequation)

                if z == 4:
                    a = float(x) / float(y)
                    b = a
                    c = float(b) * float(10)
                    d = round(c)
                    b = float(d) / float(10)
                    mathequation = f'{x} ÷ {y} = ?'
                    await ctx.send(mathequation + "\nNote: You have to roundup your answer to the nearest tenth!")
                mathgame = False
            elif not mathgame:
                await ctx.send("Someone is already attempting a math question")

    @commands.command(aliases=['ma'], name="mathanswer", help="The way to answer mathquestion")
    async def mathanswer(self, ctx, ans: float):
        global b
        global mathequation
        global mathgame
        global mathplayer
        global cursor
        global db
        float(b)
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in ctx.guild.text_channels:
                text_channel_list.append(channel)
        if ctx.channel in text_channel_list:
            if ctx.author == mathplayer:
                mp = mathplayer
                mp: discord.Member
                if ans == b or b == ans:
                    await ctx.send("Answer correct!")
                    mathequation = ""
                    b = ""
                    mathgame = True
                    cursor.execute(f"SELECT correct FROM mathgame WHERE id = '{mp.id}'")
                    c = cursor.fetchone()
                    cor = str(c).split('(')[1]
                    corr = str(cor).split(',')[0]
                    corre = float(corr) + float(1)
                    correct = int(corre)
                    cursor.execute(F"UPDATE mathgame SET correct = '{correct}' WHERE id = '{mp.id}'")
                    db.commit()
                else:
                    await ctx.send("Answer incorrect")
                    mathequation = ""
                    b = ""
                    mathgame = True
                    cursor.execute(f"SELECT incorrect FROM mathgame WHERE id = '{mp.id}'")
                    c1 = cursor.fetchone()
                    cor1 = str(c1).split('(')[1]
                    corr1 = str(cor1).split(',')[0]
                    corre1 = float(corr1) + float(1)
                    correct1 = int(corre1)
                    cursor.execute(F"UPDATE mathgame SET incorrect = '{correct1}' WHERE id = '{mp.id}'")
                    db.commit()
            else:
                await ctx.send("You are not the player")

    @commands.command(aliases=["diceroll", 'dr'], name="dice_roll", help="Rolls 1-6 dice!")
    async def dice_roll(self, ctx, dicenumber=1):
        if dicenumber <= 0:
            await ctx.send("You can't roll less than 1 dice")

        if dicenumber > 6:
            await ctx.send("You can't roll more than 6 dice")

        if dicenumber == 1:
            dice = random.randint(1, 6)
            if dice == 1:
                emb = discord.Embed(title="Dice Roll:", description=f""":white_large_square::white_large_square::white_large_square:
                                                                        :white_large_square::red_square::white_large_square:
                                                                        :white_large_square::white_large_square::white_large_square:""")
                await ctx.send(embed=emb)
            if dice == 2:
                emb = discord.Embed(title="Dice Roll:", description=f""":red_square::white_large_square::white_large_square:
                                                                        :white_large_square::red_square::white_large_square:
                                                                        :white_large_square::white_large_square::white_large_square:""")
                await ctx.send(embed=emb)
            if dice == 3:
                emb = discord.Embed(title="Dice Roll:", description=f""":red_square::white_large_square::white_large_square:
                                                                        :white_large_square::red_square::white_large_square:
                                                                        :white_large_square::white_large_square::red_square:""")
                await ctx.send(embed=emb)
            if dice == 4:
                emb = discord.Embed(title="Dice Roll:", description=f""":red_square::white_large_square::red_square:
                                                                        :white_large_square::white_large_square::white_large_square:
                                                                        :red_square::white_large_square::red_square:""")
                await ctx.send(embed=emb)
            if dice == 5:
                emb = discord.Embed(title="Dice Roll:", description=f""":red_square::white_large_square::red_square:
                                                                        :white_large_square::red_square::white_large_square:
                                                                        :red_square::white_large_square::red_square:""")
                await ctx.send(embed=emb)
            if dice == 6:
                emb = discord.Embed(title="Dice Roll:", description=f""":red_square::white_large_square::red_square:
                                                                        :red_square::white_large_square::red_square:
                                                                        :red_square::white_large_square::red_square:""")
                await ctx.send(embed=emb)
        if dicenumber == 2:
            dice = random.randint(1, 6)
            dice1 = random.randint(1, 6)
            if dice == 1:
                display = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice == 2:
                display = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice == 3:
                 display = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice == 4:
                display = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice == 5:
                display = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice == 6:
                display = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 1:
                display1 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 2:
                display1 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 3:
                 display1 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice1 == 4:
                display1 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice1 == 5:
                display1 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 6:
                display1 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            emb = discord.Embed(title="Dice Roll")
            emb.add_field(name="Dice 1:", value=display, inline=True)
            emb.add_field(name="Dice 2:", value=display1, inline=True)
            await ctx.send(embed=emb)
        if dicenumber == 3:
            dice = random.randint(1, 6)
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice == 1:
                display = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice == 2:
                display = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice == 3:
                 display = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice == 4:
                display = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice == 5:
                display = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice == 6:
                display = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 1:
                display1 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 2:
                display1 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 3:
                 display1 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice1 == 4:
                display1 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice1 == 5:
                display1 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 6:
                display1 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 1:
                display2 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 2:
                display2 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 3:
                 display2 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice2 == 4:
                display2 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice2 == 5:
                display2 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 6:
                display2 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            emb = discord.Embed(title="Dice Roll")
            emb.add_field(name="Dice 1:", value=display, inline=True)
            emb.add_field(name="Dice 2:", value=display1, inline=True)
            emb.add_field(name="Dice 3:", value=display2, inline=True)
            await ctx.send(embed=emb)
        if dicenumber == 4:
            dice = random.randint(1, 6)
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)
            if dice == 1:
                display = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice == 2:
                display = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice == 3:
                 display = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice == 4:
                display = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice == 5:
                display = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice == 6:
                display = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 1:
                display1 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 2:
                display1 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 3:
                 display1 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice1 == 4:
                display1 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice1 == 5:
                display1 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 6:
                display1 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 1:
                display2 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 2:
                display2 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 3:
                 display2 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice2 == 4:
                display2 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice2 == 5:
                display2 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 6:
                display2 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice3 == 1:
                display3 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice3 == 2:
                display3 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice3 == 3:
                 display3 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice3 == 4:
                display3 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice3 == 5:
                display3 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice3 == 6:
                display3 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            emb = discord.Embed(title="Dice Roll")
            emb.add_field(name="Dice 1:", value=display, inline=True)
            emb.add_field(name="Dice 2:", value=display1, inline=True)
            emb.add_field(name="Dice 3:", value=display2, inline=True)
            emb.add_field(name="Dice 4:", value=display3, inline=True)
            await ctx.send(embed=emb)

        if dicenumber == 5:
            dice = random.randint(1, 6)
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)
            dice4 = random.randint(1, 6)
            if dice == 1:
                display = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice == 2:
                display = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice == 3:
                 display = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice == 4:
                display = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice == 5:
                display = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice == 6:
                display = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 1:
                display1 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 2:
                display1 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 3:
                 display1 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice1 == 4:
                display1 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice1 == 5:
                display1 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 6:
                display1 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 1:
                display2 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 2:
                display2 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 3:
                 display2 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice2 == 4:
                display2 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice2 == 5:
                display2 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 6:
                display2 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice3 == 1:
                display3 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice3 == 2:
                display3 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice3 == 3:
                 display3 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice3 == 4:
                display3 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice3 == 5:
                display3 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice3 == 6:
                display3 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice4 == 1:
                display4 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice4 == 2:
                display4 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice4 == 3:
                 display4 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice4 == 4:
                display4 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice4 == 5:
                display4 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice4 == 6:
                display4 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            emb = discord.Embed(title="Dice Roll")
            emb.add_field(name="Dice 1:", value=display, inline=True)
            emb.add_field(name="Dice 2:", value=display1, inline=True)
            emb.add_field(name="Dice 3:", value=display2, inline=True)
            emb.add_field(name="Dice 4:", value=display3, inline=True)
            emb.add_field(name="Dice 5:", value=display4, inline=True)
            await ctx.send(embed=emb)
        if dicenumber == 6:
            dice = random.randint(1, 6)
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)
            dice4 = random.randint(1, 6)
            dice5 = random.randint(1, 6)
            if dice == 1:
                display = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice == 2:
                display = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice == 3:
                 display = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice == 4:
                display = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice == 5:
                display = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice == 6:
                display = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 1:
                display1 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 2:
                display1 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice1 == 3:
                 display1 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice1 == 4:
                display1 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice1 == 5:
                display1 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice1 == 6:
                display1 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 1:
                display2 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 2:
                display2 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice2 == 3:
                 display2 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice2 == 4:
                display2 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice2 == 5:
                display2 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice2 == 6:
                display2 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice3 == 1:
                display3 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice3 == 2:
                display3 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice3 == 3:
                 display3 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice3 == 4:
                display3 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice3 == 5:
                display3 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice3 == 6:
                display3 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice4 == 1:
                display4 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice4 == 2:
                display4 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice4 == 3:
                 display4 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice4 == 4:
                display4 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice4 == 5:
                display4 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice4 == 6:
                display4 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            if dice5 == 1:
                display5 = """:white_large_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                :white_large_square::white_large_square::white_large_square:"""
            if dice5 == 2:
                display5 = """:red_square::white_large_square::white_large_square:
                                :white_large_square::red_square::white_large_square:
                                 :white_large_square::white_large_square::white_large_square:"""
            if dice5 == 3:
                 display5 = """:red_square::white_large_square::white_large_square:
                                    :white_large_square::red_square::white_large_square:
                                    :white_large_square::white_large_square::red_square:"""
            if dice5 == 4:
                display5 = """:red_square::white_large_square::red_square:
                       :white_large_square::white_large_square::white_large_square:
                        :red_square::white_large_square::red_square:"""
            if dice5 == 5:
                display5 = """:red_square::white_large_square::red_square:
                                :white_large_square::red_square::white_large_square:
                                :red_square::white_large_square::red_square:"""
            if dice5 == 6:
                display5 = """:red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:
                                :red_square::white_large_square::red_square:"""
            emb = discord.Embed(title="Dice Roll")
            emb.add_field(name="Dice 1:", value=display, inline=True)
            emb.add_field(name="Dice 2:", value=display1, inline=True)
            emb.add_field(name="Dice 3:", value=display2, inline=True)
            emb.add_field(name="Dice 4:", value=display3, inline=True)
            emb.add_field(name="Dice 5:", value=display4, inline=True)
            emb.add_field(name="Dice 6:", value=display5, inline=True)
            await ctx.send(embed=emb)

    @commands.group(invoke_without_command=True, name="rank", help="Shows your level")
    async def rank(self, ctx):
        cursor.execute(f"SELECT xp FROM levels WHERE id = '{ctx.author.id}'")
        result = cursor.fetchone()
        if result is None:
            userdata = (f"{ctx.author.id}", 0)
            sql = ("INSERT INTO levels(id, xp) VALUES(?,?)")
            cursor.execute(sql, userdata)
            db.commit()
            cursor.execute(f"SELECT xp FROM levels WHERE id = '{ctx.author.id}'")
            a = cursor.fetchone()
            result = str(a).split('(')[1]
            result2 = str(result).split(',')[0]
            xp = int(result2)
            lvl = float(xp) / float(100)
            cursor.execute(f"SELECT * FROM levels")
            b = cursor.fetchall()
            cursor.execute(f"SELECT * FROM levels WHERE id = '{ctx.author.id}'")
            c = cursor.fetchone()
            rank = 0
            for x in b:
                rank +=1
                if x == c:
                    break
            emb = discord.Embed(title="Rank", colour=discord.Colour.orange())
            emb.add_field(name="Name:", value=ctx.author.mention, inline=True)
            emb.add_field(name="Level:", value=int(lvl), inline=True)
            emb.add_field(name="Rank:", value=rank, inline=True)
            await ctx.send(embed=emb)
        else:
            cursor.execute(f"SELECT xp FROM levels WHERE id = '{ctx.author.id}'")
            a = cursor.fetchone()
            result = str(a).split('(')[1]
            result2 = str(result).split(',')[0]
            xp = int(result2)
            lvl = float(xp) / float(100)
            cursor.execute(f"SELECT xp FROM levels")
            b = cursor.fetchall()
            cursor.execute(f"SELECT xp FROM levels WHERE id = '{ctx.author.id}'")
            c = cursor.fetchone()
            result3 = str(c).split('(')[1]
            result4 = str(result3).split(',')[0]
            userlvl = int(result4)
            rank = 0
            lists = 0
            e = []
            lengthb = len(b)
            while lists < lengthb:
                lists += 1
                y = random.choice(b)
                result5 = str(y).split('(')[1]
                result6 = str(result5).split(',')[0]
                cool = int(result6)
                e.append(cool)
                b.remove(y)
            e.sort(reverse=True)
            for x in e:
                rank +=1
                if x == userlvl:
                    break
            leftover = str(lvl).split(f'{str(int(lvl))}.')
            leftover.pop(0)
            lfo = leftover.pop(0)
            lo = int(lfo)
            if lo < 20:
                 progessbar = ':white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:'
            if 20 <= lo < 40:
                progessbar = ':blue_square::white_large_square::white_large_square::white_large_square::white_large_square:'
            if 40 <= lo < 60:
                progessbar = ':blue_square::blue_square::white_large_square::white_large_square::white_large_square:'
            if 60 <= lo < 80:
                progessbar = ':blue_square::blue_square::blue_square::white_large_square::white_large_square:'
            if 80 <= lo < 90:
                progessbar = ':blue_square::blue_square::blue_square::blue_square::white_large_square:'
            if 90 <= lo <= 99:
                progessbar = ':blue_square::blue_square::blue_square::blue_square::blue_square:'


            emb =discord.Embed(title="Rank", colour=discord.Colour.orange())
            emb.add_field(name="Name:", value=ctx.author.mention, inline=True)
            emb.add_field(name="Level:", value=int(lvl), inline=True)
            emb.add_field(name="Rank:", value=rank, inline=True)
            emb.add_field(name="Progress Bar", value=progessbar, inline=False)
            emb.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=emb)

    @rank.command(aliases=['ttt'], name="tictactoe", help="Shows your stats for tictactoe")
    async def _tictactoe(self, ctx):
        db = sqlite3.connect('main.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM wins WHERE id = '{ctx.author.id}'")
        result = cursor.fetchone()
        if result is None:
            userdata = (f'{ctx.author.id}', f'{ctx.author}', 0, 0, 0)
            sql = ("INSERT INTO wins(id, username, wins, loses, ties) VALUES(?,?,?,?,?)")
            cursor.execute(sql, userdata)
            db.commit()
            cursor.execute(f"SELECT wins FROM wins WHERE id = '{ctx.author.id}'")
            w = cursor.fetchone()
            wi = str(w).split('(')[1]
            win = str(wi).split(',')[0]
            wins = int(win)
            cursor.execute(f"SELECT loses FROM wins WHERE id = '{ctx.author.id}'")
            l = cursor.fetchone()
            lo = str(l).split('(')[1]
            lose = str(lo).split(',')[0]
            loses = int(lose)
            cursor.execute(f"SELECT ties FROM wins WHERE id = '{ctx.author.id}'")
            t = cursor.fetchone()
            ti = str(t).split('(')[1]
            tie = str(ti).split(',')[0]
            ties = int(tie)
            emb = discord.Embed(title="Tictactoe Stats", colour=discord.Colour.red())
            emb.add_field(name="Name:", value=ctx.author.mention, inline=False)
            emb.add_field(name="Wins:", value=wins, inline=False)
            emb.add_field(name="Loses:", value=loses, inline=False)
            emb.add_field(name="Ties:", value=ties, inline=False)
            emb.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            cursor.execute(f"SELECT wins FROM wins WHERE id = '{ctx.author.id}'")
            w = cursor.fetchone()
            wi = str(w).split('(')[1]
            win = str(wi).split(',')[0]
            wins = int(win)
            cursor.execute(f"SELECT loses FROM wins WHERE id = '{ctx.author.id}'")
            l = cursor.fetchone()
            lo = str(l).split('(')[1]
            lose = str(lo).split(',')[0]
            loses = int(lose)
            cursor.execute(f"SELECT ties FROM wins WHERE id = '{ctx.author.id}'")
            t = cursor.fetchone()
            ti = str(t).split('(')[1]
            tie = str(ti).split(',')[0]
            ties = int(tie)
            emb = discord.Embed(title="Tictactoe Stats", colour=discord.Colour.red())
            emb.add_field(name="Name:", value=ctx.author.mention, inline=False)
            emb.add_field(name="Wins:", value=wins, inline=False)
            emb.add_field(name="Loses:", value=loses, inline=False)
            emb.add_field(name="Ties:", value=ties, inline=False)
            emb.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=emb)

    @rank.command(aliases=['mq'], name="mathquestion", help="Shows your stats for the math game")
    async def _mathquestion(self, ctx):
        global db
        global cursor
        cursor.execute(f"SELECT id FROM mathgame WHERE id = '{ctx.author.id}'")
        result = cursor.fetchone()
        if result is None:
            userdata = (f"{ctx.author.id}", f"{ctx.author}", 0, 0)
            sql = (f"INSERT INTO mathgame(id, username, correct, incorrect) VALUES(?,?,?,?)")
            cursor.execute(sql, userdata)
            db.commit()
            cursor.execute(f"SELECT correct FROM mathgame WHERE id = '{ctx.author.id}'")
            c = cursor.fetchone()
            co = str(c).split('(')[1]
            cor = str(co).split(',')[0]
            correct = int(cor)
            cursor.execute(f"SELECT incorrect FROM mathgame WHERE id = '{ctx.author.id}'")
            inc = cursor.fetchone()
            inco = str(inc).split('(')[1]
            incor = str(inco).split(',')[0]
            incorrect = int(incor)
            emb = discord.Embed(title="Math Game Score", color=discord.Color.blue())
            emb.add_field(name="Name:", value=ctx.author.mention, inline=True)
            emb.add_field(name="Wins:", value=correct, inline=True)
            emb.add_field(name="Loses:", value=incorrect, inline=True)
            emb.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            cursor.execute(f"UPDATE mathgame SET username = '{ctx.author}' WHERE id = '{ctx.author.id}'")
            db.commit()
            cursor.execute(f"SELECT correct FROM mathgame WHERE id = '{ctx.author.id}'")
            c = cursor.fetchone()
            co = str(c).split('(')[1]
            cor = str(co).split(',')[0]
            correct = int(cor)
            cursor.execute(f"SELECT incorrect FROM mathgame WHERE id = '{ctx.author.id}'")
            inc = cursor.fetchone()
            inco = str(inc).split('(')[1]
            incor = str(inco).split(',')[0]
            incorrect = int(incor)
            emb = discord.Embed(title="Math Game Score", color=discord.Color.blue())
            emb.add_field(name="Name:", value=ctx.author.mention, inline=False)
            emb.add_field(name="Correct Answers:", value=correct, inline=False)
            emb.add_field(name="Incorrect Answers:", value=incorrect, inline=False)
            emb.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=emb)


    @commands.group(invoke_without_command=True, aliases=['lb'], name="leaderboard", help="The level leaderboard")
    async def leaderboard(self, ctx):
        global cursor
        global db
        cursor.execute(f"SELECT xp FROM levels")
        b = cursor.fetchall()
        rank = 0
        r = 0
        e = []
        lengthb = len(b)
        while r < lengthb:
            r += 1
            y = b.pop(0)
            result = str(y).split('(')[1]
            result2 = str(result).split(',')[0]
            cool = int(result2)
            e.append(cool)
        e.sort(reverse=True)
        f = []
        while rank < 10:
            rank += 1
            try:
                z = e.pop(0)
            except:
                z = None
                pass
            f.append(z)
            if rank == 1:
                num1 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num1}'")
                num1fetch = cursor.fetchone()
                num1r = str(num1fetch).split('(')[1]
                l1 = str(num1r).split(',')[0]
            if rank == 2:
                num2 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num2}'")
                num2fetch = cursor.fetchone()
                num2r = str(num2fetch).split('(')[1]
                l2 = str(num2r).split(',')[0]
            if rank == 3:
                num3 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num3}'")
                num3fetch = cursor.fetchone()
                num3r = str(num3fetch).split('(')[1]
                l3 = str(num3r).split(',')[0]
            if rank == 4:
                num4 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num4}'")
                num4fetch = cursor.fetchone()
                num4r = str(num4fetch).split('(')[1]
                l4 = str(num4r).split(',')[0]
            if rank == 5:
                num5 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num5}'")
                num5fetch = cursor.fetchone()
                num5r = str(num5fetch).split('(')[1]
                l5 = str(num5r).split(',')[0]
            if rank == 6:
                num6 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num6}'")
                num6fetch = cursor.fetchone()
                num6r = str(num6fetch).split('(')[1]
                l6 = str(num6r).split(',')[0]
            if rank == 7:
                num7 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num7}'")
                num7fetch = cursor.fetchone()
                num7r = str(num7fetch).split('(')[1]
                l7 = str(num7r).split(',')[0]
            if rank == 8:
                num8 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num8}'")
                num8fetch = cursor.fetchone()
                num8r = str(num8fetch).split('(')[1]
                l8 = str(num8r).split(',')[0]
            if rank == 9:
                num9 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num9}'")
                num9fetch = cursor.fetchone()
                num9r = str(num9fetch).split('(')[1]
                l9 = str(num9r).split(',')[0]
            if rank == 10:
                num10 = z
                cursor.execute(f"SELECT username FROM levels WHERE xp = '{num10}'")
                num10fetch = cursor.fetchone()
                num10r = str(num10fetch).split('(')[1]
                l10 = str(num10r).split(',')[0]
        p1 = f"1: {l1}, XP: {num1}, LEVEL: {int(num1 / 100)}"
        p2 = f"2: {l2}, XP: {num2}, LEVEL: {int(num2 / 100)}"
        p3 = f"3: {l3}, XP: {num3}, LEVEL: {int(num3 / 100)}"
        p4 = f"4: {l4}, XP: {num4}, LEVEL: {int(num4 / 100)}"
        p5 = f"5: {l5}, XP: {num5}, LEVEL: {int(num5 / 100)}"
        p6 = f"6: {l6}, XP: {num6}, LEVEL: {int(num6 / 100)}"
        p7 = f"7: {l7}, XP: {num7}, LEVEL: {int(num7 / 100)}"
        p8 = f"8: {l8}, XP: {num8}, LEVEL: {int(num8 / 100)}"
        p9 = f"9: {l9}, XP: {num9}, LEVEL: {int(num9 / 100)}"
        p10 = f"10: {l10}, XP: {num10}, LEVEL: {int(num10 / 100)}"
        emb = discord.Embed(title="Level Leaderboard", description=f"{p1}\n{p2}\n{p3}\n{p4}\n{p5}\n{p6}\n{p7}\n{p8}\n{p9}\n{p10}", colour=discord.Colour.purple())
        await ctx.send(embed=emb)

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

def setup(client):
    client.add_cog(Game_Cmds(client))