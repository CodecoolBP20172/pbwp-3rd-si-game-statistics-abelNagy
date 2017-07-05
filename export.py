# Export functions
import reports
import sys


def printed():
    print('Done. You should find the answer in ' + file_name + '.')

file_abs_path = '/home/abel/codecool/pbwp-3rd-si-game-statistics-abelNagy/game_stat.txt'
file_name = input('What filename.txt do you want to export the answers? ') + '.txt'
file = open('/home/abel/codecool/pbwp-3rd-si-game-statistics-abelNagy/' + file_name, 'w')
print('''\n\nHelo Judy(or whoever this is)!
I can answer the following any of the following 5 questions.
Please choose one that you need the answer for.''')

while True:
    answer = input('''
        1. How many games are in the file?
        2. Is there a game from a given year?
        3. Which was the latest game?
        4. How many games do we have by genre?
        5. What is the line number of the given game (by title)?
        q. Exit program (when you are finished or just want to leave...)
''')
    if answer == 'q':
        final_intent = input('Are you sure you want to quit? (y / n) ')
        if final_intent == 'y':
            file.close()
            sys.exit()
    if answer == '1':
        file.write(str(reports.count_games(file_abs_path)) + '\n')
        printed()
    if answer == '2':
        input_year = input('Which year would you like me to look up? ')
        file.write(str(reports.decide(file_abs_path, input_year)) + '\n')
        printed()
    if answer == '3':
        file.write(str(reports.get_latest(file_abs_path)) + '\n')
        printed()
    if answer == '4':
        input_genre = input('What genre would you like me to get the number of games? ')
        file.write(str(reports.count_by_genre(file_abs_path, input_genre)) + '\n')
        printed()
    if answer == '5':
        input_title = input('Which title would you like me to look up the line number for? ')
        file.write(str(reports.get_line_number_by_title(file_abs_path, input_title)) + '\n')
        printed()

file.close()
