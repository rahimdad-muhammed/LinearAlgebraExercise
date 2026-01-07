import pygame
import numpy as np
from sys import exit

from Tools import GraphEngine as graph
from Tools import SideBar as side_bar


class Main:

	def __init__(self) -> None:

		super().__init__()

		pygame.init()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # setting screen to fullsize
		pygame.display.set_caption("Linear Algebra Exercise") # title
		self.clock = pygame.time.Clock() # preparing the clock function for frame rate

		self.screen_w, self.screen_h = self.screen.get_size() # getting the size of the screen (width, height)

		# setting the graph axis
		self.graph = graph((self.screen_w/2, self.screen_h/2))



		# Test Case
		self.graph.block_x = 2
		self.graph.block_y = 2
		circ_center = (-4,4)
		self.show_circ = self.graph.show_point(circ_center)



	def main_loop(self) -> None:
		"""
		PURPOSE: Runs the whole program, starter of this program
		"""

		# game loop
		while True:

			# user events
			for event in pygame.event.get():

				# finish the program
				if event.type == pygame.QUIT:

					pygame.quit()
					exit()





			

			# setting the background color
			self.screen.fill((0,0,0))



			# showing the graph on screen
			mouse_poss = pygame.mouse.get_pos()
			self.graph.show_graph(self.screen, mouse_pos = mouse_poss)


			# Test Case
			pygame.draw.circle(self.screen, (255,0,0), self.show_circ, 10)


			
			

			# update the display
			pygame.display.flip()
			# set frame rate to 60 fps
			self.clock.tick(60)

# run the program only and only when this file runned directly
if __name__ == '__main__':

	Main().main_loop()



# Thinking Space




























