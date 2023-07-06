import pygame

from Window import *
from AnimSurface import AnimSurface
import random

WIN_SIZE = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(WIN_SIZE, pygame.NOFRAME)
make_window_on_top()
make_window_background_invisible((0, 0, 0))
clock = pygame.Clock()


class CuteCat(AnimSurface):

	def __init__(self):
		super().__init__('.\\assets\\cat', '.png', 8, (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.25), starting_num=1,
		                 subsurface=pygame.Rect(9 * 5, 47 * 5, 31 * 5, 17 * 5))
		self.frame = random.randint(0, 7)
		self.SCALE = 5
		self.scale_by(self.SCALE)
		self.pos = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
		self.size = self.subsurface.size
	
	def move(self, dpos):
		self.pos.x += dpos[0]
		self.pos.y += dpos[1]
		
		self.pos.x = pygame.math.clamp(self.pos.x, 0, screen.get_width()-self.size[0])
		self.pos.y = pygame.math.clamp(self.pos.y, 0, screen.get_height()-self.size[1])
		

class Bed:
	
	def __init__(self):
		self.SCALE = 5
		self.img = pygame.transform.flip(pygame.transform.scale_by(pygame.image.load('.\\assets\\bed.png'), self.SCALE), random.choice((True, False)), False)
		self.pos = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
		self.size = self.img.get_size()
	
	def move(self, dpos):
		self.pos.x += dpos[0]
		self.pos.y += dpos[1]
		
		self.pos.x = pygame.math.clamp(self.pos.x, 0, screen.get_width() - self.size[0])
		self.pos.y = pygame.math.clamp(self.pos.y, 0, screen.get_height() - self.size[1])
	
	def flip(self, x, y):
		self.img = pygame.transform.flip(self.img, x, y)


CuteCats = [CuteCat() for _ in range(5)]
Beds = [Bed() for _ in range(3)]

while True:
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEMOTION:
			if event.buttons[0]:
				for Cute_cat in CuteCats:
					hitbox = pygame.Rect((Cute_cat.pos.x, Cute_cat.pos.y), Cute_cat.size)
					if hitbox.collidepoint(event.pos):
						Cute_cat.move(event.rel)
				for bed in Beds:
					hitbox = bed.img.get_rect(topleft=bed.pos)
					if hitbox.collidepoint(event.pos):
						bed.move(event.rel)
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 3:
				for bed in Beds:
					hitbox = bed.img.get_rect(topleft=bed.pos)
					if hitbox.collidepoint(event.pos):
						bed.flip(True, False)
						
	
	for Cute_cat in CuteCats:
		Cute_cat.pos.y = pygame.math.clamp(Cute_cat.pos.y, 0, screen.get_height()-Cute_cat.size[1])
		pos = (Cute_cat.pos.x, Cute_cat.pos.y-Cute_cat.frame.get_height()+Cute_cat.size[1])
		screen.blit(Cute_cat.frame, pos)
	for bed in Beds:
		screen.blit(bed.img, bed.pos)
	pygame.display.flip()
	clock.tick(60)
