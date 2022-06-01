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
        color=discord.Color("0xc27c0e"))
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

@bot.command()
async def hm(ctx):
    await Hangman(ctx)

@bot.command()
async def hangman(ctx):
    await Hangman(ctx)

@bot.command()
async def Hangman(ctx):
    with open('hangman.txt', 'r') as dict:
        line = dict.readline()
        dict_list = []
        while line:
            dict_list.append(line.strip())
            line = dict.readline()
    word = dict_list[random.randint(0,len(dict_list)-1)]
    print(word)
    invalid = True
    word_list = list(word)
    guess_list = []
    game = 1
    firstTime = 1
    guesses_left = 6
    print("_ " * len(word))
    await ctx.channel.send("Welcome to hangman, type 0 to quit")
    await ctx.channel.send("\_ " * len(word))
    while game != 0:
        if guesses_left <= 0:
            print("Game Over")
            await ctx.channel.send("Game Over")
            await ctx.channel.send("The word  "+word)
            game = 0
            break
        try:
            await ctx.channel.send("Make a guess:")
            guess = await bot.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
            guess = str(guess.content).lower()
            print(guess)
            while invalid == True:
                if len(guess) > 1 and guess.lower()!= word:
                    await ctx.channel.send("Invalid. Guess your letter: ")
                    guess = await bot.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
                    guess = str(guess.content)
                    continue
                else:
                    invalid = False
        except asyncio.TimeoutError:
            await ctx.channel.send("You took too long!")
            await ctx.channel.send("The word was "+word)
            return -1
        if guess.lower() == word:
            await ctx.channel.send("correct!")
            await ctx.channel.send("You win~!")
            return -1
        if guess in word_list and firstTime == 1:
            for x in range(len(word_list)):
                if guess == word_list[x]:
                    guess_list.append(guess)
                else:
                    guess_list.append("- ")
            await ctx.channel.send("```" + str(guess_list).replace("[", "").replace("'","").replace(",","").replace("]","").replace(" ","") + " ```")
            await ctx.channel.send("correct!")
            # await ctx.channel.send("you have " + str(guesses_left) + " incorrect guesses left")
            firstTime = 0
            continue
        elif guess not in word_list and guess=="0":
            await ctx.channel.send("quitting")
            return -1
        elif guess not in word_list:
            await ctx.channel.send("incorrect!")
            guesses_left -=1
            await ctx.channel.send("you have " + str(guesses_left) + " incorrect guesses left")
        if guess in word_list and firstTime != 1:
            if guess in guess_list:
                await ctx.channel.send("already guessed!")
                await ctx.channel.send("```" + str(guess_list).replace("[", "").replace("'","").replace(",","").replace("]","").replace(" ","") + " ```")
                continue
            else:
                for x in range(len(word_list)):
                    if guess == word_list[x]:
                        guess_list[x] = guess
                await ctx.channel.send("```" + str(guess_list).replace("[", "").replace("'","").replace(",","").replace("]","").replace(" ","") + " ```")
                await ctx.channel.send("correct!")
                # await ctx.channel.send("you have " + str(guesses_left) + " incorrect guesses left")
                if guess_list == word_list:
                    await ctx.channel.send("You win~!")
                    game = 0





# Birthday
bot.run("OTgwMjI2NjQ4OTU3OTM5NzUz.GPrRvd.tWWpLWs43DBIzxhC_3KVueKZqKwY9aKSOaMXRU")



'''from bokeh.plotting import figure, show, output_file
import json
from collections import Counter
birthday_dict = {
    "Oliver": "07/01/04",
    "Richard": "09/09/05",
    "Kyle": "09/29/04",
    "Jack": "06/10/03",
}
def LoadOldBirthdays():
    with open("birthday_info.json", "r") as f:
        global info
        info = json.load(f)
        return
def CheckMonths():
    #print(info)
    month_dict = {
        1 : "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month_list = []
    for index in info:
        month_list.append(list(info[index].split("/"))[0])
    month_list = [int(index) for index in month_list]
    month_list = [month_dict.get(index) for index in month_list]
    print(Counter(month_list))
    output_file("plot.html")
    x_cat = []
    y = []
    for i in month_dict:
        x_cat.append(month_dict[i])
    x_list = month_list
    for i in month_list:
        y.append(Counter(month_list)[i])
    p = figure(x_range=x_cat)
    p.vbar(x=x_list, top=y, width=.5)
    show(p)
def AskBirthday(help="Who's birthday do you want to look up?\n"):
    name = input(help)
    name = name.title()
    if name in info:
        print("{}\'s birthday is {}".format(name,info.get(name)))
    else:
        print("{}\'s birthday is not in dictionary".format(name))
    return
def AddEntry():
    name = input("Who do you want to add to the Birthday dictionary?\n")
    name = name.title()
    date = input("When was {} born? Enter in mm/dd/yy format:\n".format(name))
    info[name] = date
    with open("birthday_info.json","w") as f:
        json.dump(info, f)
    print("{} was added to the birthday list".format(name))
if __name__ == "__main__":
    LoadOldBirthdays()
    Quit = 0
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for x in info.keys():
        print(x)
    AskBirthday()
    while Quit == 0:
        nextAction = input("What would you like to do next? Add, Find, Check, Quit:\n")
        nextAction = nextAction.title()
        if nextAction == "Add":
            AddEntry()
            continue
        elif nextAction == "Find":
            print("We know the birthdays of: ")
            for x in info.keys():
                print(x)
            AskBirthday()
            continue
        elif nextAction == "Quit":
            print("Quitting")
            Quit = 1
            break
        elif nextAction == "Check":
            CheckMonths()
            continue
        else:
            print("not valid choice".title())
            continue'''
