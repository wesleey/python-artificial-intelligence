from typing import List, Set, Tuple, Optional

X = "X"
O = "O"
EMPTY = None


def initial_state() -> List[List[None]]:
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: List[List]) -> str:
    num_x = sum(row.count(X) for row in board)
    num_o = sum(row.count(O) for row in board)
    return X if num_x <= num_o else O


def actions(board: List[List]) -> Set[Tuple[int, int]]:
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board: List[List], action: Tuple[int, int]) -> List[List]:
    i, j = action
    if not (0 <= i < len(board) and 0 <= j < len(board[0])):
        raise ValueError("Action is out of bounds.")
    if board[i][j] is not EMPTY:
        raise ValueError("Cell is already occupied.")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board: List[List]) -> Optional[str]:
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O
    # Check columns
    for col in zip(*board):
        if all(cell == X for cell in col):
            return X
        elif all(cell == O for cell in col):
            return O
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board: List[List]) -> bool:
    return not actions(board) or winner(board) is not None


def utility(board: List[List]) -> int:
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board: List[List]) -> Optional[Tuple[int, int]]:
    if winner(board) is not None:
        return None

    if player(board) == X:
        best_value = float("-inf")
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:
        best_value = float("inf")
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
    return best_action


def max_value(board: List[List]) -> int:
    if terminal(board):
        return utility(board)
    value = float("-inf")
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board: List[List]) -> int:
    if terminal(board):
        return utility(board)
    value = float("inf")
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
