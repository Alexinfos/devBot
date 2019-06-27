import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import emoji

global version
version = "alpha 0.4.1"


async def setupBattle(client, message, pokemonBattle, args):
      guestPlayer = await client.fetch_user(args[1][-19:-1])
      hostPlayer = message.author.id
      hostUserInfo = await client.fetch_user(hostPlayer)
      description = message.author.name + " défie " + guestPlayer.name + " dans un combat pokémon."
      title = emoji.emojize(':exclamation:', use_aliases=True) + " Combat Pokémon"
      
      embed = discord.Embed(title=title, description=description, color=0x00c8ff)
      embed.add_field(name=guestPlayer.name + ", êtes vous prêt pour un combat ?", value="Répondez avec les réactions ci-dessous.", inline=True)
      await message.channel.send(guestPlayer.mention + " " + hostUserInfo.mention)
      sentMessage = await message.channel.send(embed=embed)
      
      await sentMessage.add_reaction(emoji.emojize(':white_check_mark:', use_aliases=True))
      await sentMessage.add_reaction(emoji.emojize(':x:', use_aliases=True))
      
      pokemonBattle = []
      pokemonBattle.append(sentMessage)
      pokemonBattle.append(guestPlayer.id)
      pokemonBattle.append(hostPlayer)
      return pokemonBattle


async def startBattle(client, pokemonBattle, userId):
      message = pokemonBattle[0]
      guestFighter = pokemonBattle[1]
      hostPlayer = pokemonBattle[2]
      await message.remove_reaction(emoji.emojize(':x:', use_aliases=True), message.guild.me)
      await message.remove_reaction(emoji.emojize(':white_check_mark:', use_aliases=True), message.guild.get_member(userId))
      await message.remove_reaction(emoji.emojize(':white_check_mark:', use_aliases=True), message.guild.me)
      print("Starting battle")
      global healthGuest
      global healthHost
      global turn
      global pokemonBattleState
      global nextPlayer
      healthGuest = healthHost = 500
      turn = 0
      nextPlayer = guestFighter
      lastAction = None
      damages = None
      pokemonBattleData = []
      pokemonBattleData.append(healthGuest)
      pokemonBattleData.append(healthHost)
      pokemonBattleData.append(turn)
      pokemonBattleData.append(nextPlayer)
      pokemonBattleData.append(lastAction)
      pokemonBattleData.append(damages)
      print(pokemonBattleData)
      return pokemonBattleData

async def cancelBattle(client, pokemonBattle, userId, botId):
      message = pokemonBattle[0]
      guestFighter = pokemonBattle[1]
      hostPlayer = pokemonBattle[2]
      await message.remove_reaction(emoji.emojize(':x:', use_aliases=True), message.guild.get_member(userId))
      await message.remove_reaction(emoji.emojize(':white_check_mark:', use_aliases=True), message.guild.me)
      await message.remove_reaction(emoji.emojize(':x:', use_aliases=True), message.guild.me)
      print("Battle canceled")
      cancelledBy = await client.fetch_user(userId)
      embed = discord.Embed(title="Combat annulé par " + cancelledBy.name + ".", color=0xff0000)
      embed.add_field(name="Pour en commencer un nouveau, tapez", value="d.battle", inline=True)
      await message.edit(embed=embed)
      global healthGuest
      global healthHost
      global turn
      global pokemonBattleData
      pokemonBattleData = []
      pokemonBattleData.append(None)
      pokemonBattleData.append(None)
      pokemonBattleData.append("end")
      pokemonBattleData.append(None)
      pokemonBattleData.append(None)
      pokemonBattleData.append(None)
      print(pokemonBattleData)
      return pokemonBattleData

async def newTurn(client, pokemonBattle, pokemonBattleData):
      message = pokemonBattle[0]
      guestPlayer = pokemonBattle[1]
      hostPlayer = pokemonBattle[2]
      guestPlayerInfos = await client.fetch_user(guestPlayer)
      hostPlayerInfos = await client.fetch_user(hostPlayer)
      player = await client.fetch_user(pokemonBattleData[3])
      guestHealth = str(pokemonBattleData[0])
      hostHealth = str(pokemonBattleData[1])
      description = "Advanced pkmn Battle - " + version + " - Copyright (c) Alexis Brandner 2018/2019 - Tous droits réservés"
      embed = discord.Embed(title="Combat pokémon",description=description, color=0x00ff00)
      embed.add_field(name="À ton tour,", value=player.name, inline=True)
      if not pokemonBattleData[4] == None:
            embed.add_field(name=guestPlayerInfos.name + " a attaqué et a infligé", value= str(pokemonBattleData[5]) + " points de dégats.", inline=True)
      embed.add_field(name=guestPlayerInfos.name + " (Guest):", value=str(guestHealth) + " HP", inline=True)
      embed.add_field(name=hostPlayerInfos.name + " (Host):", value=str(hostHealth) + " HP", inline=True)
      embed.set_footer(text=player.name + ", utilise les réactions ci-dessous pour continuer.")
      await message.edit(embed=embed)
      if  pokemonBattleData[2] == 0:
            await message.add_reaction(emoji.emojize(":dagger:", use_aliases=True))
            await message.add_reaction(emoji.emojize(":star2:", use_aliases=True))
            await message.add_reaction(emoji.emojize(":shield:", use_aliases=True))
            await message.add_reaction(emoji.emojize(":dash:", use_aliases=True))
      pokemonBattleData[2] = pokemonBattleData[2] + 1
      return pokemonBattleData

