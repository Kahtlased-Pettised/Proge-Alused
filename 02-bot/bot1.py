#Discord boti "Päts"-i kood.
#Koodi tegid Kahtlased Pettised: Kaimar Kangur, Henry Ploom ja Sten Voronin.
#Bot ja selle tooken on Kaimari käes.

#Koodi algus

#Importib vajalikud teemad sisse.
import discord
import random
import time
import datetime
     
#Autentimistooken

#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!
token = "ODQ2MTIzMzY4OTM5OTEzMzA2.YKq7yw.hhke1b2n_Lx55V9os7bD2GGsc0Q" #TOOKEN AAAAAAAAAAAAAAAA
#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!

#Muutujad.
peamine_channel = "bot" #Peamine kanal, kus räägib ja vaatab sõnumeid(Ei tööta praegu, kuna bot viibib mitmes serveris korraga.)
märk = "p!" #Märk, mida bot kasutab arusaamiseks, mis on käsk ja mis ei ole.
paha_sõna = "päts" #Kui see sõna on tekstis, siis kas reageerib, vastab, või kustutab ära. N-ö trigger word.(NB! Reageerimine ja kustutamine ei tööta praegu.)
    
#Käsud(Kasuta neid, kui koodid midagi uut)
info_käsk = "info"
abi_käsk = "abi"
ping_käsk = "ping"
meme_käsk = "meem"
rindele_käsk = "rindele"
muusika_käsk = "muusika" #POOLELI
äratuskell_käsk = "äratus" #POOLELI
faktid_käsk = "fakt" #POOLELI
küs_käsk = "k" 
uudis_käsk = "uudised"
#sus_käsk = "sus"
elagu_käsk = "elagu" #POOLELI
abort_käsk = "abort" #POOLELI
bread_käsk = "bread"
susmeme_käsk = "amogus"
räägi_käsk = "r"

