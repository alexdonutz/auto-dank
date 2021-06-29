import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = ";"

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Alex AutoDanker", color=420699, description=f"**{prefix}start**\nsends pls beg, pls fish, pls hunt and pls dig every 50 seconds.\n\n**{prefix}stop**\nstops autodank.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/817431436679315467/a_02341c399244c48c41aade1788fb908a.gif?size=256&f=.gif")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def start(ctx):
	await ctx.message.delete()
	await ctx.send('Successfully enabled Auto Dank Memer!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(4)
			await ctx.send('pls beg')
			print(f"{Fore.GREEN}succefully begged")
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}succefully fished")
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}succefully hunt")
			await ctx.send('pls dep max')
			print(f"{Fore.GREEN}succefully deposited max")
			await asyncio.sleep(47)


@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Successfully disabled Auto Dank Memer!')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="Auto Dank Memer | By alex_#2726", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░░█████╗░███╗░░██╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║██║░██╔╝██╔════╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██║███████║██╔██╗██║█████═╝░█████╗░░██████╔╝
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░██║██╔══██║██║╚████║██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝██║░░██║██║░╚███║██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

selfbot is ready!
''')

bot.run(token, bot=False)

