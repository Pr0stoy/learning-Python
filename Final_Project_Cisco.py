import random
board = [
    ["1","2","3"],
    ["4","X","6"],
    ["7","8","9"]
    ]
def display_board(board):
    print("+-------+-------+-------+\n"
    "|       |       |       |\n"
    f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n"
    "|       |       |       |\n"
    "+-------+-------+-------+\n"

    "|       |       |       |\n"
    f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n"
    "|       |       |       |\n"
    "+-------+-------+-------+\n"

    "|       |       |       |\n"
    f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n"
    "|       |       |       |\n"
    "+-------+-------+-------+\n")    
def make_list_of_free_fields(board):
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O" or board[i][j] == "X":
                pass
            else:
                free_squares.append(board[i][j])
    return free_squares

def victory_for(board, sign):
    if  (board[0][0] == board[0][1] == board[0][2] == sign) or \
       (board[1][0] == board[1][1] == board[1][2] == sign) or \
       (board[2][0] == board[2][1] == board[2][2] == sign) or \
        (board[0][0] == board[1][0] == board[2][0] == sign) or \
       (board[0][1] == board[1][1] == board[2][1] == sign) or \
       (board[0][2] == board[1][2] == board[2][2] == sign) or \
        (board[0][0] == board[1][1] == board[2][2] == sign) or \
       (board[0][2] == board[1][1] == board[2][0] == sign):
        return True
    return False
def draw_move(board):   
    bot_move = 0
    while str(bot_move) not in make_list_of_free_fields(board):
        bot_move = random.randrange(1,10)
    bot_row = (bot_move-1)//3
    bot_col = (bot_move-1)%3
    board[bot_row][bot_col] = "X"

def enter_move(board):
    try:    
        while not victory_for(board,"O") and not victory_for(board,"X") and len(make_list_of_free_fields(board)) != 0:
            display_board(board)
            player_move = int(input("Write your move: "))
            player_row = (player_move-1)//3
            player_col = (player_move-1)%3
            if player_move not in range(1,10) or str(player_move) not in make_list_of_free_fields(board):
                print("Wrong choice!\n Restart the programm")
                break
            else:
                board[player_row][player_col] = "O"
                if victory_for(board,"O") == True:
                            pass
                elif victory_for(board,"X") == True:
                            pass
                elif len(make_list_of_free_fields(board)) == 0:
                            pass
                else:
                    draw_move(board)

        else:
            if victory_for(board,"O") == True:
                print("You win!")
            elif victory_for(board,"X") == True:
                print("You've lost(")
            elif len(make_list_of_free_fields(board)) == 0:
                print("DRAW")
    except:
         print("You've typed some shi...")
enter_move(board)
