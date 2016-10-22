class Direction():
	
	UP		=	'W'
	DOWN	=	'S'
	LEFT	=	'A'
	RIGHT	=	'D'
	
class MainSymbol():
	def __init__ (self, symbol, startX = 0, startY = 0, velx=1, vely=1, trace = "."):
		self.symbol = symbol
		
		self.x = startX
		self.y = startY
		
		self.velx = velx
		self.vely = vely
		
		self.trace = trace
		
	
	def read_pos(self, direction):
		if direction == Direction.DOWN:
			self.x += self.velx
		elif direction == Direction.UP:
			self.x -= self.velx
	
		
		elif direction == Direction.RIGHT:
			self.y += self.vely
		elif direction == Direction.LEFT:
			self.y -= self.vely
		
		
		
	

