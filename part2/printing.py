# Printing functions
import reports
import sys


def main():
    file_abs_path = '/home/abel/codecool/pbwp-3rd-si-game-statistics-abelNagy/part2/game_stat.txt'
    print('''\n\nHelo Judy(or whoever this is)!
    I can answer your next questions as well.
    Please choose one that you need the answer for.''')

    while True:
        answer = input('''
            1. What is the title of the most played game?
            2. How many copies have been sold total?
            3. What is the average selling?
            4. How many characters long is the longest title?
            5. What is the average of the release dates?
            6. What properties does a game have?
            q. Exit program (when you are finished or just want to leave...)
    ''')
        if answer == 'q':
            final_intent = input('Are you sure you want to quit? (y / n) ')
            if final_intent == 'y':
                sys.exit()
        if answer == '1':
            print('The title of the most played game is %s.' % reports.get_most_played(file_abs_path))
        if answer == '2':
            print('The total number of copies sold is %.2f million.' % reports.sum_sold(file_abs_path))
        if answer == '3':
            print('The average selling is %.2f million copies.' % reports.get_selling_avg(file_abs_path))
        if answer == '4':
            print('The longest title is %g character(s) long.' % reports.count_longest_title(file_abs_path))
        if answer == '5':
            print('The average of the release dates is %g.' % reports.get_date_avg(file_abs_path))
        if answer == '6':
            input_title_prop = input('Which title would you like me to look up the properties for? ')
            print('{0} has the following properties:\n{1}'.format(input_title_prop, reports.get_game(file_abs_path, input_title_prop)))


main()
