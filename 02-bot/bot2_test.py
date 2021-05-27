#Discord boti "Päts"-i kood.
#Koodi tegid Kahtlased Pettised: Kaimar Kangur, Henry Ploom ja Sten Voronin.
#Bot ja selle tooken on Kaimari käes.

#Koodi algus

#Importib vajalikud teemad sisse.
import discord
import random
import time
import datetime
from datetime import timedelta
from discord.ext import commands
from discord.ext import tasks

     
#Autentimistooken

#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!
token = "ODQ2MTIzMzY4OTM5OTEzMzA2.YKq7yw.G1Q3NZ8xMreAYC6_OB5E5i3xipk" #TOOKEN AAAAAAAAAAAAAAAA
#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!


client = commands.Bot(command_prefix = "p!")
client.remove_command("help")
client.remove_command("abort")


#Tekitab klassi, millega logib Discordi sisse, ehk startup.
#Paneb endale staatuse ja kinnitab sisse logimist.
käsklused= """info
abi
ping
meme
rindele
muusika  
äratus
fakt
kas
uudised
sus
elagu
abort
"""
info_käsk = "info" #töötab
abi_käsk = "abi" #töötab
ping_käsk = "ping" #töötab
meme_käsk = "meme" #töötab
rindele_käsk = "rindele" #töötab
muusika_käsk = "muusika" #POOLELI
äratuskell_käsk = "äratus" #POOLELI
faktid_käsk = "fakt" #POOLELI
küs_käsk = "k" 
uudis_käsk = "uudised" #töötab
sus_käsk = "sus" #töötab
elagu_käsk = "elagu" #POOLELI
abort_käsk = "abort" #töötab
op = "Tihke Päts#8878"

#@client.event
#async def on_message(ctx):
#    print(str(ctx.channel.name) + " / " + str(ctx.author) + ":"  + str(ctx.content))
#    await client.process_commands(ctx)

@client.event
async def on_ready():
    print("olen elus")
        
#Ping käsk testimiseks.
@client.command()
async def ping(ctx):
    print("Saadan teate")
    await ctx.send("pong")
    
#Annab kasutajale teada, mis on uut Pätsiga.    
@client.command()
async def uudised(ctx):
    print("Saadan uudiseid")
    await ctx.send("Teataja uudised: \n1.Oskab küsimustele vastata\n(*Viimati muudetud 25.05.21*)")
    
#Annab infot boti kohta.
@client.command()
async def info(ctx):
    print("Saadan infot")
    await ctx.send("""Olen kõikvõimas Konstatin Päts, Teie teenistuses.
Postitan häid ehtsaid Eesti meme', jagan tarkust ja kaitsen Eesti Vabariiki!
Kirjuta """ + märk + abi_käsk + """ , et saada käske.
NB! Olen ikka veel arengu faasis.
""")
    
#Annab nimekirja käskudest.
@client.group(invoke_without_command=True)
async def help(ctx):
    print("Saadan abi")
    em = discord.Embed(title = "abi", description = "Kasuta .abi <käsklus> täpsema informatsiooni jaoks")
    em.add_field(name = "Käsklused:", value = käsklused)
    
    await ctx.send(embed = em)
#help.commandid muutuvad kompaktsemaks failiga "käsud" skeemil [0] = nimi, [1] = seletus, [2] = kuidas töötab
@help.command()
async def info(ctx):
    em = discord.Embed(title = "info", description = "Saadab Pätsi kohta infot")
    await ctx.send(embed = em)
    
@help.command()
async def abi(ctx):
    em = discord.Embed(title = "abi", description = "Saadab olemas olevad käsud")
    await ctx.send(embed = em)
    
@help.command()
async def uudised(ctx):
    em = discord.Embed(title = "uudised", description = "Saadab mis on uut Pätsiga")
    await ctx.send(embed = em)
    
@help.command()
async def meme(ctx):
    
    em = discord.Embed(title = "meme", description = "Saadab suvalise meme'i")
    await ctx.send(embed = em)

@help.command()
async def rindele(ctx):
    
    em = discord.Embed(title = "rindele", description = "Saadab Eesti noored rindele")
    await ctx.send(embed = em)
    
@help.command()
async def kas(ctx):
    em = discord.Embed(title = "kas", description = "vastab järgevale küsimusele")
    em.add_feild(name = "koostus", value = ".kas <küsimus>")
    await ctx.send(embed = em)
    
@help.command()
async def sus(ctx):
    em = discord.Embed(title = "sus", description = """"kui lauses on fraas "sus""""")
    em.add_feild(name = "koostus", value = "Nt: valit**sus**")
    await ctx.send(embed = em)


#Kontrollib igat sõnumit, kas sõna "päts"(või ka mingi teine sõna) on sees, ja ka vastab sellele(või midagi muud).

@client.event
async def on_message(ctx):
    if "päts" in ctx.content:
        print("Tuvastasin Pätsi")
        await ctx.channel.reply("Olen Konstatin Päts. Eesti Vabariigi esimene president.")
    await client.process_commands(ctx)
    #await ctx.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846390729085026385/pats1.png")

#Käsk, kus äratab kõiki ülesse ja saadab video.
@client.command()
async def rindele(ctx):
    await ctx.channel.purge(limit=1)
    print("Saadan kõik Eesti noored rindele")
    await ctx.send("""
Tiblad ründavad üle Narva Jõe!
Rindele!""")
    await ctx.send("https://cdn.discordapp.com/attachments/625673801627336714/846393632365215764/redditsave.com-wake_up_time-rq1m3f8an9h61.mp4")
    
#Postitab meme'i.
#Võtab failist teksti ja analüüsib neid. Siis võtab suvalise numbri ja valib lingi mida saata.
@client.command()
async def meme(ctx):
    with open("meme.txt") as f:
        lingid = f.read().splitlines()
        #print(lingid)
        print("Saadan meme'i")
        await ctx.send(random.choice(lingid))
#Abort käsk ainult OP võimega
@client.command()
async def abort(ctx):
    if ctx.author == "Tihke Päts#8878":
        print("ABORT!")
        print("Väljun programmist")
        await ctx.send("On algamas tõeline Vaikiv Ajastu.")
        await ctx.channel.purge(limit=1)
        exit()
    await ctx.channel.purge(limit=1)
    msg = """Käsklus ".abort" on sulle keelatud"""
    await ctx.author.send(msg)

@client.event
async def on_message(ctx):
    if "sus" in ctx.content and ".help" not in ctx.content:
        print("Sõnum asendatud petisega")
        await ctx.reply("https://cdn.discordapp.com/attachments/846444798264213534/846466774236528710/boo7iriaha071.png")
    await client.process_commands(ctx)
#timeri setup ja valmimis vastused, global time pole veel lisatud
"""@client.command()
async def alarm(ctx, time):
    now = datetime.datetime.now()
    mtimeA = time
    mtimeB = mtimeA.split(":")
    hr = int(mtimeB[0])
    min = int(mtimeB[1])
    secsleft = int((timedelta(hours=24) - (now - now.replace(hour=hr, minute=min, second=0, microsecond=0))).total_seconds() % (24 * 3600))
    await ctx.send(f"OK\nAlarm set to {time}")
    wait(min)
    def check(message):
        return message.author == ctx.author and message.content.lower() == "cancel alarm"
    try:
        await bot.wait_for("message", check=check, timeout=secsleft)
        await ctx.send("Alarm cancelled")
    except:
        await ctx.send(f"{ctx.author.mention} alarm finished")"""
    

        
#Kasutab tookenid, et boti sisse saada.

client.run(token)

#Koodi lõpp.
