import pygame
import numpy as np

class GraphEngine:
	""" 
	this class's purpose is rendering core graph mechanics of this program
	
	"""

	def __init__(self, axis : tuple[int | float]) -> None:
		"""
		param: axis - is center of the graph
		"""

		super().__init__() # initalizes the class better

		self.axis = axis

		# how many spaces between the grids, customizable
		self.shift = 50

		# the block size of the graph, customizable
		self.block_y = 1
		self.block_x = 1

	def show_point(self, point : tuple[int | float]) -> tuple[int | float]:
		"""
		location given based on this equation (shift * (x / block_x), shift * (x / block_y))
		use that if you want to get a specific location on graph
		PURPOSE: gives you the location of the point on screen, converts the graph location to pygame screen location
		
		param: point -> a location on the graph 
		return: graph point location on screen
		
		"""

		return ((self.shift * (point[0] / self.block_x)) + self.axis[0], self.axis[1] - (self.shift * (point[1] / self.block_y)))

	def normal_point(self, point : tuple[int | float]) -> tuple[int | float]:
		"""
		PURPOSE, make it possible to using the graph location system with pygames default block size (pixel)

		param: point -> the point according to the graph
		return: convert point into default pygame screen location
		"""
		
		return (point[0] + self.axis[0], self.axis[1] - point[1])

	def show_object(self, points):

		pass

	def show_graph(self, surface, 
				   axis_colour : tuple[int] = (255,255,255), 
				   grid_colour : tuple[int] = (100, 100, 100),
				   point_colour : tuple[int] = (255,0,0)
				   )-> None:
		"""
		PURPOSE: Shows the graph table on the screen
		
		param: axis_colour -> color of the axis_lines (x,y)
		param: grid_colour -> color of the grid lines
		"""

		y_axis_start = (0, self.axis[1])
		y_axis_end = (0, -self.axis[1])
		x_axis_start = (-self.axis[0], 0)
		x_axis_end = (self.axis[0], 0)

		for grid_x in range(0, int(x_axis_end[0]), self.shift):

			# drawing vertical grid line for left side
			pygame.draw.line(surface, grid_colour, self.normal_point((-grid_x, y_axis_start[1])), self.normal_point((-grid_x, y_axis_end[1])), 1)
			# drawing vertical grid line for right side
			pygame.draw.line(surface, grid_colour, self.normal_point((grid_x, y_axis_start[1])), self.normal_point((grid_x, y_axis_end[1])), 1)

			# drawing horizontal grid line for the bottom side
			pygame.draw.line(surface, grid_colour, self.normal_point((x_axis_start[0], -grid_x)), self.normal_point((x_axis_end[0], -grid_x)), 1)
			# drawing horizontal grid line for the top side
			pygame.draw.line(surface, grid_colour, self.normal_point((x_axis_start[0], grid_x)), self.normal_point((x_axis_end[0], grid_x)), 1)

			for grid_y in range(0,int(y_axis_start[1]), self.shift):

				# point for the topright side of the graph
				point_topright = (grid_x, grid_y)
				# point for the bottomright side of the graph
				point_bottomright = (grid_x, -grid_y)
				# point for the topleft side of the graph
				point_topleft = (-grid_x, grid_y)
				# point for the bottomleft side of the graph
				point_bottomleft = (-grid_x, -grid_y)

				topright_rect = pygame.Rect(0,0,10,10)
				topright_rect.center = self.normal_point(point_topright)

				bottomright_rect = pygame.Rect(0,0,10,10)
				bottomright_rect.center = self.normal_point(point_bottomright)

				topleft_rect = pygame.Rect(0,0,10,10)
				topleft_rect.center = self.normal_point(point_topleft)

				bottomleft_rect = pygame.Rect(0,0, 10,10)
				bottomleft_rect.center = self.normal_point(point_bottomleft)

				if abs(mouse_pos[0]-topright_rect.centerx) <= (self.block_x/2) and abs(mouse_pos[1]-topright_rect.centery) <= (self.block_y/2):
					
					pygame.draw.rect(surface, (point_colour), topright_rect, 0, 10)
					
				elif abs(mouse_pos[0]-topright_rect.centerx)<= (self.block_x/2) and abs(mouse_pos[1]-topright_rect.centery)<= (self.block_y/2):
					
					pygame.draw.rect(surface, (point_colour), bottomright_rect, 0, 10)
					
				elif abs(mouse_pos[0]-topright_rect.centerx)<= (self.block_x/2) and abs(mouse_pos[1]-topright_rect.centery)<= (self.block_y/2):
					
					pygame.draw.rect(surface, (point_colour), topleft_rect, 0, 10)
					
				elif abs(mouse_pos[0]-topright_rect.centerx)<= (self.block_x/2) and abs(mouse_pos[1]-topright_rect.centery)<= (self.block_y/2):
					
					pygame.draw.rect(surface, (point_colour), bottomleft_rect, 0, 10)


		
		# drawing the y axis
		pygame.draw.line(surface, axis_colour, self.normal_point(y_axis_start), self.normal_point(y_axis_end), 2)

		# drawing the x axis
		pygame.draw.line(surface, axis_colour, self.normal_point(x_axis_start), self.normal_point(x_axis_end), 2)
		

		