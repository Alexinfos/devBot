import discord
from discord.ext.commands import bot
from discord.ext import commands
from datetime import datetime
import asyncio
import time
import emoji
import aide
import argslist
import pkmn

Client = discord.Client()
client = commands.Bot(command_prefix = "d.")

## PLEASE PUT YOUR OWN DEBUG CHANNEL ID HERE
test_channel = 0000

## -------------------[ Initialisation ] ------------------
global lastHelpSession

@client.event
async def on_ready():
      print("DevBot (re)démarré avec succès [" + str(datetime.now()) + "]")
      await client.change_presence(activity=discord.Game(name='Aide: d.help'))
      lastHelpSession = await client.get_channel(test_channel).send(":white_check_mark:  (Re)démarrage de DevBot accompli avec succès !")
      lastHelpSession.id = None
      await client.user.edit(username="DevBot")

## -----[ Détection d'envoi de message ] -----
@client.event
async def on_message(message):
      global pokemonBattle
      global pokemonBattleData
      global lastHelpSession
      if message.channel == client.get_channel(test_channel):
            ##print("test")
            return
      elif not 'pokemonBattle' in globals():
            lastHelpSession = await client.get_channel(test_channel).send("LastHelpSession object generated")
            ##print("généré")
            pokemonBattle = []
            pokemonBattle.append(lastHelpSession)
            pokemonBattle.append(None)
            pokemonBattle.append(None)
            pokemonBattle[0].id = None
##      await message.add_reaction(emoji.emojize(':fish:', use_aliases=True)) ##1er Avril 2018
      if message.content.lower().startswith('clap'):
            args = message.content.split(" ")
            if len(args) > 1:
                  try:
                        nbClap = int(args[1])
                  except ValueError:
                        nbClap = 0
                        pass
                  if args[1].lower() == "bonjour":
                        await message.channel.send(file=discord.File('ressources/clapbonjour.mp4', 'clapbonjour.mp4'))
                  elif nbClap > 0 and nbClap < 26:
                        clapArray = []
                        while (nbClap > 0) :
                              clapArray.append(":clap:")
                              nbClap = nbClap - 1
                        await message.channel.send(" ".join(clapArray[0:]))
                  elif nbClap > 25:
                        print(message.author, " a entré la commande clap [nb] avec un argument illégal (supérieur à 25): ", nbClap)
                        await message.channel.send(":no_entry_sign: <@%s>, impossible de lancer la commande clap [nb] avec l'argument illégal (strictement supérieur à 25) %s. Essayez de lancer la commande avec un argument valide (supérieur à 0 et inférieur à 26)" % (message.author.id,nbClap))
                  else:
                        await message.channel.send(":clap: %s" % (" ".join(args[1:])))
            else:
                  await message.channel.send(":clap: %s" % (" ".join(args[1:])))
      elif message.content.lower().startswith("d.help"):
            if not 'lastHelpSession' in globals():
                  lastHelpSession.id = None
            await aide.closeLastSession(client, message, lastHelpSession, "bot", None)
            args = message.content.split(" ")
            if len(args) > 1:
                  lastHelpSession = await aide.command(args[1], client, message, lastHelpSession)
            else:
                  lastHelpSession = await aide.page1(client, message, lastHelpSession)
      elif message.content.lower().startswith("d.arguments"):
##            if not 'lastHelpSession' in globals():
##                  lastHelpSession = None
##            await aide.closeLastSession(client, message, lastHelpSession, "bot", None)
##            lastHelpSession = None
##            args = message.content.split(" ")
##            if len(args) > 1:
##                  lastHelpSession = await argslist.dictionnary(args[1], client, message, lastHelpSession)
##            else:
##                  lastHelpSession = await aide.command("arguments", client, message, lastHelpSession)
            await message.channel.send("Commande bientôt disponible...")
            userInfos = await client.get_user_info(message.author.id)
            print(userInfos.name + " (" + message.author.id + ") a tenté d'exécuter la commande d.arguments qui n'est pas encore disponible.")
      elif message.content.lower().startswith("d.battle"):
            if not 'pokemonBattle' in globals():
                  pokemonBattle = []
                  pokemonBattle.append(lastHelpSession)
                  pokemonBattle.append(None)
                  pokemonBattle.append(None)
                  pokemonBattle[0].id = None
            args = message.content.split(" ")
            if len(args) > 1:
                  pokemonBattle = await pkmn.setupBattle(client, message, pokemonBattle, args)
                  pokemonBattleData = []
                  ##print(pokemonBattle)
            else:
                  lastHelpSession = await aide.command("d.battle", client, message, lastHelpSession)
      elif message.content.lower().startswith("d.info"):
            args = message.content.split(" ")
            print(args[1:])
      elif message.content.lower().startswith("martin.off"): ## En souvenir du voyage à Berlin: 16/04/18 au 20/04/18 ("rédaction de français" écrite en direct de la fernsehturm)
            await message.channel.send("Martin s'est tut !")
      elif message.content.lower().startswith("martin.on"): ## En souvenir du voyage à Berlin: 16/04/18 au 20/04/18 (développé le samedi à la maison)
            await message.channel.send("Martin parle à nouveau !")
      elif message.content.lower().startswith("lucas.off"): 
            await message.channel.send("Lucas s'est tut !")
      elif message.content.lower().startswith("lucas.on"): 
            await message.channel.send("Lucas parle à nouveau !")

## -----[ Détection d'ajout de réaction ] -----
@client.event
async def on_reaction_add(reaction, user):
      message = reaction.message
      ##print(pokemonBattle[1])
      if not 'lastHelpSession' in globals():
            lastHelpSession.id = None
            print("lastHelpSession reset")
      if not 'pokemonBattleData' in globals():
            print("pokemonBattleData reset")
            global pokemonBattleData
            pokemonBattleData = []
            pokemonBattleData.append("None")
      if reaction.emoji == emoji.emojize(':x:', use_aliases=True) and message.id == lastHelpSession.id and user.id != client.user.id:
            await aide.closeLastSession(client, message, lastHelpSession, "user", user.id)
      if  message.id == pokemonBattle[0].id and (user.id == pokemonBattle[1] or user.id == pokemonBattle[2]):
            pokemonBattleData = await pkmn.checkReaction(client, pokemonBattle, pokemonBattleData, emoji.demojize(reaction.emoji), user.id)
            

## PLEASE PUT YOUR OWN DISCORD BOT TOKEN HERE
client.run("BOT-TOKEN")
