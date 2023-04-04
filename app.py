import constants_copy
import copy
import random

def clean_data(players):
    cleaned_players = []
    for player in players:
        if player['experience'] == 'YES':
            player_exp = True
        else:
            player_exp = False       
        height, units = player['height'].split(' ')
        guardians = player['guardians'].split(' and ')
        cleaned_players.append({
            'name':player['name'], 
            'guardians':guardians, 
            'experience':player_exp, 
            'height': int(height)
            })
    return cleaned_players


def balance_team(players, teams_names):

    experienced_players = []
    inexperienced_players = []

    for player in players:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    
    experienced_players_per_team = int(len(experienced_players) / len(teams_names))
    inexperienced_players_per_team = int(len(inexperienced_players) / len(teams_names))

    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)

    # unnamed_teams = []
    # counter_experienced = 0
    # counter_inexperienced = 0
    
    # for team_name in teams_names:
    #     new_team = []
    #     experienced_slice = slice(counter_experienced, experienced_players_per_team + counter_experienced)
    #     for player in experienced_players[experienced_slice]:
    #         new_team.append(player)
    #     counter_experienced += experienced_players_per_team

    #     inexperienced_slice = slice(counter_inexperienced, inexperienced_players_per_team + counter_inexperienced)
    #     for player in inexperienced_players[inexperienced_slice]:
    #         new_team.append(player)
    #     counter_inexperienced += inexperienced_players_per_team

    #     unnamed_teams.append(new_team)
    # teams = list(zip(teams_names,unnamed_teams))


    teams = []
    for name in teams_names:
        team = [name,[]]
        teams.append(team)

    counter = 0
    for player in experienced_players:
        teams[counter % len(teams)][1].append(player)
        counter += 1

    counter = 0
    for player in inexperienced_players:
        teams[counter % len(teams)][1].append(player)
        counter += 1
    
    check(constants_copy.TEAMS, constants_copy.PLAYERS, teams)
    return teams

def check(data_teams, data_players, teams):
    num_players_team = int(len(data_players) / len(data_teams))
    errors = []
    for team in teams:
        if len(team[1]) != num_players_team:
            errors.append(f'Team {team[0]} have {len(team[1])} players. There are teams with only {num_players_team} players.')
    try:
        check = (len(errors) == 0)
        if check == False:
            raise Exception(errors)
    except Exception as error:
        for error in errors:
            print(error)



def stats_main_menu():
    print("""
BASKETBALL TEAM STATS TOOL

---- MENU----

Here are your choices:
1) Display Team Stats
2) Quit
    """)
    while True:
        menu_choice = input('Enter an option > ')
        if menu_choice == '1':
            stats_team_menu()
        elif menu_choice == '2':
            print('Bye! \n')
            exit()
        else:
            continue
    
def stats_team_menu():

    team_numb = 1
    for team in teams:
        print(f'{team_numb}) {team[0]}')
        team_numb += 1
    print()

    while True:
        team_choice = int(input('Enter an option > '))
        if team_choice > 0 and team_choice <= len(teams):
            stats(team_choice - 1)
        else:
            continue

def stats(team):
    num_of_players = len(teams[team][1])
    player_list = []
    num_experienced = 0
    num_inexperienced = 0
    combined_height = 0
    guardians = []
    for player in teams[team][1]:
        player_list.append(player['name'])
        if player['experience'] == True:
            num_experienced += 1
        else:
            num_inexperienced += 1
        combined_height += player['height']
        for guardian in player['guardians']:
            guardians.append(guardian)
    players_string = ', '.join(player_list)
    ave_height = round(combined_height / num_of_players, 1)
    guardians_string = ', '.join(guardians)


    print(f'\nTeam: {teams[team][0]} Stats')
    print('--------------------')
    print('Total players:', num_of_players)
    print(f'Total experienced: {num_experienced}')
    print(f'Total inexperienced: {num_inexperienced}')
    print(f'Average height: {ave_height}')

    print('\nPlayers on team:\n ', players_string)
    print('\nGuardians:\n ', guardians_string, '\n')
    while True:
        print('Press ENTER to continue...')
        key = input()
        if key == '':
            stats_main_menu()

if __name__ == "__main__":
    copied_players = copy.deepcopy(constants_copy.PLAYERS)
    players = clean_data(copied_players)

    copied_teams = copy.deepcopy(constants_copy.TEAMS)
    teams = balance_team(players, copied_teams)

    
    # for team in teams:
    #     print(team[0])
    #     for player in team[1]:
    #         print(player)
    #     print()

    stats_main_menu()

