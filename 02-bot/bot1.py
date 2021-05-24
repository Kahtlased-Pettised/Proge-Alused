import discord
import random
    
token = "token"
peamine_channel = "bot"
mark = "p!"
    
class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game('Kaitsen Eesti Vabariiki'))
        print('Logged on as', self.user)
        
        
    async def on_message(self, message):
        # Ei vasta endale
        if message.author == self.user:
            return
        
        print(message.author, message.content, message.channel.name)
        #Ping käsk testimiseks.
        if message.content == mark + 'ping': # and message.channel.name == peamine_channel:
            await message.channel.send("pong")
        
        #Annab infot boti kohta.
        if message.content == mark + 'info': #and message.channel.name == peamine_channel:
            print("Saadan infot")
            await message.channel.send("Olen kõikvõimas Konstatin Päts, Teie teenistuses.")
            await message.channel.send("Postitan häid ehtsaid Eesti meme',ennustan tulevikku, jagan muusikat ja palu veel!'")
            await message.channel.send("Kirjuta e!abi, et saada käske.")
            #await message.add_reaction("U+1F35E")

        #Annab nimekirja käskedest.
        if message.content == mark + "abi":
            print("Saadan abi")
            await message.channel.send("Käskude nimekiri: ")
            await message.channel.send("e!info - Saadab Pätsi boti kohta infot.")
            await message.channel.send("e!abi - Saadab käskude nimekirja.")
            await message.channel.send("e!rindele - Ättib kõike, et äratada neid ülesse, et Eestit kaitsma minna.")
            await message.channel.send("e!meme - Saadab Eesti meme'.")
            
        #Kontrollib igat sõnumit, kas sõna "päts" on sees, ja ka vastab sellele.(POOLELI)
        if message.content.lower() == "päts":
            await message.channel.send("Olen Päts")
            #await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846390729085026385/pats1.png")
            
        #Rindele käsk, kus saadab pildi.
        if message.content == mark + "rindele":
            print("Saadan kõiki rindele")
            await message.channel.send("@everyone")
            await message.channel.send("Rindele!")
            await message.channel.send("Tiblad ründavad üle Narva jõe!")
            await message.channel.send("https://cdn.discordapp.com/attachments/625673801627336714/846393632365215764/redditsave.com-wake_up_time-rq1m3f8an9h61.mp4")
            
        #Postitab meme'i
        if message.content == mark + "meme":
            with open("meme.txt") as f:
                lingid = f.read().splitlines()
                #print(lingid)
                print("Saadan meme'i")
                await message.channel.send(random.choice(lingid))
                
        #Tuleviku ennustamine
                
        #Äratuskell
                
                
client = MyClient()
client.run(token)