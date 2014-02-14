#!/usr/bin/env python

class Game:
	
	EMPTY = 0
	BLUE = -1
	RED = 1
	player_dict = {'EMPTY': 0, 'BLUE': -1, 'RED': 1}

	def __init__(self, size=7, current_player='BLUE'):
		self.SIZE = size
		self.board = [[self.EMPTY]*self.SIZE for i in range(0, self.SIZE)]
		self.current_player = current_player


	def run_game(self):
		while(True):
			self.turn()
			# TODO: is the game over?

	def turn(self):
		'''
		game loop: get input from player and update board
		and current player
		'''
		self.current_player
		move = get_input(self)
		self.update_board(move)
		print pretty_print(self)
		# change the current player
		if self.current_player == 'BLUE':
			self.current_player = 'RED'
		else:
			self.current_player = 'BLUE'
	
	def update_board(self, move):
		self.board[move[0]][move[1]] = self.player_dict[self.current_player]
		

def pretty_print(game):
	''' translates the logical game state into a string
	returns a string
	'''
	# TODO, use game.SIZE to determine num columns
	board_string = '0 1 2 3 4 5 6\n'
	for i in range(0, game.SIZE):
		for column in game.board:
			if column[i] == game.EMPTY:
				board_string+='_'
			if column[i] == game.BLUE:
				board_string+='X'
			if column[i] == game.RED:
				board_string+='O'
			board_string+=' '
		board_string+='\n'
	return board_string


def get_input(game):
	''' Keep asking current playing for input until
	valid input is provided
	'''
	while(True):
		try:
			column = int(raw_input("player " + game.current_player + "'s turn: "))
			# TODO: fix the hard-coded 0-6
			if column >= 0 and column <= 6:
				row = 0
				for index in range(0, game.SIZE):
					row = index
					if game.board[column][index] != game.EMPTY:
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
	






## input = check_input()
# if input == 0:
# raise exception


if __name__ == "__main__":
	game = Game()
	game.run_game()
	
	#print pretty_print(board)

	