import pygame
import numpy as np

from graph_engine.GraphEngine import normal_point

class SideBar:

	def __init__(self):

		super().__init__()

		self.symbol_surf = pygame.Surface((60,60))
		self.symbol_surf.fill((120,120,255))
		self.symbol_rect = self.symbol_surf.get_rect(topright = normal_point(400, 400))
		
		

	
	def symbol(self, surface, ):
		pass

	def draw_symbol(self, surface):

		surface.blit(self.symbol_surf, self.symbol_rect)
		




































