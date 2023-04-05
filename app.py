import constants
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
    
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)

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
    
    check(constants.TEAMS, constants.PLAYERS, teams)
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
            print('\nPlease choose one of the options\n')
            continue


def stats_team_menu():

    team_numb = 1
    for team in teams:
        print(f'{team_numb}) {team[0]}')
        team_numb += 1
    largest_numb = team_numb - 1  
    print()

    while True:
        team_choice = input('Enter an option > ')
        try:
            team_choice = int(team_choice)
            if not (team_choice > 0 and team_choice <= len(teams)):
                raise IndexError('\nThere is no team with that number!\n')
        except ValueError:
            print(f'\nPlease choose one of the team numbers... 1 to {largest_numb}\n')
            continue   
        except IndexError as err:
            print(f'{err}')
            continue
        else:
            stats(team_choice - 1)


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
    copied_players = copy.deepcopy(constants.PLAYERS)
    players = clean_data(copied_players)

    copied_teams = copy.deepcopy(constants.TEAMS)
    teams = balance_team(players, copied_teams)

    stats_main_menu()
