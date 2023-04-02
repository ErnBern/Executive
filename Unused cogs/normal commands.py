import discord, random, platform
from discord.ext import commands

class Normal_Cmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Normal_Cmds Cog is ready')

    @commands.command(name='executive', help='Tells you if Executive is online')
    async def executive(self, ctx):
        await ctx.send("Here")

    @commands.command(name="quote", help="Sends a random quote")
    async def quote(self, ctx):
        q = [
            "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion'.- Muhammad Ali",
            "I've been poor and I've been rich, and rich is better. - Bessie Smith",
            "What is love? ... It is the morning and the evening star. - Sinclair Lewis",
            "We want far better reasons for having children than ... knowing how to prevent them. - Dora Russell",
            "A good plan implemented today is better than a perfect plan implemented tomorrow. - General George Smith Patton",
            "You cannot help men permanently by doing for them what they could and should do for themselves. - Abraham Lincoln",
            "A politician is an animal which can sit on a fence and yet keep both ears to the ground. - H. L. Mencken",
            "Cruelty, like every other vice, requires no motive outside of itself; it only requires opportunity. - George Eliot",
            "Part of the inhumanity of the computer is that, once it is competently programmed and working smoothly, it is completely honest. - Isaac Asimov",
            "You will become as small as your controlling desire; as great as your dominant aspiration. - James Allen",
            "There are two ways of spreading light: to be the candle or the mirror that reflects it. - Edith Wharton",
            "Bore: n. a person who talks when you wish him to listen. -  Ambrose Gwinett Bierce",
            "All you have to do to be a millionaire, is earn a million dollars. - Noah Amy",
            "Who overrefines his argument brings himself to grief. -Francesco Petrarca Petrarch",
            "Theatre director: a person engaged by the management to conceal the fact that the players cannot act. -James Agate",
            "It always seems impossible until it's done. - Nelson Mandela"
            ]
        quotes = random.choice(q)
        if quotes == "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion'.- Muhammad Ali":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTQ3NjYxMzk4NjkwNzY4NDkz/muhammad_ali_photo_by_stanley_weston_archive_photos_getty_482857506.jpg")
            await ctx.send(embed=emb)
        if quotes == "I've been poor and I've been rich, and rich is better. - Bessie Smith":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRyZ4A3ZMGxmdJCTCQSi2FLDoI4zMNVqmUzTXg0FbunQ0EFkzB1")
            await ctx.send(embed=emb)
        if quotes == "What is love? ... It is the morning and the evening star. - Sinclair Lewis":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://cdn.britannica.com/65/10265-004-33F7388B/Sinclair-Lewis.jpg")
            await ctx.send(embed=emb)
        if quotes == "We want far better reasons for having children than ... knowing how to prevent them. - Dora Russell":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://spartacus-educational.com/TUrussellD.jpg")
            await ctx.send(embed=emb)
        if quotes == "A good plan implemented today is better than a perfect plan implemented tomorrow. - General George Smith Patton":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/2/2f/General_George_S_Patton.jpg")
            await ctx.send(embed=emb)
        if quotes == "You cannot help men permanently by doing for them what they could and should do for themselves. - Abraham Lincoln":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg")
            await ctx.send(embed=emb)
        if quotes == "A politician is an animal which can sit on a fence and yet keep both ears to the ground. - H. L. Mencken":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://i.guim.co.uk/img/media/6883ccf966c87c85b5fd95ea3e0ac66f615ea3a3/0_356_2336_1401/master/2336.jpg?width=620&quality=85&auto=format&fit=max&s=b4c0ea6d3205b3a2650f1ccdb2744a77")
            await ctx.send(embed=emb)
        if quotes == "Cruelty, like every other vice, requires no motive outside of itself; it only requires opportunity. - George Eliot":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/4/48/George_Eliot%2C_por_Fran%C3%A7ois_D%27Albert_Durade.jpg")
            await ctx.send(embed=emb)
        if quotes == "Part of the inhumanity of the computer is that, once it is competently programmed and working smoothly, it is completely honest. - Isaac Asimov":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTg1MjM2NDkyMzg0MjE2NzIz/gettyimages-3240525jpg--.jpg")
            await ctx.send(embed=emb)
        if quotes == "You will become as small as your controlling desire; as great as your dominant aspiration. - James Allen":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcRBcIg3IpARXzFal8tyIN5a9QvPXyI9nKayKm6zKSPCjiYpVtfJ_K-UFJFp02kc")
            await ctx.send(embed=emb)
        if quotes == "There are two ways of spreading light: to be the candle or the mirror that reflects it. - Edith Wharton":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/5/52/Edith_Newbold_Jones_Wharton_%28cropped_02%29.jpg")
            await ctx.send(embed=emb)
        if quotes == "Bore: n. a person who talks when you wish him to listen. -  Ambrose Gwinett Bierce":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/d/da/Ambrose_Bierce_1892-10-07.jpg")
            await ctx.send(embed=emb)
        if quotes == "All you have to do to be a millionaire, is earn a million dollars. - Noah Amy":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/497937146188005377/950555695936315393/CA5327F0-EB69-45C5-8901-0046E22B840E.jpg")
            await ctx.send(embed=emb)
        if quotes == "Theatre director: a person engaged by the management to conceal the fact that the players cannot act. -James Agate":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://www.theatermania.com/s/tm-photos-production/100196.jpg")
            await ctx.send(embed=emb)
        if quotes == "It always seems impossible until it's done. - Nelson Mandela":
            emb = discord.Embed(title="Quote:", description=quotes)
            emb.set_thumbnail(url="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTY2MzU2NjgxMDUwMDM5OTk5/_photo-by-per-anders-petterssongetty-images.jpg")
            await ctx.send(embed=emb)

    @commands.command(name="coinflip", help="Just a coinflip but in discord")
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails"]
        rancoin = random.choice(choices)
        if rancoin == "Heads":
            emb = discord.Embed(title="Heads!")
        if rancoin == "Tails":
            emb = discord.Embed(title="Tails!")
        await ctx.send(embed=emb)

    @commands.command(aliases=['8ball', '8_ball', '8b'], name='eightball', help="It's like an eightball but in Discord")
    async def eightball(self, ctx, *, question):
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
                     "Very doubtful.", "Without a doubt.",
                     "Yes.", "Yes – definitely.", "You may rely on it.",
                     "I don't know but I do know that you should subscribe to Think Cyber!"]

        emb = discord.Embed(title="Eightball")
        emb.add_field(name="Question:", value=question, inline=True)
        emb.add_field(name="Response:", value=random.choice(responses), inline=True)
        emb.set_thumbnail(url="https://magic-8ball.com/wp-content/themes/astra-child/assets/images/magicBallStart.webp")
        await ctx.send(embed=emb)

    @eightball.error
    async def eightball_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send("You don't have a question") 


    @commands.command(aliases=['punchline', 'pl'], name="punch_line", help='Sends a random joke with a punchline')
    async def punch_line(self, message):
        punch_lines = ["Q: Why are balloons so expensive? A: Inflation.",
                       "Q: What do you call cheese that isn’t yours? A: Nacho cheese!",
                       "Q: What side of a tree grows the most branches? A: The outside!",
                       "Q: Why did an old man fall in a well? A: Because he couldn’t see that well!",
                       "Q: What do you call a fish with no eye? A: A fsh.",
                       "Q: What breed of dog can jump higher than a skyscraper? A: Any breed of dog. Skyscrapers can’t jump.",
                       "Q: Why are elevator jokes so good? A: They work on many levels.",
                       "Q: Why are peppers the best at archery? A: Because they habanero.",
                       "Q: Why did the computer get mad at the printer? A: Because it didn’t like its toner voice.",
                       "Q: Why is Peter Pan always flying? A: Because he Neverlands.",
                       "Q: What did the three-legged dog say when he walked into a saloon?A: “I’m looking for the man who shot my paw.”",
                       "Q: What’s the best way to watch a fly-fishing tournament? A: Live stream it.",
                       "Q: Why did the broom decide to go to bed? A: It was very sweepy.",
                       "Q: Why are nurses always running out of red crayons? A: Because they often have to draw blood.",
                       "Q: Why are abortion jokes offensive? A: Because they leave an empty feeling inside"]
        punch_line = random.choice(punch_lines)
        laugh = random.randint(1, 5)
        if laugh == 1:
            emb = discord.Embed(title="Punch Line:", description=punch_line)
            emb.set_thumbnail(url="https://i0.wp.com/antidotesforchimps.com/wp-content/uploads/2019/05/86fe066b8ed2eab07a9392a63db4625b.jpg?w=800&ssl=1")
            await message.send(embed=emb)
        if laugh == 2:
            emb = discord.Embed(title="Punch Line:", description=punch_line)
            emb.set_thumbnail(url="https://images.unsplash.com/photo-1586474714722-d1f9e551cf34?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")
            await message.send(embed=emb)
        if laugh == 3:
            emb = discord.Embed(title="Punch Line:", description=punch_line)
            emb.set_thumbnail(url="https://d2rd7etdn93tqb.cloudfront.net/wp-content/uploads/2018/07/girl-laughing-article-071318.jpg")
            await message.send(embed=emb)
        if laugh == 4:
            emb = discord.Embed(title="Punch Line:", description=punch_line)
            emb.set_thumbnail(url="https://i0.wp.com/digest.bps.org.uk/wp-content/uploads/2016/05/b61eb-thinkstockphotos-92134543.jpg?ssl=1")
            await message.send(embed=emb)
        if laugh == 5:
            emb = discord.Embed(title="Punch Line:", description=punch_line)
            emb.set_thumbnail(url="https://c.tenor.com/-B859OUddZIAAAAC/crying-laughing.gif")
            await message.send(embed=emb)
    
    @commands.command(name='joke', help='Sends a random joke')
    async def joke(self, message):
        jokes = ["I don't trust stairs. They're always up to something",
                 "A guy walked into a bar and lost the limbo contest",
                 "I had a dream that I weighed less than a thousandth of a gram. I was like, 0mg.",
                 "Mom said I should do lunges to stay in shape. That would be a big step forward.",
                 "Every time I take my dog to the park, the ducks try to bite him. That’s what I get for buying a pure bread dog.",
                 "6:30 is my favorite time of day, hands down.",
                 "Mom is mad at me because she asked me to sync her phone, so I threw it in the ocean.",
                 "I wanted to eat a watch for lunch, but it was too time-consuming.",
                 "I’m friends with almost all the letters of the alphabet. I just don’t know Y.",
                 "Justice is a dish best served cold. If it were served warm, it would be justwater.",
                 "I used to hate facial hair, but then it grew on me.",
                 "We’re renovating the house, and the first floor is going great, but the second floor is another story.",
                 "It’s raining cats and dogs, so be careful not to step in a poodle.",
                 "At first, I thought my chiropractor wasn’t any good, but now I stand corrected.",
                 "My toddler is refusing to nap. He’s guilty of resisting a rest.",
                 "I used to be able to play piano by ear, but now I have to use my hands.",
                 "Every night, I have a hard time remembering something, but then it dawns on me.",
                 "The wedding was so beautiful, even the cake was in tiers."]
        joke = random.choice(jokes)
        laugh = random.randint(1, 5)
        if laugh == 1:
            emb = discord.Embed(title="Joke:", description=joke)
            emb.set_thumbnail(url="https://cms.qz.com/wp-content/uploads/2016/07/rtx2c9ws.jpg?quality=75&strip=all&w=1600&h=900")
            await message.send(embed=emb)
        if laugh == 2:
            emb = discord.Embed(title="Joke:", description=joke)
            emb.set_thumbnail(url="https://www.thelist.com/img/gallery/the-weird-reason-you-laugh-after-getting-tickled/why-we-laugh-when-someone-tickles-us-1617641616.jpg")
            await message.send(embed=emb)
        if laugh == 3:
            emb = discord.Embed(title="Joke:", description=joke)
            emb.set_thumbnail(url="https://thumbs.dreamstime.com/z/laughing-tears-pointing-emoticon-wiping-away-something-someone-his-other-hand-85083127.jpg")
            await message.send(embed=emb)
        if laugh == 4:
            emb = discord.Embed(title="Joke:", description=joke)
            emb.set_thumbnail(url="https://scontent.fyyc2-1.fna.fbcdn.net/v/t1.18169-9/10391710_192418088322_4279302_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=174925&_nc_ohc=rLx-UJgYm1IAX_T7CqE&_nc_ht=scontent.fyyc2-1.fna&oh=00_AT85rgOEkDOYsGyOyOGo0jM0cFDvETENKEM__S859hkPzw&oe=624B1A57")
            await message.send(embed=emb)
        if laugh == 5:
            emb = discord.Embed(title="Joke:", description=joke)
            emb.set_thumbnail(url="https://www.nydailynews.com/resizer/b4-X-EjxRHa0N4VMvLYKhNER8wo=/800x530/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/HKNQL2Q4A7KR6EUUFUSPKKVUH4.jpg")
            await message.send(embed=emb)
    
    @commands.command(name='fact', help='Sends a random fact')
    async def fact(self, ctx):
        facts = ["Cybercrime is up 600% due to the COVID-19 pandemic",
                 "Remote work has increased the average cost of a data breach by $137,000",
                 "More than half a million Zoom user accounts were compromised and sold on the dark web",
                 "There are 11,762 recorded breaches between January 1, 2005 and May 31 2020",
                 "In 2020, the average time to identify a breach was 207 days",
                 "43% of cyberattacks target small businesses",
                 "$3.86 million is the global average cost of a data breach",
                 "95% of cybersecurity breaches are a result of human error",
                 "On average only 5% of companies folders are properly protected",
                 "94% of malware is delivered via email",
                 "Only 16% of executives say their organizations are well prepared to deal with cyber risk",
                 "Over 77% of organizations do not have a cyber security incident response plan",
                 "89% of healthcare organizations experienced a data breach in the past two years",
                 "Healthcare cybersecurity breaches cost the most of any other industry",
                 "Over 6,000 new computer viruses are created and released every month",
                 "90% of emails contain some form of malware!", "The Firefox logo isn’t a fox… it’s a red panda!",
                 "Samsung is 38 years and 1 month older than Apple.",
                 "One Petabyte (PB) = 1024 (TB). To put this in perspective, a 50PB hard drive could hold the entire written works of mankind from the beginning of recorded history in all languages.",
                 "Alexa is always listening to your conversations. Alexa stores all of your dialogue history in the cloud to improve the Alexa experience.",
                 "On average, people read 10% slower from a screen than from paper.",
                 "The first computer mouse was made in 1964 by Doug Engelbart. It was rectangular and made from wood!",
                 "On average, there is only one reply per 12 million spam emails sent.",
                 "Surgeons that grew up playing video games more than three hours per week make 37% fewer errors and have a 42% faster completion rate when performing laparoscopic surgery and suturing.",
                 "NASA’s internet speed is 91 GB per second",
                 "Until 2010, carrier pigeons were faster than the internet",
                 "In 1971, the first ever computer virus was developed named Creeper it was made as an experiment just to see how it spread between computers. The virus simply displayed the message: I’m the creeper, catch me if you can!",
                 "Think Cyber Joined Youtube On January 14th, 2022",
                 "The worldwide information security market is forecast to reach $170.4 billion in 2022",
                 "88% of organizations worldwide experienced spear phishing attempts in 2019",
                 "68% of business leaders feel their cybersecurity risks are increasing",
                 "Data breaches exposed 36 billion records in the first half of 2020",
                 "45% of breaches featured hacking, 17% involved malware and 22% involved phishing",
                 "The top malicious email attachment types are .doc and .dot which make up 37%, the next highest is .exe at 19.5%",
                 "An estimated 300 billion passwords are used by humans and machines worldwide",
                 "The average time to identify a breach in 2020 was 207 day",
                 "Personal data was involved in 58% of breaches in 2020",
                 "Security breaches have increased by 11% since 2018 and 67% since 2014",
                 "64% of Americans have never checked to see if they were affected by a data breach",
                 "56% of Americans don’t know what steps to take in the event of a data breach",
                 "In 2020, a Twitter breach targeted 130 accounts, including those of past presidents and Elon Musk, resulted in attackers swindling $121,000 in Bitcoin through nearly 300 transactions",
                 "In 2020, Marriott disclosed a security breach impacted data of more than 5.2 million hotel guests",
                 "The 2019 MGM data breach resulted in hackers leaking records of 142 million hotel guests",
                 "In 2018, Under Armor reported that its “My Fitness Pal” was hacked, affecting 150 million users",
                 "The Equifax breach cost the company over $4 billion in total",
                 "100,000 groups in at least 150 countries and more than 400,000 machines were infected by the Wannacry virus in 2017, at a total cost of around $4 billion",
                 "In 2016, Uber reported that hackers stole the information of over 57 million riders and drivers",
                 "Uber tried to pay off hackers to delete the stolen data of 57 million users and keep the breach quiet",
                 "In one of the biggest breaches of all time 3 billion Yahoo accounts were hacked in 2013",
                 "The average ransomware payment rose 33% in 2020 over 2019, to $111,605",
                 "In 2018, an average of 10,573 malicious mobile apps were blocked per day",
                 "The average cost of a ransomware attack on businesses is $133,000",
                 "48% of malicious email attachments are office files",
                 "About 20% of malicious domains are very new and used around one week after they are registered",
                 "After declining in 2019, phishing increased in 2020 to account for 1 in every 4,200 emails",
                 "1 in 13 web requests lead to malware",
                 "Phishing attacks account for more than 80% of reported security incidents",
                 "$17,700 USD is lost every minute due to a phishing attack",
                 "In 2023, the total number of DDoS attacks worldwide will be 15.4 million",
                 "30% of data breaches involve internal actors",
                 "1 in 36 mobile devices have high- risk apps installed"]
        fact = random.choice(facts)
        fact_thumbnail = random.randint(1, 6)
        if fact_thumbnail == 1:
            emb = discord.Embed(title="Fact:", description=fact)
            emb.set_thumbnail(url="https://media.istockphoto.com/photos/facts-picture-id185269091?b=1&k=20&m=185269091&s=170667a&w=0&h=lMfv8GDbAyDNxZSMDbOFvo5dNZvSyQtYZB8lzUDH_ec=")
        if fact_thumbnail == 2:
            emb = discord.Embed(title="Fact:", description=fact)
            emb.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLRWMPjm1WyrBVD22h1g0kUXkfOsphMpa95av_NftQ=s900-c-k-c0x00ffffff-no-rj")
        if fact_thumbnail == 3:
            emb = discord.Embed(title="Fact:", description=fact)
            emb.set_thumbnail(url="https://thumbs.dreamstime.com/b/fact-square-grunge-stamp-fact-sign-fact-fact-stamp-125006414.jpg")
        if fact_thumbnail == 4:
            emb = discord.Embed(title="Fact:", description=fact)
            emb.set_thumbnail(url="https://www.factdialogue.org/frontend_standard/img/logo.png?v3")
        if fact_thumbnail == 5:
            emb = discord.Embed(title="Fact:", description=fact)
            emb.set_thumbnail(url="https://tomsbytwo.files.wordpress.com/2016/04/facts.jpg")
        if fact_thumbnail == 6:
            emb = discord.Embed(title="Fact:", description=fact)
            emb.set_thumbnail(url="https://thumbs.dreamstime.com/b/fact-square-grunge-stamp-fact-sign-fact-fact-stamp-125006414.jpg")
        await ctx.send(embed=emb)

    @commands.command(name="botping", help="Sends the bot's current ping")
    async def botping(self, ctx):
        emb = discord.Embed(title="Executive's Ping")
        emb.add_field(name="Ping:", value=f"{self.client.latency * 1000}".split('.')[0])
        emb.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=emb)

    @commands.command(aliases=['rn', 'randomnum'], name="randomnumber", help="Sends a random number")
    async def randomnumber(self, ctx, num1=0, num2=1000000):
        await ctx.send(random.randint(num1, num2))

    """@commands.command(name='verify', help='Verifies you')
    async def verify(self, ctx):
        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        opinionRole = discord.utils.get(ctx.guild.roles, name="OPINION")
        user = ctx.author

        if Verified in user.roles:
            await ctx.send("You are already verified")

        else:
            await user.add_roles(Verified)
            await ctx.send("You have now been verified")
            await ctx.author.send("You Are Now A Verified Member")
            await user.add_roles(opinionRole)"""

    @commands.command(name="minecraft", help="Sends our Minecraft server's Ip address.")
    async def minecraft(self, ctx):
        await ctx.send("think_cyber.apexmc.co")

    @commands.command(name="stats", help="Our server's and the Executive's stats")
    async def stats(self, ctx):
        pyv = platform.python_version()
        dpyv = discord.__version__
        mc = len(set(self.client.get_all_members()))
        mc -= 2
        actual_lines_of_code = "1948"
        emb = discord.Embed(title="Statistics", colour=discord.Colour.lighter_gray())
        emb.add_field(name="Members:", value=mc, inline=False)
        emb.add_field(name="Coding Language:", value="Python", inline=False)
        emb.add_field(name="Python Version:", value=pyv, inline=False)
        emb.add_field(name="Discord.Py Version:", value=dpyv, inline=False)
        emb.add_field(name="Lines Of Code:", value="1948", inline=False)
        emb.add_field(name="Executive Version:", value="5", inline=False)
        emb.add_field(name="Slowmode Delay:", value=ctx.channel.slowmode_delay, inline=False)
        emb.add_field(name="Topic:", value=f"{ctx.channel.topic if ctx.channel.topic else 'No topic'}", inline=False)
        emb.add_field(name="Channel Creation Time:", value=ctx.channel.created_at, inline=False)
        emb.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.channel.send(embed=emb)

def setup(client):
    client.add_cog(Normal_Cmds(client))