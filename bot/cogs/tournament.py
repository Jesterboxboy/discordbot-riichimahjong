from discord.ext import commands
import uuid
import json
import requests
import sys
# path relative to bot.py where the cog is loaded
import config.settings as config
import pantheon_api.api_calls.mimir as mimir
import pantheon_api.api_calls.user as frey
from twirp.exceptions import TwirpServerException


class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auth_token = frey.login_through_pantheon(
            config.LOGIN_EMAIL, config.LOGIN_PASSWD)

    @commands.Cog.listener()
    async def on_load(self):
        print(f'{self.bot.user.name} has connected to Discord!')

    @commands.command(name='ranking', help='Print ranking of active tournament')
    async def ranking(self, ctx, tourney_nr=config.TOURNEY):
        response = mimir.get_ranking(tourney_nr)
        if response:
            message_content = '```'
            for player in response.list:
                message_content += player.title
                message_content += '\n'
                message_content += str(int(player.rating))
                message_content += '\n'
            message_content += '```'
            emoji = '\N{THUMBS UP SIGN}'
            await ctx.message.add_reaction(emoji)
        await ctx.send(message_content)

    @commands.command(name='add_game', help='Give a link to a tenhou game to add it to the active tournament. I.e. !addgame https://tenhou.net/0/?log=2023071323gm-0029-0000-487edd97', brief='Add tenhou game to online tournament')
    async def addgame(self, ctx, game_url, tourney_nr=config.TOURNEY):
        response = mimir.add_game(game_url, int(tourney_nr))
        if (isinstance(response, TwirpServerException)):
            emoji = '\N{CROSS MARK}'
            await ctx.message.add_reaction(emoji)
            await ctx.message.reply(response.meta["cause"])
        else:
            emoji = '\N{THUMBS UP SIGN}'
            await ctx.message.add_reaction(emoji)

    @commands.command(name='register_player', help='Add a signed up player to a pantheon tournament. I.e.: !register_player [player_id] [tournament_id]. You can get your player id from your profile page. The tournament number defaults to the correct one, so you can omit it.', brief='Add a player to a pantheon tournament')
    async def register_player(self, ctx, player_id, tourney_nr=config.TOURNEY):
        response = mimir.add_player(
            int(player_id), int(tourney_nr), self.auth_token)
        if (isinstance(response, TwirpServerException)):
            emoji = '\N{CROSS MARK}'
            await ctx.message.add_reaction(emoji)
            await ctx.message.reply(response.meta["cause"])
        else:
            emoji = '\N{THUMBS UP SIGN}'
            await ctx.message.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(Tournament(bot))
