# Report functions
# My questions: 1. indentation of the return statement?
# My questions: 2. str.replace() creates a copy. Is there a method that strips the element of a list?


def get_most_played(file_name):
    with open(file_name) as file:
        most_played = ""
        sold_copies = 0
        for line in file:
            line = line.split('\t')
            if float(line[1]) > sold_copies:
                most_played = line[0]
                sold_copies = float(line[1])
    return most_played


def sum_sold(file_name):
    with open(file_name) as file:
        total_sold = 0
        for line in file:
            line = line.split('\t')
            total_sold += float(line[1])
    return total_sold


def get_selling_avg(file_name):
    with open(file_name) as file:
        total_sold = sum_sold(file_name)
        number_of_games = len(file.readlines())
        selling_avg = total_sold / number_of_games
    return selling_avg


def count_longest_title(file_name):
    with open(file_name) as file:
        longest_title = ""
        for line in file:
            line = line.split('\t')
            if len(line[0]) > len(longest_title):
                longest_title = line[0]
    return len(longest_title)


def get_date_avg(file_name):
    with open(file_name) as file:
        number_of_games = []
        total_years = 0
        for line in file:
            line = line.split('\t')
            number_of_games.append(line[0])
            total_years += int(line[2])
    return round(total_years / len(number_of_games))


def get_game(file_name, title):
    with open(file_name) as file:
        for line in file:
            line = line.split('\t')
            if title in line:
                line[1] = float(line[1])
                line[2] = int(line[2])
                line[-1] = line[-1].replace('\n', '')
                return line


def count_grouped_by_genre(file_name):
    with open(file_name) as file:
        games_by_genre = {}
        genre_key = []
        data_as_list = []
        for line in file:
            line = line.split('\t')
            data_as_list.append(line)
            if line[3] not in genre_key:
                genre_key.append(line[3])
        for genre in genre_key:
            count = 0
            for line in data_as_list:
                if line[3] == genre:
                    count += 1
            games_by_genre.update({genre: count})
    return games_by_genre
