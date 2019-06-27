import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import emoji

async def page1(client, message, lastHelpSession):
      title = emoji.emojize(':question:', use_aliases=True) + " Aide DevBot"
      embed = discord.Embed(title=title, description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.set_footer(text="Page 1/1")
      embed.add_field(name="Afficher l'aide:", value="d.help {arguments}", inline=True)
      embed.add_field(name="Commande clap:", value="clap {arguments}", inline=True)
      embed.add_field(name="Exécuter la commande en cours de développement:", value="d.test", inline=True)
      sentMessage = await message.channel.send(embed=embed)
      lastHelpSession = sentMessage
      #await sentMessage.add_reaction(emoji.emojize(':arrow_left:', use_aliases=True))
      #await sentMessage.add_reaction(emoji.emojize(':arrow_right:', use_aliases=True))
      await sentMessage.add_reaction(emoji.emojize(':x:', use_aliases=True))
      return lastHelpSession

async def closeLastSession(client, message, lastHelpSession, requestedBy, userId):
      if lastHelpSession.id != None:
            embed = discord.Embed(title="Session d'aide terminée.", color=0xff0000)
            embed.add_field(name="Pour en ouvrir une nouvelle, tapez", value="d.help", inline=True)
            #await lastHelpSession.remove_reaction(emoji.emojize(':arrow_left:', use_aliases=True), discord.utils.get(message.guild.members, id=client.user.id))
            #await lastHelpSession.remove_reaction(emoji.emojize(':arrow_right:', use_aliases=True), discord.utils.get(message.guild.members, id=client.user.id))
            if (requestedBy != "bot"):
                  await lastHelpSession.remove_reaction(emoji.emojize(':x:', use_aliases=True), message.guild.get_member(userId))
            await lastHelpSession.remove_reaction(emoji.emojize(':x:', use_aliases=True), message.guild.me)
            await lastHelpSession.edit(embed=embed)
            lastHelpSession.id = None
      return

async def command(commande, client, message, lastHelpSession):
      global title
      title = emoji.emojize(':question:', use_aliases=True) + " Aide DevBot"
      embed = await dictionnaire(commande.lower())
      sentMessage = await message.channel.send(embed=embed)
      lastHelpSession = sentMessage
      await sentMessage.add_reaction(emoji.emojize(':x:', use_aliases=True))
      return lastHelpSession

async def dictionnaire(commande):
      if commande == "clap":
            embed = await clapCommand()
      elif commande == "d.help" or commande == "help":
            embed = await helpCommand()
      elif commande == "d.test" or commande == "test":
            embed = await testCommand()
      elif commande == "commande":
            embed = await pasComprisCommand()
      elif commande == "arguments" or commande == "d.arguments" or commande == "d.args" or commande == "args":
            embed = await argsCommand()
      else:
            embed = await undefinedCommand()
      return embed

async def clapCommand():
      embed = discord.Embed(title=title, description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="clap", inline=True)
      embed.add_field(name="Utilisation:", value="clap {arguments}", inline=True)
      embed.add_field(name="Exemple:", value="clap 4", inline=True)
      embed.add_field(name="Résultat:", value=":clap: :clap: :clap: :clap:", inline=True)
      return embed

async def helpCommand():
      embed = discord.Embed(title=title, description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="d.help", inline=True)
      embed.add_field(name="Utilisation:", value="d.help {arguments}", inline=True)
      embed.add_field(name="Exemple:", value="d.help help", inline=True)
      embed.add_field(name="Résultat:", value="Affiche le message que vous êtes en train de regarder", inline=True)
      return embed


async def testCommand():
      embed = discord.Embed(title=title, description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="d.test", inline=True)
      embed.add_field(name="Utilisation:", value="Inconnue", inline=True)
      embed.add_field(name="Exemple:", value="Pas d'exemple disponible.", inline=True)
      embed.add_field(name="Résultat:", value="Ceci est une commande en cours de développement, merci de ne pas utiliser.", inline=True)
      return embed

async def pasComprisCommand():
      embed = discord.Embed(title=":warning:  ...", description=":expressionless: Tu t'attendais à voir quoi ici ?", color=0xffb900)
      embed.add_field(name="Commande:", value="d.help", inline=True)
      embed.add_field(name="Utilisation:", value="d.help [écris ici le nom de la commande sur laquelle tu veux avoir de l'aide SANS TAPER LES CROCHETS]", inline=True)
      embed.add_field(name="Exemple:", value="d.help help", inline=True)
      embed.add_field(name="Résultat:", value="Affiche l'aide sur la commande help", inline=True)
      return embed

async def undefinedCommand():
      embed = discord.Embed(title=":warning:  Attention, cette commande n'existe pas !", color=0xffb900)
      embed.add_field(name="Pour obtenir la liste des commandes, tapez", value="d.help", inline=True)
      return embed

async def argsCommand():
      embed = discord.Embed(title=title, description="Utilisez \"d.help commande\" pour afficher l'aide d'une commande", color=0x00c8ff)
      embed.add_field(name="Commande:", value="d.arguments", inline=True)
      embed.add_field(name="Utilisation:", value="d.arguments {arguments}", inline=True)
      embed.add_field(name="Exemple:", value="d.arguments clap", inline=True)
      embed.add_field(name="Résultat:", value="Indique quels sont les arguments disponibles pour la commande clap.", inline=True)
      return embed
