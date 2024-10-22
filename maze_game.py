"""
This code was originally written in 2023.

This is a simple program that reads a text file containing a maze, and then has the user solve the maze using input().
This program assumes that the maze text file has walls (represented by the # symbol) surrounding the entire maze, making it impossible for the player to go out of bounds.

Maze Game Instructions:
You are given a maze to solve.
* is you.
O is the finish.
# is a wall you cannot pass through.
$ is a key you must collect before going to the finish.
If you do not collect all the keys, you cannot enter the finish.
You move by entering a string.
You can make your string as long as you want, and you can take as many turns as you want.
u is up.
d is down.
l is left.
r is right.
q is quit.
All other characters are ignored.
"""

# You can make your own .txt file with your own maze, and set the filename to that
filename = "sample_maze.txt"
##################################################################################


def print_maze(maze):
    """
    Print the maze
    :param maze: a list of lists containing the maze
    :post-cond: the maze gets printed to the console
    """
    for row in maze:
        for character in row:
            print(character, end="")
        # print a newline at the end of each row
        print("")


def is_maze_solved(cursor_row, cursor_column, finish_row, finish_column, number_keys):
    """
    Determine whether the maze is solved
    :param cursor_row: an integer representing the row index of the cursor
    :param cursor_column: an integer representing the column index of the cursor
    :param finish_row: an integer representing the row index of the finish
    :param finish_column: an integer representing the column index of the finish
    :param number_keys: an integer representing the number of keys left in the maze
    :return: True if all the keys are collected and the cursor is in the same place as the finish, False otherwise
    """
    if number_keys > 0:
        return False
    # cursor is at the finish
    elif cursor_row == finish_row and cursor_column == finish_column:
        return True
    else:
        return False


def is_move_legal(maze, check_row, check_column, number_keys):
    """
    Check if a cursor can be in a specific position in the maze
    :param maze: a list of lists containing the maze
    :param check_row: an integer representing the row index of the position to be checked
    :param check_column: an integer representing the column index of the position to be checked
    :param number_keys: an integer representing the number of keys remaining in the maze
    :return: True if the position is legal, False if the position is not legal
    """
    # wall piece
    if maze[check_row][check_column] == "#":
        return False
    # user reaches finish but did not collect all the keys
    elif number_keys > 0 and maze[check_row][check_column] == "O":
        return False
    else:
        return True


def move_cursor(maze, direction, cursor_row, cursor_column, number_keys):
    """
    Move the cursor on the maze
    :param maze: a list of lists containing the maze
    :param direction: a character representing the direction to move the cursor
    :param cursor_row: an integer representing the row index of the cursor
    :param cursor_column: an integer representing the column index of the cursor
    :param number_keys: an integer representing the number of keys remaining in the maze
    :post-cond: the * in maze will move if the move is legal
    :return: a tuple containing the new coordinates of the cursor and the number of remaining keys in the maze
    """
    new_row = cursor_row
    new_column = cursor_column
    # set new cursor point depending on the direction given
    if direction == "u":
        new_row -= 1
    elif direction == "d":
        new_row += 1
    elif direction == "l":
        new_column -= 1
    elif direction == "r":
        new_column += 1
    else:
        pass
    if is_move_legal(maze, new_row, new_column, number_keys):
        # change the number of keys remaining if the new coordinates land on a key
        if maze[new_row][new_column] == "$":
            number_keys -= 1
        # change the position of the cursor in the maze
        maze[cursor_row][cursor_column] = " "
        maze[new_row][new_column] = "*"
        return (new_row, new_column, number_keys)
    else:
        # if the move is not legal, return the old coordinates of the cursor
        return (cursor_row, cursor_column, number_keys)


# get maze information from the file
maze = []  # list of lists containing the maze
file = open(filename, "r")
number_keys = 0  # the number of keys the user must collect before finishing the maze
for line in file:
    row_string = line.rstrip()
    maze_row = []
    for character in row_string:
        maze_row.append(character)
        if character == "$":
            number_keys += 1
    maze.append(maze_row)
file.close()

# set cursor and finish points
cursor_row = -1
cursor_column = -1
finish_row = -1
finish_column = -1
for row_index in range(len(maze)):
    for column_index in range(len(maze[row_index])):
        if maze[row_index][column_index] == "*":
            # cursor starting point
            cursor_row = row_index
            cursor_column = column_index
        elif maze[row_index][column_index] == "O":
            # maze finish point
            finish_row = row_index
            finish_column = column_index
        else:
            pass

# maze instructions
print("Maze Game")
print("You are given a maze to solve.\n* is you.\nO is the finish.\n# is a wall you cannot pass through.")
print("$ is a key you must collect before going to the finish.")
print("If you do not collect all the keys, you cannot enter the finish.")
print("You move by entering a string.")
print("You can make your string as long as you want, and you can take as many turns as you want.")
print("u is up.\nd is down.\nl is left.\nr is right.\nq is quit.\nAll other characters are ignored.")

# play the maze game
finished = False
user_quit = False
while not finished and not user_quit:
    print_maze(maze)
    next_move = input("Enter move: ")
    for move_direction in next_move:
        if move_direction == "u" or move_direction == "d" or move_direction == "l" or move_direction == "r":
            # move the cursor
            new_point = move_cursor(maze, move_direction, cursor_row, cursor_column, number_keys)
            # set new cursor position and number of keys
            cursor_row = new_point[0]
            cursor_column = new_point[1]
            number_keys = new_point[2]
            # if the maze is solved, all other moves in the string are ignored
            if is_maze_solved(cursor_row, cursor_column, finish_row, finish_column, number_keys):
                finished = True
                break
            else:
                pass
        elif move_direction == "q":
            # if the user quits, ignore the rest of the string
            user_quit = True
            break
        else:
            pass

# maze game ending
print_maze(maze)
if finished:
    print("You win!")
elif user_quit:
    print("You quit.")
else:
    pass
