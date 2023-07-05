import time
import pygame


class AnimSurface:
	
	def __init__(self, surf_path: str, extension: str, amount: int, timings, starting_num: int = 0):
		self.surfaces = [
			pygame.image.load(f'{surf_path}{num + starting_num}.{extension.lstrip(".")}') for num in range(amount)
		]
		self._frame = 0
		self.timings = timings
		self.start = time.time()
		if len(self.timings) < len(self.surfaces):
			raise AttributeError(
				f"Given insufficient length of timings: {len(self.timings)} to {len(self.surfaces)} frames")
	
	def scale(self, size):
		self.surfaces = [pygame.transform.scale(surf, size) for surf in self.surfaces]
	
	def scale_by(self, amount):
		self.surfaces = [pygame.transform.scale_by(surf, amount) for surf in self.surfaces]
	
	@property
	def frame(self):
		output = self.surfaces[self._frame]
		if time.time() - self.start > self.timings[self._frame]:
			self._frame += 1
			self.start = time.time()
		if self._frame > len(self.surfaces) - 1:
			self._frame = 0
		return output
	
	@frame.setter
	def frame(self, value):
		self._frame = value
		if self._frame > len(self.surfaces):
			self._frame = 0