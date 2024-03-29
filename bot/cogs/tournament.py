from discord.ext import commands
from discord.utils import get
import uuid
import json
import requests
import sys
# path relative to bot.py where the cog is loaded
import config.settings as config
import pantheon_api.api_calls.mimir as mimir
import pantheon_api.api_calls.user as frey
from pantheon_api import mimir_pb2
from twirp.exceptions import TwirpServerException


class Tournament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auth_token = frey.login_through_pantheon(
            config.LOGIN_EMAIL, config.LOGIN_PASSWD)
        self.thumbsup = '\N{THUMBS UP SIGN}'
        self.checkmark = '\N{white heavy check mark}'
        self.crossmark = '\N{CROSS MARK}'

    @commands.Cog.listener()
    async def on_load(self):
        print(f'{self.bot.user.name} has connected to Discord!')

    @commands.command(name='ranking', help='Print ranking of active tournament')
    async def ranking(self, ctx, tourney_nr=config.TOURNEY, rating_type=config.RATING_TYPE):
        response = mimir.get_ranking(tourney_nr, rating_type)
        if type(response) == mimir_pb2.EventsGetGamesSeriesResponse:
            message_content = '```'
            message_content += '\n'
            for entry in response.results:
                message_content += entry.player.tenhou_id
                message_content += '\n'
                if rating_type == "series":
                    message_content += str(int(entry.best_series_scores))
                else:
                    message_content += str(int(entry.best_series_scores))
                message_content += '\n'
            message_content += '```'

            await ctx.message.add_reaction(self.checkmark)
            await ctx.send(message_content)

        elif (isinstance(response, TwirpServerException)):
            await ctx.message.add_reaction(self.crossmark)
            await ctx.message.reply(response.meta["cause"])

    @commands.command(name='add_game', help='Give a link to a tenhou game to add it to the active tournament. I.e. !addgame https://tenhou.net/0/?log=2023071323gm-0029-0000-487edd97', brief='Add tenhou game to online tournament')
    async def add_game(self, ctx, game_url, tourney_nr=config.TOURNEY):
        response = mimir.add_game(game_url, int(tourney_nr))
        if (isinstance(response, TwirpServerException)):
            emoji = '\N{CROSS MARK}'
            await ctx.message.add_reaction(emoji)
            await ctx.message.reply(response.meta["cause"])
        else:
            await ctx.message.add_reaction(self.checkmark)

    @commands.command(pass_context=True, name='register_player', help='Add a signed up player to a pantheon tournament. I.e.: !register_player [player_id] [tournament_id]. You can get your player id from your profile page. The tournament number defaults to the correct one, so you can omit it.', brief='Add a player to a pantheon tournament')
    # @commands.has_role('everyone')
    async def register_player(self, ctx, player_id, tourney_nr=config.TOURNEY, liga_role=config.LIGA_ROLE):
        response = mimir.add_player(
            int(player_id), int(tourney_nr), self.auth_token)
        if (isinstance(response, TwirpServerException)):
            await ctx.message.add_reaction(self.crossmark)
            await ctx.message.reply(response.meta["cause"])
        else:
            if liga_role:
                role = get(ctx.message.guild.roles, name=liga_role)
                await ctx.author.add_roles(role)
            await ctx.message.add_reaction(self.checkmark)


async def setup(bot):
    await bot.add_cog(Tournament(bot))
