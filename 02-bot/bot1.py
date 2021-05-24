import discord
import random
    
    
#Tooken
#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!
token = "token" #TOOKEN AAAAAAAAAAAAAAAA
#VÕTA TOOKEN ENNE PUSH'IMIST ÄRA!!! MUIDU DISCORD KARJUB JÄLLE!!!

#Muutujad.
peamine_channel = "bot" #Peamine kanal, kus räägib(Ei tööta praegu, kuna bit viibib mitmes serveris korraga.)
märk = "p!" #Märk, mida bot kasutab arusaamiseks, mis on käsk ja mis ei ole.
paha_sõna = "päts" #Kui see sõna on tekstis, siis kas reageerib, vastab, või kustutab ära. N-ö trigger word.(NB! Reageerimine ja kustutamine ei tööta praegu.)
    
    
#Tekitab klassi, millega logib Discordi sisse, ehk startup.
#Paneb endale staatuse ja kinnitab sisse logimist.
class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(märk + 'info'))
        print('Logged on as', self.user)
        
    #Kui saab sõnumi käivita alumine kood.
    async def on_message(self, message):
        # Ei vasta endale.
        if message.author == self.user:
            return
        
        print(str(message.author) + " / " + str(message.created_at) + " / " + str(message.channel.name) + " / " + str(message.content) + " / ")
        #Ping käsk testimiseks.
        if message.content == märk + 'ping': # and message.channel.name == peamine_channel:
            await message.channel.send("pong")
        
        #Annab infot boti kohta.
        if message.content == märk + 'info': #and message.channel.name == peamine_channel:
            print("Saadan infot")
            #await message.add_reaction("U+1F35E")
            await message.channel.send("Olen kõikvõimas Konstatin Päts, Teie teenistuses.")
            await message.channel.send("Postitan häid ehtsaid Eesti meme', ennustan tulevikku, jagan muusikat ja palju veel!'")
            await message.channel.send("Kirjuta " + märk + "abi, et saada käske.")
            await message.channel.send("NB! Olen ikka veel arengu faasis.")
            
        #Annab nimekirja käskedest.
        if message.content == märk + "abi":
            print("Saadan abi")
            await message.channel.send("Käskude nimekiri: ")
            await message.channel.send(märk + "info - Saadab Pätsi boti kohta infot.")
            await message.channel.send(märk + "abi - Saadab käskude nimekirja.")
            #await message.channel.send("p!rindele - Ättib kõike.)
            await message.channel.send(märk + "meme - Saadab Eesti meme'.")
            
        #Kontrollib igat sõnumit, kas sõna "päts"(või ka mngi teine sõna) on sees, ja ka vastab sellele.(POOLELI)
        if paha_sõna in message.content.lower():
            await message.reply("Olen Konstatin Päts. Eesti Vabariigi esimene president.")
            #await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846390729085026385/pats1.png")
            
        #Rindele käsk, kus äratab kõiki ülesse ja saadab video.
        if message.content == märk + "rindele":
            print("Saadan kõiki rindele")
            await message.channel.send("@everyone")
            await message.channel.send("Rindele!")
            await message.channel.send("Tiblad ründavad üle Narva jõe!")
            await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846393632365215764/redditsave.com-wake_up_time-rq1m3f8an9h61.mp4")
            
        #Postitab meme'i.
        #Võtab failist teksti ja analüüsib neid. Siis võtab suvalise numbri ja valib lingi mida saata.
        if message.content == märk + "meme":
            with open("meme.txt") as f:
                lingid = f.read().splitlines()
                #print(lingid)
                print("Saadan meme'i")
                await message.channel.send(random.choice(lingid))
           
        #Muusika
                
                
        #Faktid
                
                
        #Tuleviku ennustamine(JAH;EI vastused)
                
                
        #Äratuskell
                
        
#Kasutab tookenid, et boti sisse saada
client = MyClient()
client.run(token)