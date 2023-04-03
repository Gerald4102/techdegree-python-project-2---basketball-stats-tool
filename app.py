import constants

def clean_data(players):
    cleaned_players = []
    for player in players:
        if player['experience'] == 'YES':
            player_exp = True
        else:
            player_exp = False       
        height, units = player['height'].split(' ')
        cleaned_players.append({
            'name':player['name'], 
            'guardians':player['guardians'], 
            'experience':player_exp, 
            'height': height
            })
    return cleaned_players


def balance_team(players, team):
    players_per_team = len(players) / len(team)
    return players_per_tea


if __name__ == "__main__":

    players = clean_data(constants.PLAYERS)
    # print(players)

    x = balance_team(constants.PLAYERS, constants.TEAMS)
    print(x)