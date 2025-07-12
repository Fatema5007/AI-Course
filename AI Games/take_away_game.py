import time

# Minimax algorithm with alpha-beta pruning
def minimax(tokens_left, is_max_turn, alpha, beta):
    # Base case: no tokens left
    if tokens_left == 0:
        return -1 if is_max_turn else 1  # If max's turn and no tokens, max lost → -1

    if is_max_turn:
        max_eval = -float('inf')  # Start with the worst case
        for move in range(1, 4):  # Try removing 1, 2, or 3 tokens
            if move <= tokens_left:
                eval = minimax(tokens_left - move, False, alpha, beta)  # Switch to minimizing turn
                max_eval = max(max_eval, eval)  # Track best score for max
                alpha = max(alpha, eval)        # Update alpha
                if beta <= alpha:
                    break  # Beta cut-off: pruning
        return max_eval
    else:
        min_eval = float('inf')  # Start with the worst case for min
        for move in range(1, 4):  # Try removing 1, 2, or 3 tokens
            if move <= tokens_left:
                eval = minimax(tokens_left - move, True, alpha, beta)  # Switch to maximizing turn
                min_eval = min(min_eval, eval)  # Track best score for min
                beta = min(beta, eval)          # Update beta
                if beta <= alpha:
                    break  # Alpha cut-off: pruning
        return min_eval

# Choose the best move for the AI using minimax
def find_best_move(tokens_left):
    best_move = None
    best_value = -float('inf')  # Start with lowest score for maximizer

    for move in range(1, 4):  # Try all moves (1, 2, 3)
        if move <= tokens_left:
            move_value = minimax(tokens_left - move, False, -float('inf'), float('inf'))
            if move_value > best_value:
                best_value = move_value
                best_move = move  # Store the move with highest value
    return best_move

# Game logic for player vs computer
def play_take_away():
    tokens = 20  # Start with 20 tokens
    print("Welcome to the Take Away Game!")
    print("There are 20 tokens.")
    print("Each turn, you can remove 1, 2, or 3 tokens.")
    print("The player who removes the last token wins.\n")

    while tokens > 0:
        # Show remaining tokens
        print(f"Tokens left: {tokens}")
        user_move = 0

        # Validate user input
        while user_move not in [1, 2, 3] or user_move > tokens:
            try:
                
                user_move = int(input("Your move (remove 1, 2, or 3 tokens): "))
            except ValueError:
                continue

        # Update token count after player's move
        tokens -= user_move
        if tokens == 0:
            print("You took the last token. You win!")
            break

        # Computer's turn
        print("AI is making a move...")
        time.sleep(2)
        comp_move = find_best_move(tokens)
        tokens -= comp_move
        print(f"Computer removes {comp_move} token(s). Tokens left: {tokens}")

        if tokens == 0:
            print("Computer took the last token. Computer wins!")
            break

# Start the game
if __name__ == "__main__":
    play_take_away()
