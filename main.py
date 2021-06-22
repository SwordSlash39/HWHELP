# Bot code: NzE5OTAxMjIyMzY2MDg1Mjkw.Xt-KTQ.BrkF7AsdE-IVsX2aLvDLemtFfEM
import discord, time
from discord.ext import commands


token = 'NzE5OTAxMjIyMzY2MDg1Mjkw.Xt-KTQ.BrkF7AsdE-IVsX2aLvDLemtFfEM'
default_call = ','
client = commands.Bot(command_prefix=str(default_call))
global content, homework, txt, blacklist, personal_list, authorised, msg
content = ""
homework = []
blacklist = []
personal_list = []
authorised = []    # Insert your discord ID here
txt = ""
msg = ""
icon = "https://lh3.googleusercontent.com/-4SNBk7GMyEE/Xx5zbN2_HpI/AAAAAAAABUg/sWTXhsIMY_YcwXJAcRgM0q3jY0YaW_mpgCK8BGAsYHg/s0/2020-07-26.png"


def findPlayer(player):
    for i in range(len(personal_list)):
        if str(personal_list[i][0]) == str(player):
            return i
    return "nil"


def findHw(id):
    for i in range(len(homework)):
        if str(homework[i]["id"]) == str(id):
            return i
    return False


def hours(hr: float):
    return hr * 3600


def days(day: float):
    return day * hours(24)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.remove_command('help')
@client.command(aliases=['help', 'halp', "help me", "commands"])
async def cmd(ctx):
    try:
        await ctx.channel.purge(limit=1)
    except:
        pass
    msg = discord.Embed(title="Help",
                        description=
                        str(default_call) + "add_hw `id` `homework` --> Add homework into the homework list\n" +
                        str(default_call) + "show_hw `id`--> Shows the today\'s hw\n" +
                        str(default_call) + "remove `id` `homework_number` --> Removes the `homework_number` item from the homework list\n" +
                        str(default_call) + "join_class `id` `password` --> Join a class\n" +
                        str(default_call) + "create_class `id` `password` --> Create your own class with ID: `id` and Password: `password`\n" +
                        str(default_call) + "deleted_hw `id` --> Shows the recently deleted homework for class `id` (will be automatically deleted after 7 days)",
                        color=discord.Color.gold())
    msg.add_field(name="Legend:", value="`id` --> ID of a class")

    msg.set_author(name="Hw help")
    msg.set_thumbnail(
        url=icon)
    await ctx.channel.send(embed=msg)

@client.command(aliases=['ssf', 'show_savefile', 'display_savefile'])
async def savefile(ctx):
    print(homework)
    await ctx.author.send(str(homework))

@client.command(aliases=["join_class", "join-class", "enter_class", "enter-class"])
async def _join_class(ctx, id, password):
    try:
        await ctx.channel.purge(limit=1)
    except:
        pass
    if findHw(id) != False:
        msg = homework[findHw(id)]
        if msg['password'] == password:
            if not str(ctx.author.id) in msg['members']:
                homework[findHw(id)]['members'].append(str(ctx.author.id))
                msg = discord.Embed(title="Success!",
                                    description="You joined the class!",
                                    color=discord.Color.green())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                    description="You are already in this class!",
                                    color=discord.Color.red())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
        else:
            msg = discord.Embed(title="Error",
                                description="Password incorrect",
                                color=discord.Color.red())
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
            await ctx.channel.send(embed=msg)
    else:
        msg = discord.Embed(title="Error",
                            description="Class id {} not found".format(str(id)),
                            color=discord.Color.red())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.channel.send(embed=msg)


@client.command(aliases=["show_hw", "display_hw", "show_homework", "display_homework", "homework", "hw", "show-hw"])
async def _show_hw(ctx, id):
    if findHw(id):
        msg = homework[findHw(id)]
        if str(ctx.author.id) in msg["members"]:
            if msg['homework'] != []:
                txt = ""
                for x in range(len(msg['homework'])):
                    txt += "#" + str(x + 1) + ": " + str(msg["homework"][x] + "\n")
                msg = discord.Embed(title="Homework for today:",
                                        description=str(txt),
                                        color=discord.Color.blue())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Nothing!",
                                        description="BEEG happy! There isnt any *`homework`* for today! :smile:",
                                        color=discord.Color.green())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
        else:
            msg = discord.Embed(title="Error",
                                description="{}, you are not in that class".format(str(ctx.author.mention)),
                                color=discord.Color.red())
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
            await ctx.channel.send(embed=msg)
    else:
        msg = discord.Embed(title="Error",
                            description="Class id `" + str(id) + "` not found",
                            color=discord.Color.red())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.channel.send(embed=msg)

