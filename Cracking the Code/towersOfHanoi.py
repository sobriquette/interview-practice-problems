class SolutionCTCI:
	class Tower:
		def __init__(self, disks, idx):
			self.disks = []
			self.idx = idx

		def get_index(self):
			return self.idx

		def add_disk(d):
			if disks and disks[len(disks) - 1] <= d:
				return ("Error placing disk: ".format(d))
			else:
				disks.append(d)

		def move_top_to(tower):
			top = self.disks.pop()
			tower.add_disk(top)

		def move_disks(n, dest, aux):
			if n > 0:
				self.move_disks(n - 1, aux, dest)
				self.move_top_to(dest)
				aux.move_disks(n - 1, dest, self.disks)

	def hanoi(self, n):
		n = int(input())
		towers = []

		for i in range(n):
			towers[i] = Tower(i)

		towers[0].move_disks(n, towers[2], towers[1])

class SolutionG4G:
	def tower_hanoi(self, n, source, dest, aux):
		if n == 1:
			self.move_disk(source, dest)
		self.tower_hanoi(n - 1, source, aux, dest)
		self.move_disk(source, dest)
		self.tower_hanoi(n - 1, aux, dest, source)

	def move_disk(self, source, dest):
		top = source.pop()
		add_disk(top, dest)

	def add_disk(self, disk, dest):
		if dest and dest[len(dest) - 1] <= disk:
			return "Error placing disk"
		else:
			dest.append(disk)
	