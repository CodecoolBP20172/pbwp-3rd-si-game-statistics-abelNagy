# Report functions


def count_games(file_name):
    with open(file_name) as file:
        game_count = file.readlines()
    return len(game_count)


def decide(file_name, year):
    with open(file_name) as file:
        year = str(year)
        for line in file:
            if year in line:
                return True
    return False


def get_latest(file_name):
    with open(file_name) as file:
        latest_game_name = ""
        latest_game_date = 0
        for line in file:
            line = line.split('\t')
            if int(line[2]) > latest_game_date:
                latest_game_name = line[0]
                latest_game_date = int(line[2])
        return latest_game_name


def count_by_genre(file_name, genre=None):
    with open(file_name) as file:
        games_by_genre = 0
        for line in file:
            line = line.split('\t')
            if genre == line[3]:
                games_by_genre += 1
        return games_by_genre


def get_line_number_by_title(file_name, title):
    with open(file_name) as file:
        line_number = 0
        for line in file:
            line_number += 1
            line = line.split('\t')
            if title == line[0]:
                return line_number
        else:
            raise ValueError('No game found with that title')
