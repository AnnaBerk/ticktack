import random
import re
from itertools import cycle


class Player:
    def __init__(self, turn, opponent_turn):
        self.turn = turn  # X or O
        self.status = ''  # User or AI
        self.opponent_turn = opponent_turn


first_player = Player('X', 'O')
second_player = Player('O', 'X')

DEFAULT_PLAYERS = (
    first_player,
    second_player
)


class Ticktacktoe:
    WIN_RULES = [range(i, 9, 3) for i in range(3)] + [range(i, i + 3) for i in range(0, 9, 3)] + \
                [range(0, 9, 4), range(2, 7, 2)]

    def __init__(self, players=DEFAULT_PLAYERS):
        self.board = list(' ' * 9)
        self._players = cycle(players)
        self.current_player = next(self._players)
        self.game_status = 'Game not finished'

    def show_board(self):
        print(9 * '-' + (3 * '\n| {} {} {} |').format(*self.board) + '\n' + 9 * '-')

    def update_status(self):
        xcount = self.board.count('X')
        ocount = self.board.count('O')
        win = lambda xo: xo * len([rule for rule in self.WIN_RULES if (lambda b: b[rule[0]] == b[rule[1]] == b[rule[2]] == xo)(self.board)])
        xo_wins = win('X') + win('O')
        self.game_status = ('Draw' if xcount + ocount == len(self.board) else 'Game not finished') if len(
            xo_wins) == 0 else str(xo_wins) + ' wins'
        return self.game_status

    def handle_easy_ai(self, player):
        cell = random.randint(0, 8)
        while self.check_if_occupied(cell):
            cell = random.randint(0, 8)
        self.board[cell] = player.turn
        print('Making move level "easy"')
        self.show_board()

    def calculate_free_cells(self):
        return [i for i, j in enumerate(self.board) if j == " "]


    def handle_hard_ai(self, player):
        cell = self.minimax(self.board, player)
        self.board[cell] = player.turn


    def one_step_to_win(self, turn):
        ai_positions = [i for i, j in enumerate(self.board) if j == turn]
        cells = [set(rule) - set(ai_positions) for rule in self.WIN_RULES]
        cell = list(group for group in cells if len(group) == 1 and group.intersection(self.calculate_free_cells()))
        if cell:
            return cell.pop().pop()
        return False

    def handle_medium_ai(self, player):
        if self.one_step_to_win(player.turn):
            self.board[self.one_step_to_win(player.turn)] = player.turn
        elif self.one_step_to_win(player.opponent_turn):
            self.board[self.one_step_to_win(player.opponent_turn)] = player.turn
        else:
            cell = random.randint(0, 8)
            while self.check_if_occupied(cell):
                cell = random.randint(0, 8)
            self.board[cell] = player.turn
        print('Making move level "medium"')
        self.show_board()


    def handle_user_move(self, player):
        cell = self.input_move('Enter the coordinates: ')
        while self.check_if_occupied(cell):
            cell = self.input_move('This cell is occupied! Choose another one!\n')
        self.board[cell] = player.turn
        self.show_board()

    def handle_player_status(self, player):
        """Check if player user or ai"""
        if self.current_player.status == 'easy':
            return self.handle_easy_ai(player)
        elif self.current_player.status == 'medium':
            return self.handle_medium_ai(player)
    #попробовать сделать словарь

    def check_if_occupied(self, cell):
        while self.board[cell] != ' ':
            return True

    def input_move(self, msg=''):
        move = input(msg)
        while not re.match('[1-3] [1-3]$', move):
            move = input(('Coordinates should be from 1 to 3!' if move.replace(' ', '').isnumeric()
                          else 'You should enter numbers!') + '\n' + msg)
        return (int(move.split()[0]) - 1) * 3 + int(move.split()[1]) - 1

    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self._players)

    def input_handler(self):
        initial_input = input('Input command: ').split(' ')
        if initial_input[0] == 'exit':
            self.game_status = 'Finished'
            return
        while len(initial_input) != 3:
            print('Bad parameters!')
            self.input_handler()
            return
        command, player1, player2 = initial_input

        if command == 'start':
            self.board = list(' ' * 9)
            self.show_board()
            self.game_status = 'Game not finished'
            first_player.status = player1
            second_player.status = player2
            players = (first_player, second_player)
            self._players = cycle(players)

    def run(self):
        if self.game_status == 'Finished':
            return
        while self.game_status != 'Finished':
            self.input_handler()
            while self.game_status == 'Game not finished':
                self.toggle_player()
                self.handle_player_status(self.current_player)
                self.update_status()
            if self.game_status != 'Finished':
                print(self.game_status)


if __name__ == '__main__':
    game = Ticktacktoe()
    game.run()