#Tekitab klassi, millega logib Discordi sisse, ehk startup.
#Paneb endale staatuse ja kinnitab sisse logimist.
class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(märk + abi_käsk))
        print('Logged on as', self.user)
        
    #Kui saab sõnumi käivita alumine kood.
    async def on_message(self, message):
        # Ei vasta endale.
        if message.author == self.user:
            return
        
        """global kella_soovija
        global saadetud_käsk
        
        global kell
        global äratus_sisu
        global äratus_aeg
        
        #kella_soovija = "test"
        #saadetud_käsk = "test"
        kell = False"""
        
        #Prindib kes saatis sõnumi, kunas, kuhu kohta ja mis oli sõnum.
        print(str(message.author) + " / " + str(message.created_at) + " / " + str(message.channel.name) + " / " + str(message.content) + " / ")
        
        #Ping käsk testimiseks.
        if message.content == märk + ping_käsk: # and message.channel.name == peamine_channel:
            print("Saadan teate")
            await message.channel.send("pong")
        
        #Annab kasutajale teada, mis on uut Pätsiga.
        if message.content == märk + uudis_käsk:
            print("Saadan uudiseid")
            await message.channel.send("""
Teataja uudised: 
1. Oskab rääkida teksti
2. Oskab vastata erinevatele küsimustele

(*Viimati muudetud 29.05.21*)
                                        """)
            
        #Annab infot boti kohta.
        if message.content == märk + info_käsk: #and message.channel.name == peamine_channel:
            print("Saadan infot")
            #await message.add_reaction("U+1F35E")
            await message.channel.send("""
Olen kõikvõimas Konstatin Päts, Teie teenistuses.
Postitan häid ehtsaid Eesti meeme, jagan tarkust ja kaitsen Eesti Vabariiki!
Kirjuta """ + märk + abi_käsk + """ , et saada käske.
NB! Olen ikka veel arengu faasis.
""")
            
        #Annab nimekirja käskedest.
        if message.content == märk + abi_käsk:
            print("Saadan abi")
            await message.channel.send("""
Käsud:
""" + märk + info_käsk + """ - Saadab Pätsi boti kohta infot.
""" + märk + abi_käsk + """ - Saadab käskude nimekirja.
""" + märk + uudis_käsk + """ - Mis uut Pätsiga.
""" + märk + meme_käsk + """ - Saadab Eesti meeme.
""" + märk + küs_käsk + """ - Saad küsida Pätsi käest küsimuse.
""" + märk + bread_käsk + """ - Saadab leiva pildi.
""" + märk + susmeme_käsk + """ - Saadab amogus sus meeme.
""" + märk + räägi_käsk + """ - Räägin sinu teksti.
""")

        #Kontrollib igat sõnumit, kas sõna "päts"(või ka mingi teine sõna) on sees, ja ka vastab sellele(või midagi muud).
        if paha_sõna in message.content.lower():
            print("Tuvastasin Pätsi")
            await message.reply("Olen Konstatin Päts. Eesti Vabariigi esimene president.")
            #await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846390729085026385/pats1.png")
            
        #Käsk, kus äratab kõiki ülesse ja saadab video.
        if message.content == märk + rindele_käsk:
            await message.delete()
            print("Saadan kõik Eesti noored rindele")
            await message.channel.send("""
Tiblad ründavad üle Narva Jõe!
Rindele!
""")
            await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846393632365215764/redditsave.com-wake_up_time-rq1m3f8an9h61.mp4")
            
        #Postitab meme'i.
        #Võtab failist teksti ja analüüsib neid. Siis võtab suvalise numbri ja valib lingi mida saata.
        if message.content == märk + meme_käsk:
            with open("meme.txt") as f1:
                lingid = f1.read().splitlines()
                #print(lingid)
                print("Saadan meemi")
                await message.channel.send(random.choice(lingid))
           
        #Sus
        if "sus" in message.content.lower():
                #await message.delete()
                #print("Sõnum kustutatud")
                await message.reply("https://cdn.discordapp.com/attachments/846444798264213534/846466774236528710/boo7iriaha071.png")
                print("Petis saadetud")
           
           
        #Muusika(saadab lingi)
                
            
        #Faktid(Eestist ja Pätsist)
                
        
        #Äratuskell
        #Kasutaja kasutab käsku, et Päts saaks aru mida saata.
        #Päts saadab soovitud teksti(või ka pildi, kui õnnestub), mingil suvalisel tunnil(saab ka, et iga tund mingi protsent väärtus).
        """if message.content == märk + äratuskell_käsk:
            kella_soovija = message.author
            saadetud_käsk = message.created_at
            
            print("Äratuskella käsk")
            print(kella_soovija)
            print(message.created_at)
            
            kell = True
            print(kell)
            await message.send("Järgmine sõnum on Teie äratuse sisu.")
            
        if kell == True:
            if message.created_at > saadetud_käsk and message.author == kella_soovija:
                print(str(kella_soovija) + " soovib äratust")
                sleep(1000)
                await message.reply("Saadan selle sõnumi tunni pärast")
                äratus_sisu = message.content
                #äratuse_aeg = """
        #Mingi API funktsioon
        #Töötab nagu meme käsk, aga kasutades välist API'd ja infot.
            
        
        #Abort käsk
        if message.content == märk + abort_käsk: # and message.author == "Tihke Päts#8878":
            await message.delete()
            #await message.reply("On algamas tõeline Vaikiv Ajastu.")
            print("ABORT!")
            print("Väljun programmist")
            exit()
            
        #Küsimuste vastaja
        if message.content.startswith(märk + küs_käsk) and message.content.endswith("?"):
            if "kas" in message.content.lower():
                print("Saadan vastuse")
                await message.reply(random.choice(["Jah","Loomulikult mitte","Võibolla","Loll küsimus, ei vasta", "Tahad vangi minna või?", ";)"]))
            if "mis" in message.content.lower():
                print("Saadan vastuse")
                await message.reply(random.choice(["Vähemalt kaks", "Su ema",""]))
            if "miks" in message.content.lower():
                print("Saadan vastuse")
                await message.reply(random.choice(["Sest koera nimi on Rex","Seks", "Kuna Eesti on võimas", "Sest tal suured tissid"]))
            
        #Saadab leiva meme'i
        if message.content == märk + bread_käsk:
            print("Kustutan sõnumi")
            await message.delete()
            print("Saadan leiva")
            await message.channel.send("https://cdn.discordapp.com/attachments/846444798264213534/847123858594856970/bread.png")
        
        #Saadab erinevaid variante sus meemist
        if message.content == märk + susmeme_käsk:
            with open("sus_meme.txt") as f2:
                sus_lingid = f2.read().splitlines()
                await message.delete()
                #print(lingid)
                print("Saadan sus meemi")
                await message.channel.send(random.choice(sus_lingid))
                
            #Ütleb seda mida kasutaja ütleb talle.
        if message.content.startswith(märk + räägi_käsk):
            räägi_info = message.content.split(" ")
            #räägi_tekst = räägi_info[1]
            räägi_info.remove("p!r")
            await message.delete()
            #print(räägi_info)
            räägi_tekst = " ".join(räägi_info)
            print("Räägin " + str(räägi_tekst))
            #await message.channel.send(str(räägi_info)[1:-1])
            await message.channel.send(räägi_tekst)
                
#Kasutab tookenid, et boti sisse saada.
client = MyClient()
client.run(token)

#Koodi lõpp.