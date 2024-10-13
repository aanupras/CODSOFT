def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_valid_move(board, row, col):
    return board[row][col] == ' '

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':  #x is AI 
        return 1
    elif winner == 'O': #o is Human
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game")
    print_board(board)
    game_over = False
    while not game_over:
   
        row, col = map(int, input("Enter your move (row and column from 0 to 2): ").split())
        if not make_move(board, row, col, 'O'):
            print("Invalid move, try again.")
            continue
        print_board(board)
        if check_winner(board):
            print("Congratulations! You win!")
            game_over = True
            break
        if is_draw(board):
            print("It's a draw!")
            game_over = True
            break

        ai_move = best_move(board)
        if ai_move:
            make_move(board, ai_move[0], ai_move[1], 'X')
            print("\nAI's Move:")
            print_board(board)
        
        if check_winner(board):
            print("AI wins! Better luck next time.")
            game_over = True
            break
        if is_draw(board):
            print("It's a draw!")
            game_over = True
            break

play_game()
