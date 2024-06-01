import gui
import sys
import time
import tictactoe as ttt


game = gui.GUI()
board = ttt.initial_state()
ai_turn = False
user = None
tiles = []


def menu() -> None:
    try:
        run()
    except KeyboardInterrupt:
        sys.exit("Game exited.")


def run() -> None:
    while True:
        for event in game.events():
            if game.quit(event):
                sys.exit()
        game.background(gui.BLACK)
        draw_home() if user is None else draw_game()
        game.show()


def draw_home() -> None:
    title = gui.Title("Play Tic-Tac-Toe")
    title.align((gui.HORIZONTAL, 50))
    title.draw(game.screen)

    # Draw buttons
    left = gui.WIDTH / 8
    top = gui.HEIGHT / 2
    width = gui.WIDTH / 4
    height = 50

    button_x = gui.Button("Play as X", left, top, width, height)
    button_x.onclick(set_user)
    button_x.draw(game.screen)

    left = button_x.left * 5
    button_o = gui.Button("Play as O", left, top, width, height)
    button_o.onclick(set_user)
    button_o.draw(game.screen)

    if game.mouse_pressed():
        button_x.handle_click(ttt.X)
        button_o.handle_click(ttt.O)


def draw_game() -> None:
    draw_board()

    player = ttt.player(board)
    game_over = ttt.terminal(board)

    status = game_status(game_over, player)
    title = gui.Title(status)
    title.align((gui.HORIZONTAL, 30))
    title.draw(game.screen)

    check_ai_turn(game_over, player)

    if game_over:
        draw_reset_game_button()

    if game.mouse_pressed():
        check_user_turn(game_over, player)


def draw_board() -> None:
    global tiles
    tile_size = 80
    origin = [(gui.WIDTH / 2) - (1.5 * tile_size),
              (gui.HEIGHT / 2) - (1.5 * tile_size)]

    for i in range(3):
        row = []
        for j in range(3):
            button = gui.Button(
                text=board[i][j],
                left=origin[0] + j * tile_size,
                top=origin[1] + i * tile_size,
                width=tile_size,
                height=tile_size,
                color=gui.WHITE
            )
            button.onclick(user_move)
            button.draw(game.screen, width=3)
            row.append(button)
        tiles.append(row)


def game_status(game_over: bool, player: str) -> str:
    if game_over:
        winner = ttt.winner(board)
        if winner is None:
            return "Game Over: Tie."
        else:
            return f"Game Over: {winner} wins."
    elif user == player:
        return f"Play as {user}"
    else:
        return "Computer thinking..."


def check_ai_turn(game_over: bool, player: str) -> None:
    global ai_turn, board
    if not game_over and user != player:
        if ai_turn:
            time.sleep(0.5)
            move = ttt.minimax(board)
            board = ttt.result(board, move)
            ai_turn = False
        else:
            ai_turn = True


def check_user_turn(game_over: bool, player: str) -> None:
    if not game_over and user == player:
        for i in range(3):
            for j in range(3):
                button = tiles[i][j]
                button.handle_click(i, j)


def draw_reset_game_button():
    button = gui.Button(
        text="Play Again",
        left=gui.WIDTH / 3,
        top=gui.HEIGHT - 65,
        width=gui.WIDTH / 3,
        height=50
    )
    button.onclick(reset_game)
    button.draw(game.screen)

    if game.mouse_pressed():
        button.handle_click()


def set_user(player: str) -> None:
    global user
    user = player


def user_move(i: int, j: int) -> None:
    global board
    if board[i][j] == ttt.EMPTY:
        board = ttt.result(board, (i, j))


def reset_game() -> None:
    time.sleep(0.2)
    global board, ai_turn, user
    board = ttt.initial_state()
    ai_turn = False
    user = None


if __name__ == "__main__":
    menu()
