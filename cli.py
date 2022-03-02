from Chessboard import Chessboard
from Saver import Saver
from utilities import complex_number_2_chess_notation, chess_notation_2_complex_number
import os

check_move = {complex_number_2_chess_notation(i) + str(k) for i in range(1, 9) for k in range(1, 9)}


class Cli:
    def __init__(self):
        self.chessboard = Chessboard()
        self.saver = Saver(self.chessboard)

    def render_chessboard(self):
        print('  ', end=" ")
        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)) + "", end=" ")
        print(" ")

        if self.chessboard.queue:
            for i in range(8, 0, -1):
                print(i, end="  ")
                for k in range(1, 9):
                    if self.chessboard.chess_board[complex(k, i)]:
                        print(self.chessboard.chess_board[complex(k, i)], end=" ")
                    else:
                        print(".", end=" ")
                print(" " + str(i))
            print('  ', end=" ")
        else:
            for i in range(1, 9):
                print(i, end="  ")
                for k in range(1, 9):
                    if self.chessboard.chess_board[complex(k, i)]:
                        print(self.chessboard.chess_board[complex(k, i)], end=" ")
                    else:
                        print(".", end=" ")
                print(" " + str(i))
            print('  ', end=" ")

        for k in range(1, 9):
            print(complex_number_2_chess_notation(complex(k, 0)), end=" ")
        print("")

    def get_command(self):
        while True:
            input_command = input("Введите команду в шахмотной нотации: ")

            if input_command == "Ход назад":
                if self.chessboard.current_move < 3:
                    print("Вы не можете вернуться назад на такой ранней стадии игры")
                    continue
                self.saver.back_one_move()
                self.render_chessboard()
                continue

            input_command_chess = input_command.split('--')
            if len(input_command_chess) <= 1:
                print('Некорректная команда')
                continue

            first_position, second_position = input_command_chess[0], input_command_chess[1]

            if first_position not in check_move or second_position not in check_move:
                print("Некорректная команда")
                continue

            respond = self.chessboard.move(chess_notation_2_complex_number(first_position),
                                           chess_notation_2_complex_number(second_position))

            if respond[0]:
                os.system('cls')
                if respond[1] == 'Выберите желаемую фигуру':
                    #Дописать
                    pass

                self.saver.add((chess_notation_2_complex_number(first_position),
                                chess_notation_2_complex_number(second_position)))
                self.render_chessboard()

            print(respond[1])
            if respond[1].find('Игра завершена, ') != -1:
                break


if __name__ == "__main__":
    new_cli = Cli()
    new_cli.render_chessboard()
    new_cli.get_command()
