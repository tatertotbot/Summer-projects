def pretty_print(board):
    for row in board:
        for col in row:
            if col == 1:
                print(" X |", end="")
            elif col == 2:
                print(" O |", end="")
            else:
                print("   |", end="")
        print("\n-------------")


def move(board, turn):
    # check if its a valid move
    invalid = True

    while invalid:
        row = int(input("Player {}: which row would you like to move in?".format(turn)))
        column = int(input("Player {}: which column would you like to move in?".format(turn)))
        invalid = False

        if row > 3 or row < 1 or column > 3 or column < 1:
            print("invalid move.  pick between 1-3")
            invalid = True
        elif board[row - 1][column - 1] != 0:
            print("position already taken!!")
            invalid = True

    board[row-1][column-1] = turn


def check_win(arr2):
    for row in arr2:
        if row[0] == row[1] == row[2] and row[0] != 0:
            print("Player {} won the game!".format(row[0]))
            return True

    for i in range(len(arr2)):
        temp = []
        for j in range(len(arr2)):
            temp.append(arr2[j][i])
        if temp[0] == temp[1] == temp[2] and temp[0] != 0:
            print("Player {} won the game!".format(temp[0]))
            return True

    if (arr2[0][0] == arr2[1][1] == arr2[2][2] or arr2[0][2] == arr2[1][1] == arr2[2][0]) and arr2[1][1] != 0:
        print("Player {} won the game!".format(arr2[1][1]))
        return True
    return False


def main():
    game_over = False

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    while not game_over:
        pretty_print(board)
        move(board, 1)
        if check_win(board):
            break

        pretty_print(board)
        move(board, 2)
        if check_win(board):
            break
    print("game over")


main()
