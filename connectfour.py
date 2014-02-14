#!/usr/bin/env python

class Game:
	

	status = {'EMPTY': 0, 'BLUE': -1, 'RED': 1}

	def __init__(self, size=7, current_player='BLUE'):
		self.SIZE = size
		self.board = [[self.status['EMPTY']]*self.SIZE for i in range(0, self.SIZE)]
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
		''' move is a list that is col, row
		'''
		self.board[move[0]][move[1]] = self.status[self.current_player]
		

def pretty_print(game):
	''' translates the logical game state into a string
	returns a string
	'''
	board_string = ''
	for cols in range(0, game.SIZE):
		board_string += str(cols) + ' '
	board_string += '\n'
	
	for i in range(0, game.SIZE): # rows
		for column in game.board: # columns
			if column[i] == game.status['EMPTY']:
				board_string+='_'
			if column[i] == game.status['BLUE']:
				board_string+='X'
			if column[i] == game.status['RED']:
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
			try:
				return check_move(game, column)
			except ValueError as e:
				print str(e)
		except ValueError:
			print 'give me a different value.'


def check_move(game, column):
	# if the move fits in the board
	if column >= 0 and column < game.SIZE:
		# we are looking for the correct row
		row = 0
		# loop down the column looking for last empty space
		for index in range(0, game.SIZE):
			row = index
			# if we found an already-filled square
			if game.board[column][index] != game.status['EMPTY']:
				# set the row to the one before the full one
				row = index - 1
				#if column already full
				if (index-1) < 0:
					raise ValueError('This column is full.')
				else:
					# found a good move
					return [column, row]	
			#column was empty
			
		return [column, row]
	# the given number didn't fit on the board at all
	else:
		raise ValueError('Number is off the board.')

	






## input = check_input()
# if input == 0:
# raise exception


if __name__ == "__main__":
	game = Game()
	game.run_game()
	
	#print pretty_print(board)

	