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
            request=mimir_pb2.GamesAddOnlineReplayPayload(event_id=tourney_nr, link=game_link),
        )
        return(response)
    except TwirpServerException as e:
        return(e)

def add_player(user_id, tourney_nr,auth_token):
    client = mimir_twirp.MimirClient(config.MIMIR_URL)


    try:
        ctx=Context()
        ctx.set_header("X-Auth-Token",auth_token.auth_token)
        ctx.set_header("X-Current-Person-Id",str(auth_token.person_id))
        response = client.RegisterPlayer(
            ctx=ctx,
            server_path_prefix="/v2",
            request=mimir_pb2.EventsRegisterPlayerPayload(event_id=tourney_nr, player_id=user_id),
        )
        return(response)
    except TwirpServerException as e:
        return(e)


