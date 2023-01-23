def grid(user_input):
    first_line = user_input[0:3]
    second_line = user_input[3:6]
    third_line = user_input[6:]
    print("---------")
    print('| ' + " ".join(first_line) + ' |')
    print('| ' + " ".join(second_line) + ' |')
    print('| ' + " ".join(third_line) + ' |')
    print("---------")


def occupied_cell(user_input_, coordinate, player):

    index = (coordinate[0] - 1) * 3 + coordinate[1] - 1
    if user_input_[index] == "X" or user_input_[index] == "O":
        print("This cell is occupied! Choose another one!")
        return True
    else:
        user_input_[index] = player
        grid(user_input_)


def range_error(grid_filler):

    place_range = [1, 2, 3]
    if int(grid_filler[0]) not in place_range or int(grid_filler[1]) not in place_range:
        print("Coordinates should be from 1 to 3!")
        return True


def next_step(grid_filler, player):

    while True:
        coordinates_from_user = input().split(" ")
        try:
            coordinates = [int(coordinate) for coordinate in coordinates_from_user]
        except ValueError:
            print("You should enter numbers!")

        if range_error(coordinates) is not True:
            if occupied_cell(grid_filler, coordinates, player) is not True:
                if not checking_the_winner():
                    break


def checking_the_winner():

    if x[0] != " ":
        if x[0] == x[1] == x[2] or x[0] == x[4] == x[8] or x[0] == x[3] == x[6]:
            letters_won.append(x[0])
    if x[1] != " ":
        if x[1] == x[4] == x[7]:
            letters_won.append(x[1])
    if x[2] != " ":
        if x[2] == x[5] == x[8] or x[2] == x[4] == x[6]:
            letters_won.append(x[2])
    if x[3] != " ":
        if x[3] == x[4] == x[5]:
            letters_won.append(x[3])
    if x[6] != " ":
        if x[6] == x[7] == x[8]:
            letters_won.append(x[6])

    if len(letters_won) == 0:
        if empty not in x:
            print('Draw')
            quit()

    elif len(letters_won) == 1:
        print(f'{letters_won[0]} wins')
        quit()


def playing_tic_tac_toe(games_to_check, grid_filler):
    while True:
        if games_to_check % 2 == 1:
            player = "O"
        else:
            player = "X"

        next_step(grid_filler, player)
        games_to_check += 1


letters_won = []
empty = ' '
x = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
games = 2
grid(x)
playing_tic_tac_toe(games, x)
