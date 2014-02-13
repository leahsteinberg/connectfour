#!/usr/bin/env python
SIZE = 7
EMPTY = 0
BLUE = 1
RED = 2
board = [[EMPTY]*SIZE for i in range(0, SIZE)]


def pretty_print(board):
	board_string = '0 1 2 3 4 5 6\n'
	for i in range(0, SIZE):
		for column in board:
			if column[i] == EMPTY:
				board_string+='_'
			if column[i] == BLUE:
				board_string+='X'
			if column[i] == RED:
				board_string+='O'
			board_string+=' '
		board_string+='\n'
	return board_string
	





if __name__ == "__main__":
	print pretty_print(board)

	