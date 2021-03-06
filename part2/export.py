# Export functions

# Export functions
import reports
import sys


def main():
    file_abs_path = '/home/abel/codecool/pbwp-3rd-si-game-statistics-abelNagy/part2/game_stat.txt'
    file_name = input('What filename do you want to export the answers to? ') + '.txt'
    file = open('/home/abel/codecool/pbwp-3rd-si-game-statistics-abelNagy/part2/' + file_name, 'w')

    def feedback():
        print('Done. You should find the answer in ' + file_name + '.')

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
                file.close()
                sys.exit()
        if answer == '1':
            file.write(str(reports.get_most_played(file_abs_path)) + '\n')
            feedback()
        if answer == '2':
            file.write(str(reports.sum_sold(file_abs_path)) + '\n')
            feedback()
        if answer == '3':
            file.write(str(reports.get_selling_avg(file_abs_path)) + '\n')
            feedback()
        if answer == '4':
            file.write(str(reports.count_longest_title(file_abs_path)) + '\n')
            feedback()
        if answer == '5':
            file.write(str(reports.get_date_avg(file_abs_path)) + '\n')
            feedback()
        if answer == '6':
            input_title_prop = input('Which title would you like me to look up the properties for? ')
            file.write(str(reports.get_game(file_abs_path, input_title_prop)) + '\n')
            feedback()
        if answer == '7':
            file.write(str(reports.count_grouped_by_genre(file_abs_path)))
            feedback()


main()
