# anti homestuck bot for gwens server
# author Nicky (@starmaid#6925)
# created 03/21/2020
# edited 03/21/2020
# version 1.0.0

import discord
from discord.ext import commands
import random

class Bot(commands.Bot):
    phrases = [
        'miku',
        'hatsune'
    ]
    replies = [
        'its me, miku!',
        '\\*peace signs\\*'
    ]
    homestuck = [
        'homestuck',
        'hs',
        'vriska',
        'terezi',
        'karkat'
    ]
    hs_replies = [
        'STOP THAT',
        'STOP DEFILING THIS CHAT',
        '\\*smacks you over the head\\*'
    ]
    activity = 'viddy gaem'
    logoff_msg = 'logging off :3'

    def __init__(self):
        # This is the stuff that gets run at startup
        super().__init__(command_prefix='/',self_bot=False,activity=discord.Game(self.activity))
        random.seed()
        self.quit_val = random.randint(100000000000,999999999999)
        self.remove_command('help')
        self.read_token()
        if self.token is not None:
            super().run(self.token)
        else:
            pass

    def read_token(self):
        self.token = None
        try:
            with open('./token.txt','r') as fp:
                self.token = fp.readlines()[0].strip('\n')
        except:
            pass
        try:
            if self.token is None:
                with open('./mikubot/token.txt','r') as fp:
                    self.token = fp.readlines()[0].strip('\n')
        except:
            print("Token file not found")

    async def on_ready(self):
        # This creates the quitval and saves it to my server
        print("Logged on")
        print(self.quit_val)
        #with open("char_" + str(self.quit_val),"w") as file:
        #    file.write(str(self.quit_val))

    async def on_message(self, message):
        # this function is executed when a message is recieved
        if message.author == self.user:
            # ignore yourself
            return
        # turn the whole message lowercase
        contents = message.clean_content.lower()
        contents.split(' ')
        # finds where the message came from
        channel = message.channel

        # Checks the contents against the predefined phrases
        for phrase in self.phrases:
            if phrase in contents:
                # replies with a generated keysmash
                await channel.send(self.replies[random.randint(0,len(self.replies)-1)])
                return

        if str(channel.name) != 'h-mestuck':
            for h in self.homestuck:
                if h in contents:
                    await channel.send(self.hs_replies[random.randint(0,len(self.hs_replies)-1)])

        if str(self.quit_val) in contents:
            await channel.send(self.logoff_msg)
            await self.close()


if __name__ == '__main__':
    Bot()
