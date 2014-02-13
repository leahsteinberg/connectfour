#!/usr/bin/env python
SIZE = 7
player_dict = {'EMPTY': 0, 'BLUE': -1, 'RED': 1}
EMPTY = 0
BLUE = -1
RED = 1
board = [[EMPTY]*SIZE for i in range(0, SIZE)]
whose_turn = 'BLUE'

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


def get_input():
	while(True):
		try:
			column = int(raw_input("player " + whose_turn + "'s turn: "))
			if column >= 0 and column <= 6:
				row = 0
				for index in range(0, SIZE):
					row = index
					if board[column][index] != EMPTY:
						row = index - 1
						#if column already full
						if (index-1) < 0:
							raise ValueError
						else:
							break
				# done gathering info from this player
				return [column, row]
			else:
				raise ValueError
		except ValueError:
			print 'give me a different value.'
	

def turn():
	global whose_turn
	move = get_input()
	update_board(move)
	print pretty_print(board)
	if whose_turn == 'BLUE':
		whose_turn = 'RED'
	else:
		whose_turn = 'BLUE'


def update_board(move):
	board[move[0]][move[1]] = player_dict[whose_turn]




	#at the end of this, we switch whose turn it is



## input = check_input()
# if input == 0:
# raise exception


if __name__ == "__main__":
	while(True):
		turn()

	#print pretty_print(board)

	