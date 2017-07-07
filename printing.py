# Printing functions
import reports
import sys


def main():
    file_abs_path = '/home/abel/codecool/pbwp-3rd-si-game-statistics-abelNagy/game_stat.txt'
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
                sys.exit()
        if answer == '1':
            print('There are %g games in the file.' % reports.count_games(file_abs_path))
        if answer == '2':
            try:
                input_year = int(input('Which year would you like me to look up? '))
                if input_year < 0:
                    print('Please only enter poisitve numbers.')
                    continue
                elif not len(str(input_year)) == 4:
                    print('Please enter 4 digits.')
                    continue
            except ValueError:
                print('Please enter a number.')
                continue
            if reports.decide(file_abs_path, input_year) is True:
                print('Yes, there is a game from %s.' % input_year)
            else:
                print('No, there is not a game from %s.' % input_year)
        if answer == '3':
            print('The latest game was %s.' % reports.get_latest(file_abs_path))
        if answer == '4':
            input_genre = input('What genre would you like me to get the number of games? ')
            print('There are {0} games with the {1} genre.'.format(reports.count_by_genre(file_abs_path, input_genre), input_genre))
        if answer == '5':
            try:
                input_title_line = input('Which title would you like me to look up the line number for? ')
                print('The line number of {0} is {1}.'.format(input_title_line, reports.get_line_number_by_title(file_abs_path, input_title_line)))
            except ValueError:
                print('No title found.')
                continue


main()
