from os import system as sys
class Matrix():
	def __init__ (self, rows, columns, default_chaterter = ' '):
		self.rows = rows
		self.columns = columns
		self.grid = [ [default_chaterter]*columns for _ in range(rows) ]
		
	def print_matrix(self):
		sys('clear')
		for row in self.grid:
			print ("".join(row))
				
	
	def update_matrix(self, row_pos, col_pos, upd_char):
		if 0 <= row_pos < self.rows:
			if 0 <= col_pos < self.columns:
				self.grid[row_pos][col_pos] = upd_char
				return
		raise IndexError("Out of Index value")
			
		
