#Discord boti "Päts"-i kood.
#Koodi tegid Kahtlased Pettised: Kaimar Kangur, Henry Ploom ja Sten Voronin.
#Bot ja selle tooken on Kaimari käes.

#Koodi algus

#Importib vajalikud teemad sisse.
import discord
import random
import time
     
#Tooken
#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!
token = "token" #TOOKEN AAAAAAAAAAAAAAAA
#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!

#Muutujad.
peamine_channel = "bot" #Peamine kanal, kus räägib ja vaatab sõnumeid(Ei tööta praegu, kuna bot viibib mitmes serveris korraga.)
märk = "p!" #Märk, mida bot kasutab arusaamiseks, mis on käsk ja mis ei ole.
paha_sõna = "päts" #Kui see sõna on tekstis, siis kas reageerib, vastab, või kustutab ära. N-ö trigger word.(NB! Reageerimine ja kustutamine ei tööta praegu.)
    
#Käsud(Kasuta neid, kui koodid midagi uut)
info_käsk = "info"
abi_käsk = "abi"
ping_käsk = "ping"
meme_käsk = "meme"
rindele_käsk = "rindele"
muusika_käsk = "muusika"
äratuskell_käsk = "kell"
faktid_käsk = "fakt"
küsimus_käsk = "küs"
uudis_käsk = "uut"
sus_käsk = "sus"

#Tekitab klassi, millega logib Discordi sisse, ehk startup.
#Paneb endale staatuse ja kinnitab sisse logimist.
class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(märk + info_käsk))
        print('Logged on as', self.user)
        
    #Kui saab sõnumi käivita alumine kood.
    async def on_message(self, message):
        # Ei vasta endale.
        if message.author == self.user:
            return
        
        #Prindib kes saatis sõnumi, kunas, kuhu kohta ja mis oli sõnum.
        print(str(message.author) + " / " + str(message.created_at) + " / " + str(message.channel.name) + " / " + str(message.content) + " / ")
        
        #Ping käsk testimiseks.
        if message.content == märk + ping_käsk: # and message.channel.name == peamine_channel:
            print("Saadan teate")
            await message.channel.send("pong")
        
        #Annab kasutajale teada, mis on uut Pätsiga.
        if message.content == märk + uudis_käsk:
            print("Saadan uudiseid")
            await message.channel.send("Teataja uudised: ")
            await message.channel.send("Bot versioon 0.3")
            await message.channel.send("1. Lisatud uudiste funktsioon")
            await message.channel.send("2. Rohkem meme")
            await message.channel.send("3. Päts suudab tuvastada, kuna temast räägitakse ja vastab sellele")
            await message.channel.send("*Viimati muudetud 24.05.21*")
        
        #Annab infot boti kohta.
        if message.content == märk + info_käsk: #and message.channel.name == peamine_channel:
            print("Saadan infot")
            #await message.add_reaction("U+1F35E")
            await message.channel.send("Olen kõikvõimas Konstatin Päts, Teie teenistuses.")
            await message.channel.send("Postitan häid ehtsaid Eesti meme', ennustan tulevikku, jagan muusikat ja palju veel!")
            await message.channel.send("Kirjuta " + märk + abi_käsk + " , et saada käske.")
            await message.channel.send("NB! Olen ikka veel arengu faasis.")
            
        #Annab nimekirja käskedest.
        if message.content == märk + abi_käsk:
            print("Saadan abi")
            await message.channel.send("Käskude nimekiri: ")
            await message.channel.send(märk + info_käsk + " - Saadab Pätsi boti kohta infot.")
            await message.channel.send(märk + abi_käsk + " - Saadab käskude nimekirja.")
            await message.channel.send(märk + uudis_käsk + " - Mis uut Pätsiga.")
            #await message.channel.send("p!rindele - Ättib kõike.)
            await message.channel.send(märk + meme_käsk + " - Saadab Eesti meme'.")
            
        #Kontrollib igat sõnumit, kas sõna "päts"(või ka mingi teine sõna) on sees, ja ka vastab sellele(või midagi muud).
        if paha_sõna in message.content.lower():
            print("Tuvastasin Pätsi")
            await message.reply("Olen Konstatin Päts. Eesti Vabariigi esimene president.")
            #await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846390729085026385/pats1.png")
            
        #Käsk, kus äratab kõiki ülesse ja saadab video.
        if message.content == märk + rindele_käsk:
            print("Saadan kõik Eesti noored rindele")
            await message.channel.send("@everyone")
            await message.channel.send("Tiblad ründavad üle Narva jõe!")
            await message.channel.send("Rindele!")
            await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846393632365215764/redditsave.com-wake_up_time-rq1m3f8an9h61.mp4")
            
        #Postitab meme'i.
        #Võtab failist teksti ja analüüsib neid. Siis võtab suvalise numbri ja valib lingi mida saata.
        if message.content == märk + meme_käsk:
            with open("meme.txt") as f:
                lingid = f.read().splitlines()
                #print(lingid)
                print("Saadan meme'i")
                await message.channel.send(random.choice(lingid))
           
        #Sus
        if message.content == märk + sus_käsk:
                await message.delete()
                print("Sõnum kustutatud")
                await message.channel.send("https://cdn.discordapp.com/attachments/846444798264213534/846466774236528710/boo7iriaha071.png")
                print("Petis saadetud")
           
           
        #Muusika(saadab lingi)
                
                
        #Faktid(Eestist ja Pätsist)
                
                
        #Tuleviku ennustamine(JAH;EI vastused näiteks)
                
                
        #Äratuskell
        #Kasutaja kasutab käsku, et Päts saaks aru mida saata.
        #Päts saadab soovitud teksti(või ka pildi, kui õnnestub), mingil suvalisel tunnil(saab ka, et iga tund mingi protsent väärtus).
        
        
        #Mingi API funktsioon
        #Töötab nagu meme käsk, aga kasutades välist API'd ja infot.
                
        
#Kasutab tookenid, et boti sisse saada.
client = MyClient()
client.run(token)

#Koodi lõpp. ):