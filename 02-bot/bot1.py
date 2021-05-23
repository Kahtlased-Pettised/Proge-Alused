import discord
    
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!sus':
            await message.channel.send("https://cdn.discordapp.com/attachments/741595512695685181/845414914159935498/e6mr16a9ah071.png")

        if message.content == '!eesti':
            await message.channel.send("piir käib vastu Hiina müüri!")
            
client = MyClient()
client.run('ODQ2MTIzMzY4OTM5OTEzMzA2.YKq7yw.3FYMlGN775hc7a3yz-64H5X9QKQ')