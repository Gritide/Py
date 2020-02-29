import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!Gritide':
            await message.channel.send('(Male High Elf Wizard) Level= 3, Hp= 17, Strength= 8, Dexterity= 10, Constitution= 12 , Intelligence= 16, Wisdom= 15, Charisma= 15' )
            await message.channel.send('https://www.dndbeyond.com/characters/16082964')
        if message.content == '!Xarelto':
            await message.channel.send('(Male Wood Elf Bard) Level= 3, Hp= 18, Strength= 8, Dexterity= 16, Constitution= 10 , Intelligence= 12, Wisdom= 14, Charisma= 15' )
            await message.channel.send('https://www.dndbeyond.com/characters/16082965')
        if message.content == '!Trion':
            await message.channel.send('(Man Human Paladin ) Level= 2, Hp= 14, Strength= 16, Dexterity= 14, Constitution= 9 , Intelligence= 11, Wisdom= 13, Charisma= 15' )
            await message.channel.send('https://www.dndbeyond.com/characters/17047944')
        if message.content == '!YokEdenLokum':
            await message.channel.send('(Male Tiefling Sorcerer ) Level= 2, Hp= 16, Strength= 8, Dexterity= 10, Constitution= 14 , Intelligence= 13, Wisdom= 13, Charisma= 17' )
            await message.channel.send('https://www.dndbeyond.com/characters/16790751')
        if message.content == '!Amon':
            await message.channel.send('(Male Aarakocra Barbarian ) Level= 2, Hp= 20, Strength= 15, Dexterity= 10, Constitution= 10 , Intelligence= 12, Wisdom= 14, Charisma= 14' )
            await message.channel.send('https://www.dndbeyond.com/characters/14923774')
        if message.content == '!Necip Uysal':
            await message.channel.send('(Male Human Rogue ) Level= 1, Hp= 8, Strength= 9, Dexterity= 16, Constitution= 11 , Intelligence= 15, Wisdom= 17, Charisma= 20' )
            await message.channel.send('https://www.dndbeyond.com/characters/16377177')
        if message.content == '!Agis':
            await message.channel.send('(Fluid-Gender Variant Human Wizard) Level= 15, Hp= 77, Strength= 8, Dexterity= 10, Constitution= 12 , Intelligence= 19, Wisdom= 18, Charisma= 13' )
            await message.channel.send('https://www.dndbeyond.com/characters/15847011')
        if message.content == '!Admin':
            await message.channel.send('@Ludens The Admin_Sama.exe' )
        if message.content == '!Putnam':
            await message.channel.send('(Male Half-Orc Rogue) Level= 1, Hp= 10, Strength= 10, Dexterity= 15, Constitution= 14 , Intelligence= 14, Wisdom= 12, Charisma= 10' )
            await message.channel.send('https://www.dndbeyond.com/characters/17142366')
        if message.content == '!Evren':
            await message.channel.send('Alt Diyar' )
        if message.content == '!bilgi':
            await message.channel.send('!evren, !your D&D beyond character name(for stats),!Admin(for admin)' )
        if message.content == '!Stream':
            await message.channel.send('https://www.twitch.tv/kafein_man/' )
        if message.content == '!Hayat':
            await message.channel.send('Zor' )
        if message.content == '!Olivia':
            await message.channel.send(':heart:' )
        if message.content == '!Ulas':
            await message.channel.send(':regional_indicator_u: :regional_indicator_l: :regional_indicator_a: :regional_indicator_s: :heart:' )
        if message.content == '!Huwei':
            await message.channel.send('Toast Kawaii ' )
        if message.content == '!Ludens':
            await message.channel.send('Muhammed Serif Be.... Syntax Error ' )
        if message.content == '!Energy':
            await message.channel.send('Euro Truck Simulator 2 ' )
        
            

client = MyClient()




client.run("NjI3NTM5NjMyMDg2NTgxMjU4.XY-xZg.r7kGzqSOKQxCqnwHXC")
