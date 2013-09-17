from tmmcalc import TeamMatchMaking

players = (
    {'id': '1',
     'name': 'PeteT',
     'elo': 1723},
    {'id': '2',
     'name': 'MattT',
     'elo': 1489},
    {'id': '3',
     'name': 'AlexB',
     'elo': 1616},
    {'id': '4',
     'name': 'RobF',
     'elo': 1618},
    {'id': '5',
     'name': 'ChrisF',
     'elo': 1564},
    {'id': '6',
     'name': 'ChrisH',
     'elo': 1644},
    {'id': '7',
     'name': 'AlexH',
     'elo': 1430},
    {'id': '8',
     'name': 'RichB',
     'elo': 1512},
    {'id': '9',
     'name': 'MarkG',
     'elo': 1309},
    {'id': '10',
     'name': 'TimH',
     'elo': 1829},
)

if __name__ == "__main__":
    tmm = TeamMatchMaking(debug=True)
    for player in players:
        tmm.add_player(player)
    tmm.shuffle_teams()