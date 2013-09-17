from itertools import combinations


class TeamMatchMaking(object):

    def __init__(self, **kwargs):
        self.__debug = False
        self._match_full = False
        self.player_list = []
        self.team_size = 5
        self.team_one = {}
        self.team_two = {}
        self._set_debug(kwargs.get('debug', False))
        # Set the team size, 5v5 by default
        self.set_team_size(kwargs.get('team_size', 5))

    def __debug_print(self, stmt):
        if self.__debug:
            print(stmt)

    def _set_debug(self, debug):
        self.__debug = debug

    def _set_match_full(self):
        # Check if we have enough players, set flag
        if len(self.player_list) == (self.team_size * 2):
            self._match_full = True
            self.__debug_print("Match is full...")
        else:
            self._match_full = False

    def add_player(self, player):
        # If match is full, don't accept any more players
        if not self._match_full:
            # Check that the player object has the necessary data
            required_fields = ('id', 'name', 'elo')
            for field in required_fields:
                if field not in player or not player[field]:
                    raise ValueError("Missing player field: {0}".format(field))
            # Add the player to the list, set match full trigger
            self.player_list.append(player)
            self.__debug_print("Added player: {0}...".format(player['name']))
            self._set_match_full()

    def remove_player(self, player_id):
        for i, player in enumerate(self.player_list):
            if player['id'] == player_id:
                self.player_list.pop(i)
                self.__debug_print("Removed player: {0}...".format(player['name']))
                self._set_match_full()

    def set_team_size(self, team_size):
        # Set the team size, between 1v1 and 5v5
        if 1 > int(team_size) > 5:
            raise ValueError("Team size must be between 1 and 5")
        self.team_size = team_size
        self.__debug_print("Team size set to {0} vs {0}...".format(team_size))

    def shuffle_teams(self):
        # Get list of distinct team combinations
        team_combos = list(combinations(self.player_list, self.team_size))
        halfway_point = len(team_combos) / 2
        # Split list into halves, reversing second half lines up
        # team1 with it's team2 counterpart
        team1_list, team2_list = team_combos[:halfway_point], team_combos[:halfway_point-1:-1]
        team_pairs = [(team1_list[x], team2_list[x]) for x in range(halfway_point)]
        for team1, team2 in team_pairs:
            team1_elo = sum([player['elo'] for player in team1]) / self.team_size
            team2_elo = sum([player['elo'] for player in team2]) / self.team_size

        print len(team_pairs)