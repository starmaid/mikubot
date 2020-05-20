# destiny assistant bot for my destiny server
# this one chekcs rss feeds and is meant to run like once every 15 min
# author Nicky (@starmaid#6925)
# created 05/07/2020
# edited 05/20/2020
# version 1.1
# fixed xur location. xurlok is not maintained anymore. understandable tho

import feedparser
import requests
import discord
import json

# look at previous updates
updates_path = './feed_updates.json'
try:
    with open(updates_path, 'r') as fp:
        last_update = json.load(fp)
except:
    last_update = {"hs2": "None"}

# hs2 updates
hs2_update = False
hs2 = feedparser.parse('https://homestuck2.com/story/rss')
title = hs2['entries'][0]['title']
link = hs2['entries'][0]['link']
if last_update['hs2'] != title:
    hs2_update = True
    last = last_update['hs2']
    last_update['hs2'] = title
    pages = 1
    while hs2['entries'][pages]['title'] != last:
        pages += 1
        link = hs2['entries'][pages]['link']

# send the messages maybe
if hs2_update:
    with open(updates_path, 'w') as fp:
        json.dump(last_update, fp)

    client = discord.Client(activity=discord.Game("searching"))

    @client.event
    async def on_ready():
        hs_chan = []
        for g in client.guilds:
            for c in g.channels:
                if c.name == 'h-mestuck':
                    hs_chan.append(c)
        if hs2_update:
            #send a twab update to the twab channel
            for c in hs_chan:
                await c.send('`' + str(pages) + ' MORE PAGES OF NONSENSE:` ' + link)
        await client.close()

    def read_token():
        token = None
        try:
            with open('./token.txt','r') as fp:
                token = fp.readlines()[0].strip('\n')
        except:
            print('Token file not found')
        return token

    token = read_token()
    if token is not None:
        client.run(token)
    else:
        pass
