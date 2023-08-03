# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mimir.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pantheon_api.atoms_pb2 as atoms__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmimir.proto\x12\x06\x63ommon\x1a\x0b\x61toms.proto\"\x1a\n\x18\x45ventsGetRulesetsPayload\"q\n\x19\x45ventsGetRulesetsResponse\x12\'\n\x08rulesets\x18\x01 \x03(\x0b\x32\x15.common.RulesetConfig\x12\x13\n\x0bruleset_ids\x18\x02 \x03(\t\x12\x16\n\x0eruleset_titles\x18\x03 \x03(\t\")\n\x19\x45ventsGetTimezonesPayload\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\"H\n\x1a\x45ventsGetTimezonesResponse\x12\x17\n\x0fpreferred_by_ip\x18\x01 \x01(\t\x12\x11\n\ttimezones\x18\x02 \x03(\t\")\n\x19\x45ventsGetCountriesPayload\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\"Y\n\x1a\x45ventsGetCountriesResponse\x12\x17\n\x0fpreferred_by_ip\x18\x01 \x01(\t\x12\"\n\tcountries\x18\x02 \x03(\x0b\x32\x0f.common.Country\"P\n\x16\x45ventsGetEventsPayload\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x17\n\x0f\x66ilter_unlisted\x18\x03 \x01(\x08\"G\n\x17\x45ventsGetEventsResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x1d\n\x06\x65vents\x18\x02 \x03(\x0b\x32\r.common.Event\")\n\x1a\x45ventsGetEventsByIdPayload\x12\x0b\n\x03ids\x18\x01 \x03(\x05\"<\n\x1b\x45ventsGetEventsByIdResponse\x12\x1d\n\x06\x65vents\x18\x01 \x03(\x0b\x32\r.common.Event\"\x1b\n\x19PlayersGetMyEventsPayload\"=\n\x1aPlayersGetMyEventsResponse\x12\x1f\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x0f.common.MyEvent\"\xbd\x01\n\x1b\x45ventsGetRatingTablePayload\x12\x15\n\revent_id_list\x18\x01 \x03(\x05\x12\x10\n\x08order_by\x18\x02 \x01(\t\x12\r\n\x05order\x18\x03 \x01(\t\x12!\n\x10with_prefinished\x18\x04 \x01(\x08\x42\x02\x18\x01H\x00\x88\x01\x01\x12\x1b\n\x0eonly_min_games\x18\x05 \x01(\x08H\x01\x88\x01\x01\x42\x13\n\x11_with_prefinishedB\x11\n\x0f_only_min_games\"D\n\x1c\x45ventsGetRatingTableResponse\x12$\n\x04list\x18\x01 \x03(\x0b\x32\x16.common.PlayerInRating\"\x93\x01\n\x19\x45ventsGetLastGamesPayload\x12\x15\n\revent_id_list\x18\x01 \x03(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x15\n\x08order_by\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05order\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\x0b\n\t_order_byB\x08\n\x06_order\"u\n\x1a\x45ventsGetLastGamesResponse\x12!\n\x05games\x18\x01 \x03(\x0b\x32\x12.common.GameResult\x12\x1f\n\x07players\x18\x02 \x03(\x0b\x32\x0e.common.Player\x12\x13\n\x0btotal_games\x18\x03 \x01(\x05\",\n\x14\x45ventsGetGamePayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"Z\n\x15\x45ventsGetGameResponse\x12 \n\x04game\x18\x01 \x01(\x0b\x32\x12.common.GameResult\x12\x1f\n\x07players\x18\x02 \x03(\x0b\x32\x0e.common.Player\"E\n\x1c\x45ventsGetGamesSeriesResponse\x12%\n\x07results\x18\x01 \x03(\x0b\x32\x14.common.SeriesResult\"G\n PlayersGetCurrentSessionsPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\"M\n!PlayersGetCurrentSessionsResponse\x12(\n\x08sessions\x18\x01 \x03(\x0b\x32\x16.common.CurrentSession\"9\n$EventsGetAllRegisteredPlayersPayload\x12\x11\n\tevent_ids\x18\x01 \x03(\x05\"R\n%EventsGetAllRegisteredPlayersResponse\x12)\n\x07players\x18\x01 \x03(\x0b\x32\x18.common.RegisteredPlayer\"\xc0\x01\n\x1b\x45ventsGetTimerStateResponse\x12\x0f\n\x07started\x18\x01 \x01(\x08\x12\x10\n\x08\x66inished\x18\x02 \x01(\x08\x12\x16\n\x0etime_remaining\x18\x03 \x01(\x05\x12\x19\n\x11waiting_for_timer\x18\x04 \x01(\x08\x12\x16\n\x0ehave_autostart\x18\x05 \x01(\x08\x12\x17\n\x0f\x61utostart_timer\x18\x06 \x01(\x08\x12\x1a\n\x12hide_seating_after\x18\x08 \x01(\x05\"6\n\x1eGamesGetSessionOverviewPayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"\xb8\x01\n\x1fGamesGetSessionOverviewResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x18\n\x0btable_index\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12(\n\x07players\x18\x04 \x03(\x0b\x32\x17.common.PlayerInSession\x12#\n\x05state\x18\x05 \x01(\x0b\x32\x14.common.SessionStateB\x0e\n\x0c_table_index\"H\n\x1cPlayersGetPlayerStatsPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x15\n\revent_id_list\x18\x02 \x03(\x05\"\xfa\x03\n\x1dPlayersGetPlayerStatsResponse\x12\x16\n\x0erating_history\x18\x01 \x03(\x05\x12\x38\n\rscore_history\x18\x02 \x03(\x0b\x32!.common.SessionHistoryResultTable\x12$\n\x0cplayers_info\x18\x03 \x03(\x0b\x32\x0e.common.Player\x12\x31\n\x0eplaces_summary\x18\x04 \x03(\x0b\x32\x19.common.PlacesSummaryItem\x12\x1a\n\x12total_played_games\x18\x05 \x01(\x05\x12\x1b\n\x13total_played_rounds\x18\x06 \x01(\x05\x12-\n\x0bwin_summary\x18\x07 \x01(\x0b\x32\x18.common.PlayerWinSummary\x12\x32\n\x13hands_value_summary\x18\x08 \x03(\x0b\x32\x15.common.HandValueStat\x12&\n\x0cyaku_summary\x18\t \x03(\x0b\x32\x10.common.YakuStat\x12-\n\x0eriichi_summary\x18\n \x01(\x0b\x32\x15.common.RiichiSummary\x12&\n\tdora_stat\x18\x0b \x01(\x0b\x32\x13.common.DoraSummary\x12\x13\n\x0blast_update\x18\x0c \x01(\t\"O\n\x14GamesAddRoundPayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\x12!\n\nround_data\x18\x02 \x01(\x0b\x32\r.common.Round\"\xd8\x02\n\x15GamesAddRoundResponse\x12\x33\n\x06scores\x18\x01 \x03(\x0b\x32#.common.IntermediateResultOfSession\x12+\n\x12\x65xtra_penalty_logs\x18\x02 \x03(\x0b\x32\x0f.common.Penalty\x12\r\n\x05round\x18\x03 \x01(\x05\x12\r\n\x05honba\x18\x04 \x01(\x05\x12\x13\n\x0briichi_bets\x18\x05 \x01(\x05\x12\x1c\n\x14prematurely_finished\x18\x06 \x01(\x08\x12\x1a\n\x12round_just_changed\x18\x07 \x01(\x08\x12\x13\n\x0bis_finished\x18\x08 \x01(\x08\x12\x19\n\x11last_hand_started\x18\t \x01(\x08\x12/\n\x0clast_outcome\x18\n \x01(\x0e\x32\x14.common.RoundOutcomeH\x00\x88\x01\x01\x42\x0f\n\r_last_outcome\"S\n\x18GamesPreviewRoundPayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\x12!\n\nround_data\x18\x02 \x01(\x0b\x32\r.common.Round\">\n\x19GamesPreviewRoundResponse\x12!\n\x05state\x18\x01 \x01(\x0b\x32\x12.common.RoundState\"=\n\x1bGamesAddOnlineReplayPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x0c\n\x04link\x18\x02 \x01(\t\"a\n\x1cGamesAddOnlineReplayResponse\x12 \n\x04game\x18\x01 \x01(\x0b\x32\x12.common.GameResult\x12\x1f\n\x07players\x18\x02 \x03(\x0b\x32\x0e.common.Player\"C\n\x1cPlayersGetLastResultsPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\"N\n\x1dPlayersGetLastResultsResponse\x12-\n\x07results\x18\x01 \x03(\x0b\x32\x1c.common.SessionHistoryResult\"A\n\x1aPlayersGetLastRoundPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\"@\n\x1bPlayersGetLastRoundResponse\x12!\n\x05round\x18\x01 \x01(\x0b\x32\x12.common.RoundState\"2\n\x1aPlayersGetAllRoundsPayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"A\n\x1bPlayersGetAllRoundsResponse\x12\"\n\x06rounds\x18\x01 \x03(\x0b\x32\x12.common.RoundState\"8\n PlayersGetLastRoundByHashPayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"F\n!PlayersGetLastRoundByHashResponse\x12!\n\x05round\x18\x01 \x01(\x0b\x32\x12.common.RoundState\"*\n\x1c\x45ventsGetEventForEditPayload\x12\n\n\x02id\x18\x01 \x01(\x05\"M\n\x1d\x45ventsGetEventForEditResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12 \n\x05\x65vent\x18\x02 \x01(\x0b\x32\x11.common.EventData\"H\n\x18\x45ventsUpdateEventPayload\x12\n\n\x02id\x18\x01 \x01(\x05\x12 \n\x05\x65vent\x18\x02 \x01(\x0b\x32\x11.common.EventData\"B\n\x1c\x45ventsGetTablesStateResponse\x12\"\n\x06tables\x18\x01 \x03(\x0b\x32\x12.common.TableState\"B\n\x1b\x45ventsRegisterPlayerPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\"D\n\x1d\x45ventsUnregisterPlayerPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\"c\n$EventsUpdatePlayerSeatingFlagPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x16\n\x0eignore_seating\x18\x03 \x01(\x08\"K\n\x1c\x45ventsGetAchievementsPayload\x12\x19\n\x11\x61\x63hievements_list\x18\x02 \x03(\t\x12\x10\n\x08\x65vent_id\x18\x03 \x01(\x05\"J\n\x1d\x45ventsGetAchievementsResponse\x12)\n\x0c\x61\x63hievements\x18\x01 \x03(\x0b\x32\x13.common.Achievement\"h\n\"EventsUpdatePlayersLocalIdsPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x30\n\x10ids_to_local_ids\x18\x02 \x03(\x0b\x32\x16.common.LocalIdMapping\"c\n$EventsUpdatePlayerReplacementPayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x16\n\x0ereplacement_id\x18\x03 \x01(\x05\"c\n\x1f\x45ventsUpdatePlayersTeamsPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12.\n\x11ids_to_team_names\x18\x02 \x03(\x0b\x32\x13.common.TeamMapping\":\n\x15GamesStartGamePayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x0f\n\x07players\x18\x02 \x03(\x05\".\n\x16GamesStartGameResponse\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"+\n\x13GamesEndGamePayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\".\n\x16GamesCancelGamePayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"t\n\x19GamesDropLastRoundPayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\x12\x41\n\x14intermediate_results\x18\x02 \x03(\x0b\x32#.common.IntermediateResultOfSession\"2\n\x1aGamesDefinalizeGamePayload\x12\x14\n\x0csession_hash\x18\x01 \x01(\t\"]\n\x16GamesAddPenaltyPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x11\n\tplayer_id\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\x12\x0e\n\x06reason\x18\x04 \x01(\t\"?\n\x1aGamesAddPenaltyGamePayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x0f\n\x07players\x18\x02 \x03(\x05\"+\n\x1bGamesAddPenaltyGameResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t\"%\n\x17PlayersGetPlayerPayload\x12\n\n\x02id\x18\x01 \x01(\x05\";\n\x18PlayersGetPlayerResponse\x12\x1f\n\x07players\x18\x01 \x01(\x0b\x32\x0e.common.Player\"I\n\x1f\x45ventsGetCurrentSeatingResponse\x12&\n\x07seating\x18\x01 \x03(\x0b\x32\x15.common.PlayerSeating\"Y\n!SeatingMakeShuffledSeatingPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x14\n\x0cgroups_count\x18\x02 \x01(\x05\x12\x0c\n\x04seed\x18\x03 \x01(\x05\"M\n#SeatingGenerateSwissSeatingResponse\x12&\n\x06tables\x18\x01 \x03(\x0b\x32\x16.common.TableItemSwiss\"C\n!SeatingMakeIntervalSeatingPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x0c\n\x04step\x18\x02 \x01(\x05\"U\n$SeatingMakePrescriptedSeatingPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x1b\n\x13randomize_at_tables\x18\x02 \x01(\x08\"T\n(SeatingGetNextPrescriptedSeatingResponse\x12(\n\x06tables\x18\x01 \x03(\x0b\x32\x18.common.PrescriptedTable\"\x8d\x01\n\'EventsGetPrescriptedEventConfigResponse\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x1a\n\x12next_session_index\x18\x02 \x01(\x05\x12\x16\n\tprescript\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06\x65rrors\x18\x04 \x03(\tB\x0c\n\n_prescript\"l\n)EventsUpdatePrescriptedEventConfigPayload\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x1a\n\x12next_session_index\x18\x02 \x01(\x05\x12\x11\n\tprescript\x18\x03 \x01(\t\"/\n\x1e\x45ventsGetStartingTimerResponse\x12\r\n\x05timer\x18\x01 \x01(\x05\"*\n\x15\x43learStatCachePayload\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x32\xa2*\n\x05Mimir\x12R\n\x0bGetRulesets\x12 .common.EventsGetRulesetsPayload\x1a!.common.EventsGetRulesetsResponse\x12U\n\x0cGetTimezones\x12!.common.EventsGetTimezonesPayload\x1a\".common.EventsGetTimezonesResponse\x12U\n\x0cGetCountries\x12!.common.EventsGetCountriesPayload\x1a\".common.EventsGetCountriesResponse\x12L\n\tGetEvents\x12\x1e.common.EventsGetEventsPayload\x1a\x1f.common.EventsGetEventsResponse\x12X\n\rGetEventsById\x12\".common.EventsGetEventsByIdPayload\x1a#.common.EventsGetEventsByIdResponse\x12T\n\x0bGetMyEvents\x12!.common.PlayersGetMyEventsPayload\x1a\".common.PlayersGetMyEventsResponse\x12@\n\rGetGameConfig\x12\x1b.common.GenericEventPayload\x1a\x12.common.GameConfig\x12[\n\x0eGetRatingTable\x12#.common.EventsGetRatingTablePayload\x1a$.common.EventsGetRatingTableResponse\x12U\n\x0cGetLastGames\x12!.common.EventsGetLastGamesPayload\x1a\".common.EventsGetLastGamesResponse\x12\x46\n\x07GetGame\x12\x1c.common.EventsGetGamePayload\x1a\x1d.common.EventsGetGameResponse\x12S\n\x0eGetGamesSeries\x12\x1b.common.GenericEventPayload\x1a$.common.EventsGetGamesSeriesResponse\x12i\n\x12GetCurrentSessions\x12(.common.PlayersGetCurrentSessionsPayload\x1a).common.PlayersGetCurrentSessionsResponse\x12v\n\x17GetAllRegisteredPlayers\x12,.common.EventsGetAllRegisteredPlayersPayload\x1a-.common.EventsGetAllRegisteredPlayersResponse\x12Q\n\rGetTimerState\x12\x1b.common.GenericEventPayload\x1a#.common.EventsGetTimerStateResponse\x12\x65\n\x12GetSessionOverview\x12&.common.GamesGetSessionOverviewPayload\x1a\'.common.GamesGetSessionOverviewResponse\x12]\n\x0eGetPlayerStats\x12$.common.PlayersGetPlayerStatsPayload\x1a%.common.PlayersGetPlayerStatsResponse\x12G\n\x08\x41\x64\x64Round\x12\x1c.common.GamesAddRoundPayload\x1a\x1d.common.GamesAddRoundResponse\x12S\n\x0cPreviewRound\x12 .common.GamesPreviewRoundPayload\x1a!.common.GamesPreviewRoundResponse\x12\\\n\x0f\x41\x64\x64OnlineReplay\x12#.common.GamesAddOnlineReplayPayload\x1a$.common.GamesAddOnlineReplayResponse\x12]\n\x0eGetLastResults\x12$.common.PlayersGetLastResultsPayload\x1a%.common.PlayersGetLastResultsResponse\x12W\n\x0cGetLastRound\x12\".common.PlayersGetLastRoundPayload\x1a#.common.PlayersGetLastRoundResponse\x12W\n\x0cGetAllRounds\x12\".common.PlayersGetAllRoundsPayload\x1a#.common.PlayersGetAllRoundsResponse\x12i\n\x12GetLastRoundByHash\x12(.common.PlayersGetLastRoundByHashPayload\x1a).common.PlayersGetLastRoundByHashResponse\x12^\n\x0fGetEventForEdit\x12$.common.EventsGetEventForEditPayload\x1a%.common.EventsGetEventForEditResponse\x12M\n\x0eRebuildScoring\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12=\n\x0b\x43reateEvent\x12\x11.common.EventData\x1a\x1b.common.GenericEventPayload\x12O\n\x0bUpdateEvent\x12 .common.EventsUpdateEventPayload\x1a\x1e.common.GenericSuccessResponse\x12J\n\x0b\x46inishEvent\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12K\n\x0cToggleListed\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12S\n\x0eGetTablesState\x12\x1b.common.GenericEventPayload\x1a$.common.EventsGetTablesStateResponse\x12I\n\nStartTimer\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12U\n\x0eRegisterPlayer\x12#.common.EventsRegisterPlayerPayload\x1a\x1e.common.GenericSuccessResponse\x12Y\n\x10UnregisterPlayer\x12%.common.EventsUnregisterPlayerPayload\x1a\x1e.common.GenericSuccessResponse\x12g\n\x17UpdatePlayerSeatingFlag\x12,.common.EventsUpdatePlayerSeatingFlagPayload\x1a\x1e.common.GenericSuccessResponse\x12^\n\x0fGetAchievements\x12$.common.EventsGetAchievementsPayload\x1a%.common.EventsGetAchievementsResponse\x12P\n\x11ToggleHideResults\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12\x63\n\x15UpdatePlayersLocalIds\x12*.common.EventsUpdatePlayersLocalIdsPayload\x1a\x1e.common.GenericSuccessResponse\x12g\n\x17UpdatePlayerReplacement\x12,.common.EventsUpdatePlayerReplacementPayload\x1a\x1e.common.GenericSuccessResponse\x12]\n\x12UpdatePlayersTeams\x12\'.common.EventsUpdatePlayersTeamsPayload\x1a\x1e.common.GenericSuccessResponse\x12J\n\tStartGame\x12\x1d.common.GamesStartGamePayload\x1a\x1e.common.GamesStartGameResponse\x12\x46\n\x07\x45ndGame\x12\x1b.common.GamesEndGamePayload\x1a\x1e.common.GenericSuccessResponse\x12L\n\nCancelGame\x12\x1e.common.GamesCancelGamePayload\x1a\x1e.common.GenericSuccessResponse\x12N\n\x0f\x46inalizeSession\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12R\n\rDropLastRound\x12!.common.GamesDropLastRoundPayload\x1a\x1e.common.GenericSuccessResponse\x12T\n\x0e\x44\x65\x66inalizeGame\x12\".common.GamesDefinalizeGamePayload\x1a\x1e.common.GenericSuccessResponse\x12L\n\nAddPenalty\x12\x1e.common.GamesAddPenaltyPayload\x1a\x1e.common.GenericSuccessResponse\x12Y\n\x0e\x41\x64\x64PenaltyGame\x12\".common.GamesAddPenaltyGamePayload\x1a#.common.GamesAddPenaltyGameResponse\x12N\n\tGetPlayer\x12\x1f.common.PlayersGetPlayerPayload\x1a .common.PlayersGetPlayerResponse\x12Y\n\x11GetCurrentSeating\x12\x1b.common.GenericEventPayload\x1a\'.common.EventsGetCurrentSeatingResponse\x12`\n\x13MakeShuffledSeating\x12).common.SeatingMakeShuffledSeatingPayload\x1a\x1e.common.GenericSuccessResponse\x12O\n\x10MakeSwissSeating\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12K\n\x0cResetSeating\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12`\n\x14GenerateSwissSeating\x12\x1b.common.GenericEventPayload\x1a+.common.SeatingGenerateSwissSeatingResponse\x12`\n\x13MakeIntervalSeating\x12).common.SeatingMakeIntervalSeatingPayload\x1a\x1e.common.GenericSuccessResponse\x12\x66\n\x16MakePrescriptedSeating\x12,.common.SeatingMakePrescriptedSeatingPayload\x1a\x1e.common.GenericSuccessResponse\x12j\n\x19GetNextPrescriptedSeating\x12\x1b.common.GenericEventPayload\x1a\x30.common.SeatingGetNextPrescriptedSeatingResponse\x12i\n\x19GetPrescriptedEventConfig\x12\x1b.common.GenericEventPayload\x1a/.common.EventsGetPrescriptedEventConfigResponse\x12q\n\x1cUpdatePrescriptedEventConfig\x12\x31.common.EventsUpdatePrescriptedEventConfigPayload\x1a\x1e.common.GenericSuccessResponse\x12P\n\x11InitStartingTimer\x12\x1b.common.GenericEventPayload\x1a\x1e.common.GenericSuccessResponse\x12W\n\x10GetStartingTimer\x12\x1b.common.GenericEventPayload\x1a&.common.EventsGetStartingTimerResponse\x12O\n\x0e\x43learStatCache\x12\x1d.common.ClearStatCachePayload\x1a\x1e.common.GenericSuccessResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mimir_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _EVENTSGETRATINGTABLEPAYLOAD.fields_by_name['with_prefinished']._options = None
  _EVENTSGETRATINGTABLEPAYLOAD.fields_by_name['with_prefinished']._serialized_options = b'\030\001'
  _globals['_EVENTSGETRULESETSPAYLOAD']._serialized_start=36
  _globals['_EVENTSGETRULESETSPAYLOAD']._serialized_end=62
  _globals['_EVENTSGETRULESETSRESPONSE']._serialized_start=64
  _globals['_EVENTSGETRULESETSRESPONSE']._serialized_end=177
  _globals['_EVENTSGETTIMEZONESPAYLOAD']._serialized_start=179
  _globals['_EVENTSGETTIMEZONESPAYLOAD']._serialized_end=220
  _globals['_EVENTSGETTIMEZONESRESPONSE']._serialized_start=222
  _globals['_EVENTSGETTIMEZONESRESPONSE']._serialized_end=294
  _globals['_EVENTSGETCOUNTRIESPAYLOAD']._serialized_start=296
  _globals['_EVENTSGETCOUNTRIESPAYLOAD']._serialized_end=337
  _globals['_EVENTSGETCOUNTRIESRESPONSE']._serialized_start=339
  _globals['_EVENTSGETCOUNTRIESRESPONSE']._serialized_end=428
  _globals['_EVENTSGETEVENTSPAYLOAD']._serialized_start=430
  _globals['_EVENTSGETEVENTSPAYLOAD']._serialized_end=510
  _globals['_EVENTSGETEVENTSRESPONSE']._serialized_start=512
  _globals['_EVENTSGETEVENTSRESPONSE']._serialized_end=583
  _globals['_EVENTSGETEVENTSBYIDPAYLOAD']._serialized_start=585
  _globals['_EVENTSGETEVENTSBYIDPAYLOAD']._serialized_end=626
  _globals['_EVENTSGETEVENTSBYIDRESPONSE']._serialized_start=628
  _globals['_EVENTSGETEVENTSBYIDRESPONSE']._serialized_end=688
  _globals['_PLAYERSGETMYEVENTSPAYLOAD']._serialized_start=690
  _globals['_PLAYERSGETMYEVENTSPAYLOAD']._serialized_end=717
  _globals['_PLAYERSGETMYEVENTSRESPONSE']._serialized_start=719
  _globals['_PLAYERSGETMYEVENTSRESPONSE']._serialized_end=780
  _globals['_EVENTSGETRATINGTABLEPAYLOAD']._serialized_start=783
  _globals['_EVENTSGETRATINGTABLEPAYLOAD']._serialized_end=972
  _globals['_EVENTSGETRATINGTABLERESPONSE']._serialized_start=974
  _globals['_EVENTSGETRATINGTABLERESPONSE']._serialized_end=1042
  _globals['_EVENTSGETLASTGAMESPAYLOAD']._serialized_start=1045
  _globals['_EVENTSGETLASTGAMESPAYLOAD']._serialized_end=1192
  _globals['_EVENTSGETLASTGAMESRESPONSE']._serialized_start=1194
  _globals['_EVENTSGETLASTGAMESRESPONSE']._serialized_end=1311
  _globals['_EVENTSGETGAMEPAYLOAD']._serialized_start=1313
  _globals['_EVENTSGETGAMEPAYLOAD']._serialized_end=1357
  _globals['_EVENTSGETGAMERESPONSE']._serialized_start=1359
  _globals['_EVENTSGETGAMERESPONSE']._serialized_end=1449
  _globals['_EVENTSGETGAMESSERIESRESPONSE']._serialized_start=1451
  _globals['_EVENTSGETGAMESSERIESRESPONSE']._serialized_end=1520
  _globals['_PLAYERSGETCURRENTSESSIONSPAYLOAD']._serialized_start=1522
  _globals['_PLAYERSGETCURRENTSESSIONSPAYLOAD']._serialized_end=1593
  _globals['_PLAYERSGETCURRENTSESSIONSRESPONSE']._serialized_start=1595
  _globals['_PLAYERSGETCURRENTSESSIONSRESPONSE']._serialized_end=1672
  _globals['_EVENTSGETALLREGISTEREDPLAYERSPAYLOAD']._serialized_start=1674
  _globals['_EVENTSGETALLREGISTEREDPLAYERSPAYLOAD']._serialized_end=1731
  _globals['_EVENTSGETALLREGISTEREDPLAYERSRESPONSE']._serialized_start=1733
  _globals['_EVENTSGETALLREGISTEREDPLAYERSRESPONSE']._serialized_end=1815
  _globals['_EVENTSGETTIMERSTATERESPONSE']._serialized_start=1818
  _globals['_EVENTSGETTIMERSTATERESPONSE']._serialized_end=2010
  _globals['_GAMESGETSESSIONOVERVIEWPAYLOAD']._serialized_start=2012
  _globals['_GAMESGETSESSIONOVERVIEWPAYLOAD']._serialized_end=2066
  _globals['_GAMESGETSESSIONOVERVIEWRESPONSE']._serialized_start=2069
  _globals['_GAMESGETSESSIONOVERVIEWRESPONSE']._serialized_end=2253
  _globals['_PLAYERSGETPLAYERSTATSPAYLOAD']._serialized_start=2255
  _globals['_PLAYERSGETPLAYERSTATSPAYLOAD']._serialized_end=2327
  _globals['_PLAYERSGETPLAYERSTATSRESPONSE']._serialized_start=2330
  _globals['_PLAYERSGETPLAYERSTATSRESPONSE']._serialized_end=2836
  _globals['_GAMESADDROUNDPAYLOAD']._serialized_start=2838
  _globals['_GAMESADDROUNDPAYLOAD']._serialized_end=2917
  _globals['_GAMESADDROUNDRESPONSE']._serialized_start=2920
  _globals['_GAMESADDROUNDRESPONSE']._serialized_end=3264
  _globals['_GAMESPREVIEWROUNDPAYLOAD']._serialized_start=3266
  _globals['_GAMESPREVIEWROUNDPAYLOAD']._serialized_end=3349
  _globals['_GAMESPREVIEWROUNDRESPONSE']._serialized_start=3351
  _globals['_GAMESPREVIEWROUNDRESPONSE']._serialized_end=3413
  _globals['_GAMESADDONLINEREPLAYPAYLOAD']._serialized_start=3415
  _globals['_GAMESADDONLINEREPLAYPAYLOAD']._serialized_end=3476
  _globals['_GAMESADDONLINEREPLAYRESPONSE']._serialized_start=3478
  _globals['_GAMESADDONLINEREPLAYRESPONSE']._serialized_end=3575
  _globals['_PLAYERSGETLASTRESULTSPAYLOAD']._serialized_start=3577
  _globals['_PLAYERSGETLASTRESULTSPAYLOAD']._serialized_end=3644
  _globals['_PLAYERSGETLASTRESULTSRESPONSE']._serialized_start=3646
  _globals['_PLAYERSGETLASTRESULTSRESPONSE']._serialized_end=3724
  _globals['_PLAYERSGETLASTROUNDPAYLOAD']._serialized_start=3726
  _globals['_PLAYERSGETLASTROUNDPAYLOAD']._serialized_end=3791
  _globals['_PLAYERSGETLASTROUNDRESPONSE']._serialized_start=3793
  _globals['_PLAYERSGETLASTROUNDRESPONSE']._serialized_end=3857
  _globals['_PLAYERSGETALLROUNDSPAYLOAD']._serialized_start=3859
  _globals['_PLAYERSGETALLROUNDSPAYLOAD']._serialized_end=3909
  _globals['_PLAYERSGETALLROUNDSRESPONSE']._serialized_start=3911
  _globals['_PLAYERSGETALLROUNDSRESPONSE']._serialized_end=3976
  _globals['_PLAYERSGETLASTROUNDBYHASHPAYLOAD']._serialized_start=3978
  _globals['_PLAYERSGETLASTROUNDBYHASHPAYLOAD']._serialized_end=4034
  _globals['_PLAYERSGETLASTROUNDBYHASHRESPONSE']._serialized_start=4036
  _globals['_PLAYERSGETLASTROUNDBYHASHRESPONSE']._serialized_end=4106
  _globals['_EVENTSGETEVENTFOREDITPAYLOAD']._serialized_start=4108
  _globals['_EVENTSGETEVENTFOREDITPAYLOAD']._serialized_end=4150
  _globals['_EVENTSGETEVENTFOREDITRESPONSE']._serialized_start=4152
  _globals['_EVENTSGETEVENTFOREDITRESPONSE']._serialized_end=4229
  _globals['_EVENTSUPDATEEVENTPAYLOAD']._serialized_start=4231
  _globals['_EVENTSUPDATEEVENTPAYLOAD']._serialized_end=4303
  _globals['_EVENTSGETTABLESSTATERESPONSE']._serialized_start=4305
  _globals['_EVENTSGETTABLESSTATERESPONSE']._serialized_end=4371
  _globals['_EVENTSREGISTERPLAYERPAYLOAD']._serialized_start=4373
  _globals['_EVENTSREGISTERPLAYERPAYLOAD']._serialized_end=4439
  _globals['_EVENTSUNREGISTERPLAYERPAYLOAD']._serialized_start=4441
  _globals['_EVENTSUNREGISTERPLAYERPAYLOAD']._serialized_end=4509
  _globals['_EVENTSUPDATEPLAYERSEATINGFLAGPAYLOAD']._serialized_start=4511
  _globals['_EVENTSUPDATEPLAYERSEATINGFLAGPAYLOAD']._serialized_end=4610
  _globals['_EVENTSGETACHIEVEMENTSPAYLOAD']._serialized_start=4612
  _globals['_EVENTSGETACHIEVEMENTSPAYLOAD']._serialized_end=4687
  _globals['_EVENTSGETACHIEVEMENTSRESPONSE']._serialized_start=4689
  _globals['_EVENTSGETACHIEVEMENTSRESPONSE']._serialized_end=4763
  _globals['_EVENTSUPDATEPLAYERSLOCALIDSPAYLOAD']._serialized_start=4765
  _globals['_EVENTSUPDATEPLAYERSLOCALIDSPAYLOAD']._serialized_end=4869
  _globals['_EVENTSUPDATEPLAYERREPLACEMENTPAYLOAD']._serialized_start=4871
  _globals['_EVENTSUPDATEPLAYERREPLACEMENTPAYLOAD']._serialized_end=4970
  _globals['_EVENTSUPDATEPLAYERSTEAMSPAYLOAD']._serialized_start=4972
  _globals['_EVENTSUPDATEPLAYERSTEAMSPAYLOAD']._serialized_end=5071
  _globals['_GAMESSTARTGAMEPAYLOAD']._serialized_start=5073
  _globals['_GAMESSTARTGAMEPAYLOAD']._serialized_end=5131
  _globals['_GAMESSTARTGAMERESPONSE']._serialized_start=5133
  _globals['_GAMESSTARTGAMERESPONSE']._serialized_end=5179
  _globals['_GAMESENDGAMEPAYLOAD']._serialized_start=5181
  _globals['_GAMESENDGAMEPAYLOAD']._serialized_end=5224
  _globals['_GAMESCANCELGAMEPAYLOAD']._serialized_start=5226
  _globals['_GAMESCANCELGAMEPAYLOAD']._serialized_end=5272
  _globals['_GAMESDROPLASTROUNDPAYLOAD']._serialized_start=5274
  _globals['_GAMESDROPLASTROUNDPAYLOAD']._serialized_end=5390
  _globals['_GAMESDEFINALIZEGAMEPAYLOAD']._serialized_start=5392
  _globals['_GAMESDEFINALIZEGAMEPAYLOAD']._serialized_end=5442
  _globals['_GAMESADDPENALTYPAYLOAD']._serialized_start=5444
  _globals['_GAMESADDPENALTYPAYLOAD']._serialized_end=5537
  _globals['_GAMESADDPENALTYGAMEPAYLOAD']._serialized_start=5539
  _globals['_GAMESADDPENALTYGAMEPAYLOAD']._serialized_end=5602
  _globals['_GAMESADDPENALTYGAMERESPONSE']._serialized_start=5604
  _globals['_GAMESADDPENALTYGAMERESPONSE']._serialized_end=5647
  _globals['_PLAYERSGETPLAYERPAYLOAD']._serialized_start=5649
  _globals['_PLAYERSGETPLAYERPAYLOAD']._serialized_end=5686
  _globals['_PLAYERSGETPLAYERRESPONSE']._serialized_start=5688
  _globals['_PLAYERSGETPLAYERRESPONSE']._serialized_end=5747
  _globals['_EVENTSGETCURRENTSEATINGRESPONSE']._serialized_start=5749
  _globals['_EVENTSGETCURRENTSEATINGRESPONSE']._serialized_end=5822
  _globals['_SEATINGMAKESHUFFLEDSEATINGPAYLOAD']._serialized_start=5824
  _globals['_SEATINGMAKESHUFFLEDSEATINGPAYLOAD']._serialized_end=5913
  _globals['_SEATINGGENERATESWISSSEATINGRESPONSE']._serialized_start=5915
  _globals['_SEATINGGENERATESWISSSEATINGRESPONSE']._serialized_end=5992
  _globals['_SEATINGMAKEINTERVALSEATINGPAYLOAD']._serialized_start=5994
  _globals['_SEATINGMAKEINTERVALSEATINGPAYLOAD']._serialized_end=6061
  _globals['_SEATINGMAKEPRESCRIPTEDSEATINGPAYLOAD']._serialized_start=6063
  _globals['_SEATINGMAKEPRESCRIPTEDSEATINGPAYLOAD']._serialized_end=6148
  _globals['_SEATINGGETNEXTPRESCRIPTEDSEATINGRESPONSE']._serialized_start=6150
  _globals['_SEATINGGETNEXTPRESCRIPTEDSEATINGRESPONSE']._serialized_end=6234
  _globals['_EVENTSGETPRESCRIPTEDEVENTCONFIGRESPONSE']._serialized_start=6237
  _globals['_EVENTSGETPRESCRIPTEDEVENTCONFIGRESPONSE']._serialized_end=6378
  _globals['_EVENTSUPDATEPRESCRIPTEDEVENTCONFIGPAYLOAD']._serialized_start=6380
  _globals['_EVENTSUPDATEPRESCRIPTEDEVENTCONFIGPAYLOAD']._serialized_end=6488
  _globals['_EVENTSGETSTARTINGTIMERRESPONSE']._serialized_start=6490
  _globals['_EVENTSGETSTARTINGTIMERRESPONSE']._serialized_end=6537
  _globals['_CLEARSTATCACHEPAYLOAD']._serialized_start=6539
  _globals['_CLEARSTATCACHEPAYLOAD']._serialized_end=6581
  _globals['_MIMIR']._serialized_start=6584
  _globals['_MIMIR']._serialized_end=11994
# @@protoc_insertion_point(module_scope)