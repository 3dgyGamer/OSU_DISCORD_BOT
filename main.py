import os
import discord
import random
import asyncio


from discord import Spotify

from discord.ext import commands


intents = discord.Intents.all()
intents.messages = True

client = commands.Bot(command_prefix = "!", intents=intents)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


@client.command()
async def chuck(ctx):
  await ctx.send('```I AM NOT CRAZY!... I am not crazy! I know he swapped those numbers. I knew it was 1216. One after Magna Carta. As if I could ever make such a mistake. Never. Never! I just - I just couldnt prove it. He covered his tracks, he got that idiot at the copy shop to lie for him. You think this is something? You think this is bad? This? This chicanery? Hes done worse. That billboard! Are you telling me that a man just happens to fall like that? No! *He* orchestrated it! Jimmy! He *defecated* through a *sunroof*! And I saved him! And I shouldnt have. I took him into my own firm! What was I *thinking*? Hell never change. Hell *never* change! Ever since he was 9, *always* the same! Couldnt keep his hands out of the cash drawer! But not our Jimmy! Couldnt be precious *Jimmy*! Stealing them blind! And *HE* gets to be a lawyer? What a sick joke! I shouldve stopped him when I had the chance!```')
  await ctx.send('https://tenor.com/view/chuck-better-call-saul-rant-explain-chicanery-gif-25351449')

@client.command()
async def gavin(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/930653029768790116/1019057332572934214/unknown.png')
@client.command()
async def spotify(ctx, user: discord.Member= None):
  if user == None:
        user = ctx.mention
        pass
  if user.activities:
    for activity in user.activities:
      if isinstance(activity, Spotify):
        embed = discord.Embed(
        title = f"{user.name}'s Spotify",
        description = "Listening to {}".format(activity.title), color = 0xFFC0CB)
        embed.set_thumbnail(url=activity.album_cover_url)
        embed.add_field(name="Artist", value=activity.artist)
        embed.add_field(name="Album", value=activity.album)
        embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
        await ctx.send(embed=embed)
  else:
    await ctx.send("No spotify activity is found")

#show their playlist?
@client.command()
async def playlist(ctx, user: discord.Member=None):
  if user == None:
    user = ctx.mention
    pass
  #hyunbin
  if user.id == 527317965230702612:
    await ctx.send('https://open.spotify.com/album/34GQP3dILpyCN018y2k61L?si=a45b3baeaf2349d5')
  #aiden park
  if user.id == 575852934651445248:
    await ctx.send('https://open.spotify.com/playlist/5ZgmH1PXFgGWCcZegzFV4T?si=898a7cb8ff5e4e52')
  #yejun park
  if user.id == 595685425285300244:
    await ctx.send('https://open.spotify.com/playlist/0qxVGHvQxitkECaZD8ey2z?si=9b405948390d4593')
  if user.id == 785299730120310845:
    await ctx.send('test?')
@client.command()
async def math(ctx):
  await ctx.send('警察精CAN YOU DO THE MATHEMATICS?>警察精?')
  num_one = random.randint(1, 100)
  num_two = random.randint(1, 100)
  answer = num_one + num_two
  answer_string = str(answer)
  await ctx.send(f'{num_one} + {num_two}?')
  def check(m):
    return m.content == answer_string
  msg = await client.wait_for('message', check=check)
  await ctx.send(f"{msg.author.mention} got the correct answer!")


@client.command()
async def hb(ctx):
  await ctx.send('```Hyunbin Kim? Do you mean THE HYUNBIN KIM? he is rich af, top korean gangster of the bergen county, stacks the Extracurriculars faster than he can stack his BREAD, has a huge mansion, future cornell valedictorian, can buy ur entire bloodline, cracked at golf sport, the asian tiger woods, the k-pop king, the mvp of life```')

@client.command()
async def walter(ctx):
  await ctx.send('```Who are you talking to right now? Who is it you think you see? Do you know how much I make a year? I mean, even if I told you, you wouldnt believe it. Do you know what would happen if I suddenly decided to stop going into work? A business big enough that it could be listed on the NASDAQ goes belly up. Disappears! It ceases to exist without me. No, you clearly dont know who youre talking to, so let me clue you in. I am not in danger, Skyler. I am the danger. A guy opens his door and gets shot and you think that of me? No. I am the one who knocks!```')
  await ctx.send('https://tenor.com/view/walter-walterwhite-ballin-walterisballin-gif-26404776')
@client.command()
async def gamble(ctx):
  await ctx.send('we are both randomly picking a number from 1-10...')
  await asyncio.sleep(1)
  bot = random.randint(1, 10)
  yours = random.randint(1, 10)
  if bot == yours:
    await ctx.send('u just won 1 quinntillion waltillion dollars$$$!!!! :)' + ' my pick: ' + str(bot) + ' your pick: ' + str(yours))
    await ctx.send('\U0001f389')
  else:
    await ctx.send('u LOST!!! minus 1 QUINTILLION WALTILLION $DOLLAR$ :(' +  ' my pick: ' + str(bot) + ' your pick: ' + str(yours))
    await ctx.send('\U0001F621')
    

@client.command()
async def friend(ctx):
  img_lol = random.choice(open("friend.txt").readlines())
  enem_lol = random.choice(open("friend.txt").readlines())
  await ctx.send('one will be ur friend... one will be ur enemy...')
  await asyncio.sleep(1)
  await ctx.send('```ur friend:```')
  await ctx.send(img_lol)
  await ctx.send('```ur enemy:```')
  await ctx.send(enem_lol)
  chance = random.randint(1,2)
  if chance == 1:
    await ctx.send('```> UR FRIEND WINS!!!!1```')
  else:
    await ctx.send('```> UR OPP WINS!!11!```')
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
#COMMANDS
    if message.author == client.user:
        return
    if 'osu' in message.content:
        await message.channel.send('osu!, previously stylised as Osu!, is a free-to-play rhythm game primarily developed, published, and created by Dean "peppy" Herbert and released for Microsoft Windows on 16 September 2007. Its gameplay is inspired by other rhythm games, including Osu! Tatakae! Ouendan, Taiko no Tatsujin, Happy Feet, Beatmania IIDX, Elite Beat Agents, O2Jam, StepMania and DJMax.')
    
    if '727' in message.content:
      random_lines = random.choice(open("seven27.txt").readlines())
      await message.channel.send(random_lines)
    if 'wysi' in message.content:
        await message.channel.send('WYSI!!!')
        await message.add_reaction('\U0001F976')
#GOOD RESPONSES
    #aiden park
    if message.author.id == 575852934651445248:
      aiden_lines = random.choice(open("scripts.txt").readlines())
      await message.channel.send(aiden_lines)
    if message.author.id == 595685425285300244:
      await message.add_reaction('\U0001F976')
    if message.author.id == 503353272674025472:
      await message.add_reaction('\U0001F976')
    await client.process_commands(message)
my_secret = os.environ['TOKEN']
client.run(my_secret)


