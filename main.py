from Window import *
from AnimSurface import AnimSurface
import random

WIN_SIZE = get_free_area()
screen = pygame.display.set_mode(WIN_SIZE, pygame.NOFRAME)
make_window_on_top()
make_window_background_invisible((0, 0, 0))
clock = pygame.Clock()


class CuteCat(AnimSurface):

	def __init__(self):
		super().__init__('.\\cats\\cat', '.png', 8, (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.25), starting_num=1)
		self.frame = random.randint(0, 7)
		self.SCALE = 5
		self.scale_by(self.SCALE)
		self.pos = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
		self.size = (31 * self.SCALE, 17 * self.SCALE)


CuteCats = [CuteCat() for i in range(5)]


while True:
	screen.fill((0, 0, 0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEMOTION:
			if event.buttons[0]:
				for Cute_cat in CuteCats:
					hitbox = pygame.Rect((Cute_cat.pos.x-Cute_cat.size[0]+45, Cute_cat.pos.y), Cute_cat.size)
					if hitbox.collidepoint(event.pos):
						Cute_cat.pos += pygame.Vector2(event.rel)
	
	for Cute_cat in CuteCats:
		Cute_cat.pos.y = pygame.math.clamp(Cute_cat.pos.y, 0, screen.get_height()-Cute_cat.size[1])
		pos = (Cute_cat.pos.x-Cute_cat.size[0], Cute_cat.pos.y-Cute_cat.frame.get_height()+Cute_cat.size[1])
		screen.blit(Cute_cat.frame, pos)
	pygame.display.flip()
	clock.tick(60)
