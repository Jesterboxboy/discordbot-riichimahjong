from discord.ext import commands
import uuid
import json
import requests
import sys
#path relative to bot.py where the cog is loaded
import config.tournament as config

class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_load(self):
        print(f'{self.bot.user.name} has connected to Discord!')

    @commands.command(name='ranking', help='Print ranking of active tournament')
    async def ranking(self,ctx):
        request_url = str(config.MIMIR_URL)+'/v2/common.Mimir/GetRatingTable'
        json_body = json.dumps({"eventIdList": [int(config.TOURNEY)], "orderBy": "rating", "order": "desc" })
        headers = {'content-type': 'application/json'}
        print(json_body)
        response = requests.post(url=request_url, data=json_body, headers=headers)

        if response.status_code == 200:
           message_content = '```'
           for rank in response.json()['list']:
             message_content += str(rank['title'])
             message_content += '\n'
             message_content += str(rank['rating'])
             message_content += '\n'
           message_content += '```'
           emoji = '\N{THUMBS UP SIGN}'
           await ctx.message.add_reaction(emoji)
        await ctx.send(message_content)

    @commands.command(name='addgame', help='Give a link to a tenhou game to add it to the active tournament. I.e. !addgame https://tenhou.net/0/?log=2023071323gm-0029-0000-487edd97', brief='Add tenhou game to online tournament')
    async def addgame(self,ctx, game_url):
        request_url = str(config.MIMIR_URL)+'/v2/common.Mimir/AddOnlineReplay'
        json_body = json.dumps({ "eventId": int(config.TOURNEY), "link": game_url })
        headers = {'content-type': 'application/json'}
        print(json_body)
        response = requests.post(url=request_url, data=json_body, headers=headers)
        if response.status_code == 200 and "error" not in response.json()['msg']:
           emoji = '\N{THUMBS UP SIGN}'
           print(response.json())
           await ctx.message.add_reaction(emoji)
        else:
           emoji = '\N{CROSS MARK}'

           print(response.json())
           await ctx.message.add_reaction(emoji)
           await ctx.send('```'+response.json()['meta']['cause']+'```')

async def setup(bot):
    await bot.add_cog(Tournament(bot))