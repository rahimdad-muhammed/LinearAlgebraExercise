import pygame
import numpy as np

class GraphEngine:

	def __init__(self, axis : tuple[int | float]) -> None:

		super().__init__()

		self.axis = axis

		
		self.shift = 50
		
		self.grid_y = 1
		self.grid_x = 1

	def show_point(self, point : tuple[int | float]) -> tuple[int | float]:

		return ((self.shift * (point[0] / self.grid_x)) + self.axis[0], self.axis[1] - (self.shift * (point[1] / self.grid_y)))

	def normal_point(self, point : tuple[int | float]) -> tuple[int | float]:
		
		return (point[0] + self.axis[0], self.axis[1] - point[1])

	def show_object(self, points):

		pass

	def show_graph(self, surface, 
				   axis_colour : tuple[int] = (255,255,255), 
				   grid_colour : tuple[int] = (100, 100, 100)) -> None:

		y_axis_start = (0, self.axis[1])
		y_axis_end = (0, -self.axis[1])
		x_axis_start = (-self.axis[0], 0)
		x_axis_end = (self.axis[0], 0)

		for grid in range(0, int(x_axis_end[0]), self.shift):

			# drawing vertical grid line for left side
			pygame.draw.line(surface, grid_colour, self.normal_point((-grid, y_axis_start[1])), self.normal_point((-grid, y_axis_end[1])), 1)
			# drawing vertical grid line for right side
			pygame.draw.line(surface, grid_colour, self.normal_point((grid, y_axis_start[1])), self.normal_point((grid, y_axis_end[1])), 1)

			# drawing horizontal grid line for the bottom side
			pygame.draw.line(surface, grid_colour, self.normal_point((x_axis_start[0], -grid)), self.normal_point((x_axis_end[0], -grid)), 1)
			# drawing horizontal grid line for the top side
			pygame.draw.line(surface, grid_colour, self.normal_point((x_axis_start[0], grid)), self.normal_point((x_axis_end[0], grid)), 1)

		# drawing the y axis
		pygame.draw.line(surface, axis_colour, self.normal_point(y_axis_start), self.normal_point(y_axis_end), 2)

		# drawing the x axis
		pygame.draw.line(surface, axis_colour, self.normal_point(x_axis_start), self.normal_point(x_axis_end), 2)
		

		