@client.command(aliases=["add_hw", "add", "add-hw"])
async def _add_hw(ctx, id, *, hw):
    if findHw(id):
        msg = homework[findHw(id)]
        if str(ctx.author.id) in msg["members"]:
            if str(ctx.author) not in blacklist:
                homework[findHw(id)]["homework"].append(str(hw))
                msg = discord.Embed(title="Success!",
                                        description="Successfully added `" + str(hw) + "` to the homework list!",
                                        color=discord.Color.green())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(url=icon)
                await ctx.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                        description="You have been blacklisted",
                                        color=discord.Color.red())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
        else:
            msg = discord.Embed(title="Error",
                                description="You are not in that class",
                                color=discord.Color.red())
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
            await ctx.channel.send(embed=msg)
    else:
        msg = discord.Embed(title="Error",
                            description="Class not found",
                            color=discord.Color.red())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.channel.send(embed=msg)


@client.command(aliases=["del_hw", "deleted_homework", "deleted_hw"])
async def _show_deleted_hw(ctx, id):
    if findHw(id):
        msg = homework[findHw(id)]
        for x in range(len(msg["del_hw"])):
            if time.time() - float(msg["del_hw"][len(msg["del_hw"]) - x - 1][1]) >= days(7):
                msg["del_hw"].pop(len(msg["del_hw"]) - x - 1)

        if len(msg["del_hw"]) > 0:
            txt = "\n\n"
            for i in range(len(msg["del_hw"])):
                txt += "#{}: {}\n".format(str(i + 1), msg["del_hw"][i][0])
            msg = discord.Embed(title="Recently deleted homework",
                                description=str(txt),
                                color=0xeca7a7)
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
        else:
            msg = discord.Embed(title="No deleted hw!",
                                description="There isn\'t any deleted homework! :D",
                                color=discord.Color.green())
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
        await ctx.channel.send(embed=msg)
    else:
        msg = discord.Embed(title="Error",
                            description="Class not found",
                            color=discord.Color.red())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.channel.send(embed=msg)



@client.command(aliases=["remove", "pop"])
async def _remove(ctx, id, num):
    if findHw(id):
        try:
            msg = homework[findHw(id)]
            if str(ctx.message.author) not in blacklist:
                try:
                    homework[findHw(id)]["del_hw"].append([msg["homework"][int(num) - 1], time.time()])
                except KeyError:
                    homework[findHw(id)]["del_hw"] = [[msg["homework"][int(num) - 1], time.time()]]
                homework[findHw(id)]["homework"].pop(int(num) - 1)
                msg = discord.Embed(title="***`Pop`***",
                                    description="Successfully removed hw number #{} from the homework list!".format(num),
                                    color=discord.Color.green())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="Error",
                                        description="You have been blacklisted",
                                        color=discord.Color.red())
                msg.set_author(name="Hw help")
                msg.set_thumbnail(
                    url=icon)
                await ctx.channel.send(embed=msg)
        except IndexError:
            msg = discord.Embed(title="Invalid",
                                    description="Something went wrong, are you sure that hw number exists? Just checking.",
                                    color=discord.Color.red())
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
            await ctx.channel.send(embed=msg)
        except ValueError:
            msg = discord.Embed(title="Invalid",
                                    description="Something went wrong, are you sure you keyed in a number? Just checking.",
                                    color=discord.Color.red())
            msg.set_author(name="Hw help")
            msg.set_thumbnail(
                url=icon)
            await ctx.channel.send(embed=msg)
    else:
        msg = discord.Embed(title="Error",
                            description="Class id not found",
                            color=discord.Color.red())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.channel.send(embed=msg)


@client.command()
async def create_class(ctx, id, password):
    try:
        await ctx.channel.purge(limit=1)
    except:
        pass
    if findHw(id) == False:
        homework.append({'homework': [], "password": str(password), "id": id, "del_hw": [], "members": [str(ctx.author.id)]})
        msg = discord.Embed(title="Success!",
                            description="You created your class with id `{}` and password `{}`!".format(str(id), str(password)),
                            color=discord.Color.green())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.author.send(embed=msg)
    else:
        msg = discord.Embed(title="Error",
                            description="That class ID already exists!",
                            color=discord.Color.red())
        msg.set_author(name="Hw help")
        msg.set_thumbnail(
            url=icon)
        await ctx.author.send(embed=msg)


client.run(token)
