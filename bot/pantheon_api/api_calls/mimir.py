import config.settings as config
from twirp.context import Context
from twirp.exceptions import TwirpServerException

from pantheon_api import mimir_pb2, mimir_twirp

def get_ranking(tourney_nr):
    client = mimir_twirp.MimirClient(config.MIMIR_URL)

    try:
        response = client.GetRatingTable(
            ctx=Context(),
            server_path_prefix="/v2",
            request=mimir_pb2.EventsGetRatingTablePayload(event_id_list=[tourney_nr],order_by="rating", order="desc"),
        )
        return(response)
    except TwirpServerException as e:
            return(e)


def add_game(game_link, tourney_nr):
    client = mimir_twirp.MimirClient(config.MIMIR_URL)

    try:
        response = client.AddOnlineReplay(
            ctx=Context(),
            server_path_prefix="/v2",
            request=mimir_pb2.GamesAddOnlineReplayPayload(tourney_nr, game_link),
        )
        return(response)
    except TwirpServerException as e:
        return(e)


