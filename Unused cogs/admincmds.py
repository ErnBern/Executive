import discord, asyncio
from discord.ext import commands

class Admin_Cmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin Cog is ready")

    class DurationConverter(commands.Converter):
        async def convert(self, command, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ['s', 'm', 'h', 'd']:
                return (int(amount), unit)

            raise command.BadArgument(message='Not a valid duration')


    @commands.command(name="ban", help='Bans a member')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned for {reason}')

    @ban.error
    async def ban_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)


    @commands.command(name='unban', help="Unbans a member, don't @ them but include their discord tag")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='kick', help="Kicks a member")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked for {reason}')

    @kick.error
    async def kick_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='clear', help='Deletes messages')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='mute', help='Mutes a member')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def mute(self, ctx, *, user : discord.Member):
        MUTED = discord.utils.get(ctx.guild.roles, name="MUTED")
        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        Opinion = discord.utils.get(ctx.guild.roles, name="OPINION")

        if MUTED in user.roles:
         await ctx.send(f"{user.mention} is already muted.")

        else:
            if Verified in user.roles:
                await user.remove_roles(Verified)
                await user.add_roles(MUTED)
                await ctx.send(f"{user.mention} has been muted.")

            if Opinion in user.roles:
                await user.remove_roles(Opinion)
            await user.add_roles(MUTED)

    @mute.error
    async def mute_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='unmute', help='Unmutes a member')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def unmute(self, ctx, *, user : discord.Member):
        MUTED = discord.utils.get(ctx.guild.roles, name="MUTED")
        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        Opinion = discord.utils.get(ctx.guild.roles, name="OPINION")
        if MUTED in user.roles:
            await user.remove_roles(MUTED)
            await user.add_roles(Verified)
            await user.add_roles(Opinion)
            await ctx.send(f"Unmuted {user}")


        else:
            await ctx.send(f"{user} is already unmuted.")

    @unmute.error
    async def unmute_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='disenfranchise', help="Takes away a member's ability to vote")
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def disenfranchise(self, ctx, member: discord.Member):
        opinionRole = discord.utils.get(ctx.guild.roles, name="OPINION")
        await member.remove_roles(opinionRole)
        await ctx.send(f"{member.mention}, permissions to vote have been taken.")

    @disenfranchise.error
    async def disenfranchise_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='franchise', help="Gives a member the ability to vote")
    @commands.has_any_role("TC HELPER", "Server Booster", 'Founder')
    async def franchise(self, ctx, member: discord.Member):
        opinionRole = discord.utils.get(ctx.guild.roles, name="OPINION")
        await member.add_roles(opinionRole)
        await ctx.send(f"{member.mention}, permissions to vote have been given.")

    @franchise.error
    async def franchise_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)



    @commands.command(name="poll", help='A poll with a simple thumbs up and down')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def poll(self, ctx, *, message):
        amount = 1
        await ctx.channel.purge(limit=amount)
        emb = discord.Embed(title="Opinion", description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

    @poll.error
    async def poll_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='numpoll', help='A poll with numbers')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def numpoll(self, ctx, *, message):
        amount = 1
        await ctx.channel.purge(limit=amount)
        emb = discord.Embed(title="Opinion", description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')
    @numpoll.error
    async def numpoll_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name='colpoll', help='A poll with colours')
    @commands.has_any_role("TC MEMBERS", "TC HELPER", "Server Booster", 'Founder')
    async def colpoll(self, ctx, *, message):
        amount = 1
        await ctx.channel.purge(limit=amount)
        emb = discord.Embed(title="Opinion", description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction('🟥')
        await msg.add_reaction('🟩')
        await msg.add_reaction('🟦')
    @colpoll.error
    async def colpoll_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.group(invoke_without_command=True, name="new", help="Creates a channel or category")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def new(self, ctx):
        await ctx.send("Invalid sub-command")


    @new.command(name='category', help='Makes a new category')
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def category(self, ctx, *, name):
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        category = await ctx.guild.create_category(name=name, overwrites=overwrites)
        await ctx.send(f"Made category {category.name}")

    @new.error
    @category.error
    async def category_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @new.command(name="channel", help='Makes a new chanel')
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def channel(self, ctx, *, name):
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await ctx.guild.create_text_channel(name=name, overwrites=overwrites)
        await ctx.send(f"Made channel {channel.name}")
    @new.error
    @channel.error
    async def channel_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.group(invoke_without_command=True, name="delete", help="Deletes a channel or category")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def delete(self, ctx):
        await ctx.send("Invalid sub-command")

    @delete.command(name="category", help="Deletes a category")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def _category(self, ctx, *, category: discord.CategoryChannel):
        await category.delete()
        await ctx.send(f'Deleted {category.name}')

    @delete.error
    @_category.error
    async def _category(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)


    @delete.command(name="channel", help="Deletes a text channel")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def _channel(self, ctx, *, category: discord.TextChannel):
        await category.delete()
        await ctx.send(f'Deleted {category.name}')

    @delete.error
    @_channel.error
    async def _channel(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(name="lock", help="Locks a channel")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def lock(self, ctx, channel: discord.TextChannel = None):
        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        channel = channel or ctx.channel

        overwrites = channel.overwrites[ctx.guild.default_role]
        overwrites.send_messages = False
        await channel.set_permissions(Verified, overwrite=overwrites)
        await ctx.send(f"Locked {channel.name}")

    @lock.error
    async def lock_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(aliases=['tl'], name="templock", help="Temporarily locks a channel")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def templock(self, ctx, duration: DurationConverter, channel: discord.TextChannel = None):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = duration

        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        channel = channel or ctx.channel

        overwrites = channel.overwrites[ctx.guild.default_role]
        overwrites.send_messages = False
        await channel.set_permissions(Verified, overwrite=overwrites)
        await ctx.send(f"Locked {channel.name} for {amount}{unit}")
        await asyncio.sleep(amount * multiplier[unit])
        overwrites.send_messages = True
        await channel.set_permissions(Verified, overwrite=overwrites)


    @commands.command(name="unlock", help="Unlocks a locked channel")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        overwrites = channel.overwrites[ctx.guild.default_role]
        overwrites.send_messages = True
        overwrites.view_channel = True
        await channel.set_permissions(Verified, overwrite=overwrites)
        await ctx.send(f"Unlocked {channel.name}")
    @unlock.error
    async def unlock_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(error)

    @commands.command(aliases=['tb'], name="tempban", help="Temporarily bans a user")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def _ban(self, ctx, member: discord.Member, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = duration

        await member.ban()
        await ctx.send(f'{member} has been banned for {amount}{unit}')
        await asyncio.sleep(amount * multiplier[unit])
        await member.unban()

    @commands.command(aliases=["tm"], name='tempmute', help="Temporarily mutes a user")
    @commands.guild_only()
    @commands.has_any_role("TC MEMBERS", "TC HELPER", 'Founder')
    async def tempmute(self, ctx, user: discord.Member, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = duration

        MUTED = discord.utils.get(ctx.guild.roles, name="MUTED")
        Verified = discord.utils.get(ctx.guild.roles, name="VERIFIED")
        Opinion = discord.utils.get(ctx.guild.roles, name="OPINION")

        if MUTED in user.roles:
            await ctx.send(f"{user.mention} is already muted.")

        else:
            if Verified in user.roles:
                await user.remove_roles(Verified)
                await user.add_roles(MUTED)
                await ctx.send(f"{user.mention} has been muted for {amount}{unit}")

            if Opinion in user.roles:
                await user.remove_roles(Opinion)
            await user.add_roles(MUTED)
            await asyncio.sleep(amount * multiplier[unit])
            await user.remove_roles(MUTED)
            await user.add_roles(Opinion)
            await user.add_roles(Verified)



def setup(client):
    client.add_cog(Admin_Cmds(client))