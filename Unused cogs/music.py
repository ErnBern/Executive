import discord
from discord.ext import commands

from youtube_dl import YoutubeDL


class Music_Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}

        self.vc = ""

    # searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            # get the first url
            m_url = self.music_queue[0][0]['source']

            # remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            # try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                try:
                    self.vc = await self.music_queue[0][1].connect()
                except:
                    pass
            else:
                await self.vc.move_to(self.music_queue[0][1])

            print(self.music_queue)
            # remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(aliases=['p'], name="play", help="Plays a selected song from youtube")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def p(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()
    @commands.command(aliases=['q'], name="queue", help="Displays the current songs in queue")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    @q.error
    async def q_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(aliases=['fs', 's'], name="skip", help="Skips the current song that is being played")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            # try to play next in the queue if it exists
            await self.play_music()
            await ctx.send("Skipped Song")

    @skip.error
    async def skip_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(aliases=['dc', 'd'], name="disconnect", help="Disconnects bot from VC")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def dc(self, ctx):
        await self.vc.disconnect()
        await ctx.send("Disconnected from voice channel")

    @dc.error
    async def dc_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='pause', help="Pauses the current song that is playing")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def pause(self, ctx):
        self.vc.pause()
        await ctx.send("Paused Song")

    @pause.error
    async def pause_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='resume', help='Resumes the song that was paused')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def resume(self, ctx):
        self.vc.resume()
        await ctx.send("Resumed song")

    @resume.error
    async def resume_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='join', help="Joins the voice channel you're in")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def join(self, ctx):
       if ctx.author.voice is None:
           await ctx.send("You're not in a voice channel!")
       voice_channel = ctx.author.voice.channel
       if ctx.voice_client is None:
           await voice_channel.connect()
           await ctx.send("Bot has joined the voice channel")
       else:
           await ctx.voice_client.move_to(voice_channel)

def setup(bot):
    bot.add_cog(Music_Cmds(bot))