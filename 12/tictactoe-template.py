from typing import Any, List, Optional

DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)
PLAYERS = ('X', '0')


class TicTacToe:

    def __init__(self) -> None:
        '''Constructor, below worked well for us ...'''
        self.board = [''] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    def __str__(self) -> str:
        '''Print the board'''
        return '\n'.join(' '.join(self.board[i:i+3]) for i in range(7, 0, -3))
        
    def is_win(self) -> Optional[str]:
        for combination in WINNING_COMBINATIONS:
            for player in PLAYERS:
                if all(self.board[i] == player for i in combination):
                    return player
        return None

    def is_tie(self) -> bool:
        if all(i != DEFAULT for i in self.board[1:]):
            return True
        return False

    def take_turn(self, player: str, position: int):
        try:
            position = int(position)
        except ValueError:
            raise ValueError('Not a valid position')
        if player not in PLAYERS:
            raise ValueError('Not a valid player')
        if position not in VALID_POSITIONS:
            raise ValueError('Not a valid position')
        if self.board[position] != DEFAULT:
            raise ValueError('Position is already taken')
        self.board[position] = player

    def input_move(self, player: str):
        try:
            self.take_turn(player, input(f'Pick a square for player {player}...'))
        except ValueError as e:
            print(e)
            self.input_move(player)
        

    # TODOS:
    # display board in __str__ (clearing screen)
    # have at least an is_win method to exit game
    # num turns = len(VALID_POSITIONS) so might not need is_draw (tie) method
    # have method(s) to get user input and validate
    # if playing against computer (AI) calculate next best move (algorithm)
    # update board upon each turn


if __name__ == "__main__":
    game = TicTacToe()
    while True:
        print(game)
        game.input_move('X')
        print('\n\n\n\n\n\n\n\n\n\n\n')
        # take turn
        # make move
        # check win - break
        #
        # ask if another game, if n - break
