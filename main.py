import random
import discord

bot = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"{guild.id} (name:{guild.name})")
        guild_count = guild_count+1
    print("Parker is in "+ str(guild_count)+" guilds.")

@bot.event
async def on_message(message):
    if message.content.lower() == "parker":
        # sends message
        await message.channel.send("pedro")
bot.run("OTgwMjI2NjQ4OTU3OTM5NzUz.GPrRvd.tWWpLWs43DBIzxhC_3KVueKZqKwY9aKSOaMXRU")
'''def CowBull():
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
                userinput = int(input("Enter a number: "))
                if userinput > 9999 or userinput < 0:
                    print("enter valid number")
            except ValueError:
                print("enter valid number")
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
                    print(str(cows) + " cow(s) and " + str(bulls) + " bull(s)")
                    list2.clear()
                    userinput = 10000
                    break
            else:
                bulls+=1
                indexnum+=1
                if indexnum >=4:
                    indexnum = 0
                    print(list2)
                    print(str(cows) + " cow(s) and " + str(bulls) + " bull(s)")
                    list2.clear()
                    userinput = 10000
                    break
        #print(list1) prints after cows
CowBull()'''