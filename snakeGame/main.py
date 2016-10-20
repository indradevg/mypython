#!/usr/bin/python3.4 
# -*- coding: utf-8 -*-

import matrix
from charecter import *


(rows, col) = (20, 40)

game_matrix = matrix.Matrix(rows, col)
main_symbol = MainSymbol('>', vely=2, trace='#')

game_matrix.update_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

while True:
	game_matrix.print_matrix()
	
	
	direc = input("Which direction next (WASD)? ")
	direc=direc.upper()
	
	
	if direc == 'Q': break
	elif direc not in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
		continue
	
	game_matrix.update_matrix(main_symbol.x, main_symbol.y, main_symbol.trace)
	main_symbol.read_pos(direc)
	game_matrix.update_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)
	
	



