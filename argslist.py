import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import emoji

async def dictionnary(commande):
      if commande == "clap":
            embed = await clapCommand()
      elif commande == "d.help" or commande == "help":
            embed = await helpCommand()
      elif commande == "d.test" or commande == "test":
            embed = await testCommand()
      elif commande == "{arguments}":
            embed = await pasComprisCommand()
      else:
            embed = await undefinedCommand()
      sentMessage = await message.channel.send(embed=embed)
      lastHelpSession = sentMessage
      await sentMessage.add_reaction(emoji.emojize(':x:', use_aliases=True))
      return lastHelpSession

async def clapCommand():
      embed = discord.Embed(title=":information_source:  Aide DevBot", description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="clap", inline=True)
      embed.add_field(name="Utilisation:", value="clap {arguments}", inline=True)
      embed.add_field(name="Exemple:", value="clap 4", inline=True)
      embed.add_field(name="Résultat:", value=":clap: :clap: :clap: :clap:", inline=True)
      return embed

async def helpCommand():
      embed = discord.Embed(title=":information_source:  Aide DevBot", description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="d.help", inline=True)
      embed.add_field(name="Utilisation:", value="d.help {arguments}", inline=True)
      embed.add_field(name="Exemple:", value="d.help help", inline=True)
      embed.add_field(name="Résultat:", value="Affiche le message que vous êtes en train de regarder", inline=True)
      return embed


async def testCommand():
      embed = discord.Embed(title=":information_source:  Aide DevBot", description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="d.test", inline=True)
      embed.add_field(name="Utilisation:", value="Inconnue", inline=True)
      embed.add_field(name="Exemple:", value="Pas d'exemple disponible.", inline=True)
      embed.add_field(name="Résultat:", value="Ceci est une commande en cours de développement, merci de ne pas utiliser.", inline=True)
      return embed

async def pasComprisCommand():
      embed = discord.Embed(title=":warning:  ...", description=":expressionless: Tu t'attendais à voir quoi ici ?", color=0xffb900)
      embed.add_field(name="Commande:", value="d.arguments", inline=True)
      embed.add_field(name="Utilisation:", value="d.help [écris ici le nom de la commande dont tu veux la liste des arguments SANS TAPER LES CROCHETS]", inline=True)
      embed.add_field(name="Exemple:", value="d.arguments clap", inline=True)
      embed.add_field(name="Résultat:", value="Affiche les arguments disponibles pour la commande help", inline=True)
      return embed

async def undefinedCommand():
      embed = discord.Embed(title=":warning:  Attention, cette commande n'existe pas !", color=0xffb900)
      embed.add_field(name="Pour obtenir la liste des commandes, tapez", value="d.help", inline=True)
      return embed