## ==========[dictionnaire des réactions]==========
async def checkReaction(client, pokemonBattle, pokemonBattleData, reactionEmoji, userId):
##    ---------{debug}---------
      print(reactionEmoji, " | ", userId)
      print(pokemonBattleData)

##    ------{startBattle}------
      if emoji.emojize(reactionEmoji) == emoji.emojize(':white_check_mark:', use_aliases=True) and userId == pokemonBattle[1]:
            pokemonBattleData = await startBattle(client, pokemonBattle, userId)
            pokemonBattleData = await newTurn(client, pokemonBattle, pokemonBattleData)
##    -----{cancelBattle}-----
      elif emoji.emojize(reactionEmoji) == emoji.emojize(':x:', use_aliases=True):
            pokemonBattleData = await cancelBattle(client, pokemonBattle, userId)
##    -----------{fight}----------
      elif emoji.emojize(reactionEmoji) == emoji.emojize(':dagger:', use_aliases=True) and userId == pokemonBattleData[3]:
            print("fight")
            pokemonBattleData = await fight(client, pokemonBattle, pokemonBattleData)
##    ---------{special}---------
      elif emoji.emojize(reactionEmoji) == emoji.emojize(':star2:', use_aliases=True) and userId == pokemonBattleData[3]:
            print("special")
##    --------{defense}--------
      elif emoji.emojize(reactionEmoji) == emoji.emojize(':shield:', use_aliases=True) and userId == pokemonBattleData[3]:
            print("defense")
##    ---------{escape}---------
      elif emoji.emojize(reactionEmoji) == emoji.emojize(':dash:', use_aliases=True) and userId == pokemonBattleData[3]:
            print("escape")
      return pokemonBattleData


## =================[attaquer]=================
async def fight(client, pokemonBattle, pokemonBattleData):
##    ------{definitions}------
      message = pokemonBattle[0]
      guestPlayer = pokemonBattle[1]
      hostPlayer = pokemonBattle[2]
      guestHealth = pokemonBattleData[0]
      hostHealth = pokemonBattleData[1]
      actualPlayer = pokemonBattleData[3]

      await message.remove_reaction(emoji.emojize(":dagger:", use_aliases=True), message.guild.get_member(actualPlayer))

      if actualPlayer == guestPlayer:
            hostHealth = hostHealth - 100
            actualPlayer = hostPlayer
      else:
            guestHealth = guestHealth - 100
            actualPlayer = guestPlayer
      print("Hôte: " + str(hostHealth) + " HP | Invité: " + str(guestHealth) + " HP")
      pokemonBattleData[4] = "attaque"
      pokemonBattleData[5] = 100
      pokemonBattleData[3] = actualPlayer
      print(actualPlayer)
      print(pokemonBattleData)
      pokemonBattleData[1] = hostHealth
      pokemonBattleData[0] = guestHealth
      if actualPlayer == guestPlayer and guestHealth < 1:
            print("Fin du combat")
            await endBattle(pokemonBattle, client, guestPlayer)
      elif actualPlayer == hostPlayer and hostHealth < 1:
            print("Fin du combat")
            await endBattle(pokemonBattle, client, hostPlayer)
      else:
            await newTurn(client, pokemonBattle, pokemonBattleData)
      return pokemonBattleData

async def endBattle(pokemonBattle, client, loser):
      loserUser = await client.fetch_user(loser)
      loserName = loserUser.name
      embed = discord.Embed(title="Combat terminé.",description=loserName+ " a perdu...", color=0xff0000)
      embed.add_field(name="Pour en commencer un nouveau, tapez", value="d.battle", inline=True)
      message = pokemonBattle[0]
      await message.edit(embed=embed)
      await message.remove_reaction(emoji.emojize(":dagger:", use_aliases=True), message.guild.me)
      await message.remove_reaction(emoji.emojize(":star2:", use_aliases=True), message.guild.me)
      await message.remove_reaction(emoji.emojize(":shield:", use_aliases=True), message.guild.me)
      await message.remove_reaction(emoji.emojize(":dash:", use_aliases=True), message.guild.me)
      return
