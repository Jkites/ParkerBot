import asyncio
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="%%")

textStimuli = {
    "parker": "pedro"
}


def match_text(text):
    for a in textStimuli:
        if a == text:
            return textStimuli[a]


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"{guild.id} (name:{guild.name})")
        guild_count = guild_count + 1
    print("Parker is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    text = str(message.content).lower()
    text = match_text(text)
    if not text is None:
        await message.channel.send(text)
    await bot.process_commands(message)


@bot.command()
async def embed(ctx):
    text1 = discord.Embed(
        title="Information",
        description="information stuff",
        color=discord.Color.random())
    text1.set_author(name="pp", icon_url="https://cdn.vox-cdn.com/thumbor/MZRJnpwAMIHQ5-XT4FwNv0rivw4=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19397812/1048232144.jpg.jpg")
    text1.set_thumbnail(url="https://c.tenor.com/QqSkd-o9L8sAAAAC/aireu-wysi.gif")
    text1.add_field(name="sleeper", value="hi", inline=False)
    text1.set_footer(text="save me")
    await ctx.send(embed=text1)


# Games
@bot.command()
async def CowBull(ctx):
    await ctx.channel.send("```Welcome to Cow and Bulls. Guess 4 Cows to win```")
    list1 = []
    i = 1
    list2 = []
    userinput = 10000
    bulls = 0
    cows = 0
    indexnum = 0
    while i <= 4:
        list1.append(random.randint(0, 9))
        i += 1
    while cows != 4:
        cows=0
        while userinput > 9999 or userinput < 0:
            try:
                await ctx.channel.send("Enter a number between 0 and 9999")
                userinput = await bot.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
                userinput = int(userinput.content)
                if userinput > 9999 or userinput < 0:
                    print("enter valid number")
                    await ctx.channel.send("enter valid number")
            except (ValueError, TypeError) as e:
                userinput = str(userinput.content).lower()
                print (userinput)
                if userinput == "quit":
                    print("quitting")
                    await ctx.channel.send("quitting")
                    return -1
                print("enter valid number")
                await ctx.channel.send("enter valid number")
                userinput = -1
            except asyncio.TimeoutError:
                await ctx.channel.send("Too late!")
                return -1
        if userinput in range(100,1000):
            list2.append(0)
            list2+=[int(d) for d in str(userinput)]
        elif userinput in range(10,100):
            list2.append(0)
            list2.append(0)
            list2 += [int(d) for d in str(userinput)]
        elif userinput in range(0,10):
            list2.append(0)
            list2.append(0)
            list2.append(0)
            list2 += [int(d) for d in str(userinput)]
        else:
            list2+=[int(d) for d in str(userinput)]
        while indexnum < 4:
            if list1[indexnum] == list2[indexnum]:
                cows+=1
                indexnum+=1
                if indexnum >=4:
                    indexnum = 0
                    print(list2)
                    await ctx.channel.send(list2)
                    print(str(cows) + " cow(s) and " + str(bulls) + " bull(s)")
                    await ctx.channel.send(str(cows) + " cow(s) and " + str(bulls) + " bull(s)")
                    list2.clear()
                    userinput = 10000
                    break
            else:
                bulls+=1
                indexnum+=1
                if indexnum >=4:
                    indexnum = 0
                    print(list2)
                    #await ctx.channel.send(list2)
                    print(str(cows) + " cow(s) and " + str(bulls) + " bull(s)")
                    await ctx.channel.send(str(cows) + " cow(s) and " + str(bulls) + " bull(s)")
                    list2.clear()
                    userinput = 10000
                    break
        print(list1) #prints after cows


@bot.command()
async def cab(ctx):
    await CowBull(ctx)
# Birthday
bot.run("OTgwMjI2NjQ4OTU3OTM5NzUz.GPrRvd.tWWpLWs43DBIzxhC_3KVueKZqKwY9aKSOaMXRU")




