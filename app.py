import constants


def clean_data(data):
    clean_players = []
    for item in data:
        player = {}
        player['name'] = item['name']
        player['guardians'] = item['guardians'].split(" and ")
        if item['experience'] == 'NO':
            player['experience'] = False
        if item['experience'] == 'YES':
            player['experience'] = True
        player['height'] = int(item['height'].split()[0])
        clean_players.append(player)
    return clean_players
        

def balance_teams(player_list, team_list):
    num_players_team = len(player_list) / len(team_list)
    sorted_list = sorted(player_list, key=lambda value: value['experience'])
    team1 = [sorted_list[0], sorted_list[1], sorted_list[2], sorted_list[9], sorted_list[10], sorted_list[11]]
    team2 = [sorted_list[3], sorted_list[4], sorted_list[5], sorted_list[12], sorted_list[13], sorted_list[14]]
    team3 = [sorted_list[6], sorted_list[7], sorted_list[8], sorted_list[15], sorted_list[16], sorted_list[17]]
    return team1, team2, team3


def average_height(players):
    total_height = 0
    num_players = len(players)
    for player in players:
        total_height += player['height']
    return total_height / num_players


def print_team_name(team):
    team_name = constants.TEAMS[team]
    print("""

Team: {}
--------------------""".format(team_name))


def print_team(team):
    total_players = len(team)
    player_name_list = []
    player_guardian_list = []
    experienced = 0
    inexperienced = 0
    for player in team:
        if player['experience'] == True:
            experienced += 1
        if player['experience'] == False:
            inexperienced += 1
        player_name_list.append(player['name'])
        for i in player['guardians']:
            player_guardian_list.append(i)
    avg_height = round(average_height(team), 1)
    names_str = ', '.join(player_name_list)
    guardians_str = ', '.join(player_guardian_list)
    print("""
Total players: {}
Total experienced: {}
Total inexperienced: {}
Average height: {}

Players on Team:
{}

Guardians:
{}
        """.format(total_players, experienced, inexperienced, avg_height, names_str, guardians_str))
    continue_program = "lolz"
    while continue_program != "":
        continue_program = input("Press ENTER to continue...  ")
        try:
            continue_program = str(continue_program)
        except ValueError:
            break
        if continue_program == "":
            break
    return None
    

def team_stats():
    value_error_message = "Sorry, please enter '1', '2', or '3'"
    team_choice = 0
    while team_choice != 1 or team_choice != 2 or team_choice != 3:
        print("""
    
Please select a team:
1) {}
2) {}
3) {}
        
        """.format(constants.TEAMS[0], constants.TEAMS[1], constants.TEAMS[2]))
        team_choice = input("Please select an option >  ")
        try:
            team_choice = int(team_choice)
        except ValueError:
            print("That's not a number!")
        if team_choice == 1:
            print_team_name(0)
            print_team(team1)
            break
        elif team_choice == 2:
            print_team_name(1)
            print_team(team2)
            break
        elif team_choice == 3:
            print_team_name(2)
            print_team(team3)
            break
        else:
            print(value_error_message)
    return None
    
    
def main():
    run_program()


def run_program():
    value_error_message = "Sorry, please enter '1' or '2'"
    print("""
BASEKETBALL TEAM STATS TOOL

----MENU----""")
    menu_nav = 0
    while menu_nav != 1 or menu_nav != 2:
        print("""
Please select one of the following options:
1) Display Team Stats
2) Quit
        """)
        menu_nav = input("Please select an option >  ")
        try:
            menu_nav = int(menu_nav)
        except ValueError:
            print("That's not a number!")
        if menu_nav == 1:
            team_stats()
        elif menu_nav == 2:
            break
        elif menu_nav == None:
            break
        else:
            print(value_error_message)
            continue

            
if __name__ == "__main__":
    clean_players = clean_data(constants.PLAYERS)
    team1, team2, team3 = balance_teams(clean_players, constants.TEAMS)
    main()
