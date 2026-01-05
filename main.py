import pygame
import numpy as np
from sys import exit

from Tools import GraphEngine as graph


class Main:

	def __init__(self):

		super().__init__()

		pygame.init()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		pygame.display.set_caption("Linear Algebra Exercise")
		self.clock = pygame.time.Clock()

		self.screen_w, self.screen_h = self.screen.get_size()

		# setting the graph axis
		self.graph = graph((self.screen_w/2, self.screen_h/2))



		# Test Case
		self.graph.grid_x = 2
		self.graph.grid_y = 2
		circ_center = (-4,4)
		self.show_circ = self.graph.show_point(circ_center)


	def main_loop(self):

		while True:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:

					pygame.quit()
					exit()





			

			# setting the background color
			self.screen.fill((0,0,0))



			# showing the graph on screen
			self.graph.show_graph(self.screen)


			# Test Case
			pygame.draw.circle(self.screen, (255,0,0), self.show_circ, 10)


			

			pygame.display.flip()
			self.clock.tick(60)


if __name__ == '__main__':

	Main().main_loop()




