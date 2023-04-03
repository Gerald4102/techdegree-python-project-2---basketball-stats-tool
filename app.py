import constants
import random

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


def balance_team(players, teams):
    players_per_team_float = len(players) / len(teams)
    players_per_team = int(players_per_team_float)
    shuffled_players = players.copy()
    random.shuffle(shuffled_players)
    balanced_teams = []
    counter = 0
    for team in teams:
        new_team = slice(counter, players_per_team + counter)
        balanced_teams.append(shuffled_players[new_team])
        counter += players_per_team

    
    return balanced_teams


if __name__ == "__main__":

    players = clean_data(constants.PLAYERS)
    # print(players)

    x = balance_team(players, constants.TEAMS)
    print(x[0])
    print(x[1])
    print(x[2])