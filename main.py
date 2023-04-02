import discord, random, os
from discord.ext import commands

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

class CustomHelpCommand(commands.HelpCommand):

   def __init__(self):
       super().__init__()

   async def send_bot_help(self, mapping):
       for cog in mapping:
           pass

   async def send_cog_help(self, cog):
      pass

   async def send_group_help(self, group):
       pass

   async def send_command_help(self, command):
       pass

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents, help_command=CustomHelpCommand())

@client.event
async def on_member_join(member):
    if member.guild.id != 932465380746735616: return
    channel = client.get_channel(id=932489947003379762)
    welcomes = ["Please click the reaction in <#937472442421612644> to confirm that you are not a bot!"]
    welcome = random.choice(welcomes)
    await channel.send(f"{member.name} {welcome}")
    await member.send(f'Welcome to the Think Cyber Community Server! I am Executive, a bot created by members of the team and I will support you during your time. To see all commands, do !help.')


@client.event
async def on_member_remove(member):
    if member.guild.id != 932465380746735616: return
    channel = client.get_channel(id=937553094210899981)
    leaves = ["Left The Server!", "Hopped Out!", "Sad To See You Go!"]
    leave = random.choice(leaves)
    await channel.send(f"{member.name} {leave}")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_raw_reaction_add(payload):
    poll = 954556673710784533
    verify = 964665363713392640
    if poll == payload.message_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name
        if emoji == '👍':
            role = discord.utils.get(guild.roles, name="MINECRAFT")
            await member.add_roles(role)
    if verify == 964665363713392640:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name
        if emoji == '✅':
            role1 = discord.utils.get(guild.roles, name="VERIFIED")
            role2 = discord.utils.get(guild.roles, name="OPINION")
            await member.add_roles(role1)
            await member.add_roles(role2)

@client.event
async def on_raw_reaction_remove(payload):
    poll = 954556673710784533
    verify = 964665363713392640
    if poll == payload.message_id:
        guild = await(client.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '👍':
            role = discord.utils.get(guild.roles, name="MINECRAFT")
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
    if verify == 964665363713392640:
        emoji = payload.emoji.name
        if emoji == '✅':
            guild = await(client.fetch_guild(payload.guild_id))
            member = await(guild.fetch_member(payload.user_id))
            role1 = discord.utils.get(guild.roles, name="VERIFIED")
            role2 = discord.utils.get(guild.roles, name="OPINION")
            if member is not None:
                await member.remove_roles(role1)
                await member.remove_roles(role2)


""" @client.command(name="ve", description="verify message")
async def verify_message(ctx):
    emb = discord.Embed(title="Verify", description="Please react to verify yourself!", colour=discord.Colour.dark_green())
    msg = await ctx.send(embed=emb)
    await msg.add_reaction("✅") """


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)