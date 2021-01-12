
import discord
import os
import requests
import json
from stay_up import stay_up
import time
#creates instance of client
client = discord.Client()

def get_age(name):

  response = requests.get("https://api.agify.io/?name=" + name + "&country_id=US")

  json_data = json.loads(response.text)
  age = "The name " + json_data['name'] + " is on average " + str(json_data['age']) + " years old in " + json_data['country_id']

  return (age)

def get_joke():
  response = requests.get("https://official-joke-api.appspot.com/random_joke")

  json_data = json.loads(response.text)
  return (json_data)

def get_anime():
  response = requests.get("https://animechanapi.xyz/api/quotes/random")

  json_data = json.loads(response.text)
  anime = json_data['data']
  #+ " -" + json_data['character'] + " from " + json_data['anime']
  real_anime = anime[0]['quote'] + " -" + anime[0]['character'] + " from " + anime[0]['anime']
  return(real_anime)

def get_zen():
  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)
  zen = json_data[0]['q']  +  " -" + json_data[0]['a']

  return(zen)

#event that happens once bot is ready
@client.event
#^^^ registers event
async def on_ready():
  print('{0.user} has arrived'.format(client))

#event if bot sees message
@client.event
async def on_message(message):
  if message.content.startswith('#age'):
    channel = message.channel
    await channel.send("Please tell me your name")
    name = await client.wait_for('message')
    my_name = name.content
    age = get_age(my_name)
    #sends a dictionary
    await message.channel.send(age)
  
  elif message.author == client.user:
    return

  elif message.content.startswith('#quote'):
     zen = get_zen()
     await message.channel.send(zen)

  elif message.content.startswith('#anime'):
    anime = get_anime()
    await message.channel.send(anime)
    
  elif message.content.startswith('#help'):
    await message.channel.send("just type some stuff for fun #age, #quote #anime ")
  
  elif message.content.startswith('#joke'):
    joke = get_joke()
    await message.channel.send(joke['setup'])
    for i in range(3):
      await message.channel.send("...")
      time.sleep(1)
      i += 1
    await message.channel.send(joke['punchline'])

#places the token into an environmental variable to be private and then calls it
stay_up()
client.run(os.getenv('TOKEN'))
