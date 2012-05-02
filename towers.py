#!/usr/bin/python
class Towers:
	"""A class for solving the Towers of Hanoi challenge"""

	def __init__(self, n):
		"""Initialize this Towers solver and stack n rings on tower a"""
		self.b, self.c = [], []
		self.a = range(n, 0, -1)
		self.n = n

	def solve(self):
		"""Solve this instance of Towers, and return the generator"""
		return self.move("a", "c", "b", self.n)

	def move(self, src, dest, spare, n):
		"""Move n rings from the src tower to the dest tower, yielding each step"""
		if self.__dict__[src]:
			if n == 1:
				ring = self.__dict__[src].pop()
				self.__dict__[dest].append(ring)
				yield str(ring) + " - " + dest.upper()
			else:
				# Move all but biggest to spare tower
				for s in self.move(src, spare, dest, n - 1):
					yield s
				# Move biggest to target tower
				yield self.move(src, dest, spare, 1).next()
				# Move all but the biggest from the spare onto destination
				for s in self.move(spare, dest, src, n - 1):
					yield s


if __name__ == "__main__":
	n = int(raw_input())
	towers = Towers(n)
	for step in towers.solve():
		print step
