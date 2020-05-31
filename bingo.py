#!/usr/bin/env python3

import random as rn
from dotenv import load_dotenv
import asyncio
import discord
import os
import sys
import time

client = discord.Client()

load_dotenv() # to run this you need to get the dotenv lib and make a .env file (or load in your token the way you want to)
TOKEN=os.getenv('DISCORD_TOKEN')

async def main(message):
    Numbs={ 
        1:"Kelly's Eye",
        2:"One little duck | Me and you",
        3:"Cup of tea | You and me",
        4:"knock on the door",
        5:"Man alive",
        6:"Tom Mix | Half a Dozen",
        7:"Lucky",
        8:"Garden Gate",
        9:"Doctors Orders",
        10:"Boris's Den",
        11:"legs eleven",
        12:"A Dozen",
        13: "Unlucky for some",
        14:"The lawnmower",
        15:"Young and Keen",
        16:"Never been kissed",
        17:"Pete Shuffle",
        18:"Coming of age",
        19:"Goodbye Teens",
        20:"One score | Getting Plenty",
        21:"Key of the Door",
        22:"Two Little Ducks",
        23:"The lord is my shepard",
        24:"A double Dozen",
        25:"Duck and a Dive",
        26:"Two and six, half a crown | A to Z",
        27:"Duck and a Crutch",
        28:"In a State",
        29:"Rise and shine",
        30:"Burlington Bertie | Dirty Gertie",
        31:"Get up and run",
        32:"buckle my shoe",
        33:"All the Threes | Fish Chips and Peas",
        34:"Ask for more",
        35:"jump and jive",
        36:"triple dozen",
        37:"A lonely one",
        38:"Christmas cake",
        39:"steps",
        40:"Life Begins",
        41:"A lonely one",
        42:"A lonely one",
        43:"Down on your knees",
        44:"Droopy drawers",
        45:"Half way there",
        46:"Up to tricks",
        47:"A lonely one",
        48:"Four Dozen",
        49:"PC",
        50:"It's a bullseye! | Snow white",
        51:"A lonely one",
        52:"Chicken vindaloo | Danny La Rue | Deck of Cards",
        53:"Here comes Herbie",
        54:"Man at the Door",
        55:"All the fives",
        56:"shottes Bus",
        57:"Heinz Varieties",
        58:"A lonely one",
        59:"The brighton line",
        60:"Grandmas Getting Frisky",
        61:"A lonely one",
        62:"tickity boo",
        63:"Katie's bad knee",
        64:"Almost Retired",
        65:"Stop Working!",
        66:"Clickety click |Trent Alexander-Arnold",
        67:"Stairway to heaven",
        68:"Pick a mate",
        69:"Anyway up, Meal for Two, A Favourite of mine | NICE",
        70:"A lonely one",
        71:"Bang on a drum",
        72:"Dannny La Rue",
        73:"Queen Bee. Under The Tree. Lucky 3",
        74:"Hit the floor",
        75:"A lonely one",
        76:"Trombones | Was she worth it?",
        77:"Two Little crutches | Sunset strip",
        78:"39 more steps",
        80:"Gandhi's Breakfast ",
        81:"fat lady with a walking stick",
        82:"I'm gonna get more right than you ",
        83:"Time for tea",
        84:"Seven Dozen",
        85:"Stayin Alive",
        86:"Between the sticks",
        87:"Torquay to devon",
        88:"two fat ladys",
        89:"Nearly There",
        90:"Top of the shop",
        91:"A lonely one",
        92:"A lonely one",
        93:"A lonely one",
        94:"A lonely one",
        95:"A lonely one",
        96:"A lonely one",
        97:"A lonely one",
        98:"A lonely one",
        99:"A lonely one",
        100:"A lonely one",
    }

    exi = False

    while exi != True:
        if bool(Numbs) == False:
            break
        else:
            num = rn.choice(list(Numbs.keys())) ## selects a random key from the Numbs dictionary and putes it in num
            output = Numbs[num] +" "+ str(num)
            print(output)
            time.sleep(1)
            await message.channel.send(output)
            del Numbs[num]

    print("done")
    await message.channel.send("No More Numbers!")
    await client.logout()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bingo'):
        await message.channel.send("We are Playing bingo!")
        await main(message)
        

client.run(TOKEN)

