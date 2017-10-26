# Gene Ressler, SWE, Google NYC
# generessler@google.com

def doesPairExist(arr, target):
	# Will track the complementary number
	# and its index
	pairs = {}
	for index, num in enumerate(arr):
		# if complement is in dict then there is
		# a pairing that sums up to target value
		if num in pairs:
			return True
		else:
			pairs[target - num] = index

	return False

# A DS that is like a set but not really
import random

class SetLike:
	def __init__(self):
		self.itemsDict = {}
		self.itemsList = []

	def insert(self, item):
		self.itemsList.append(item)
		self.itemsDict[item] = len(itemsList) - 1

	def remove(self, item):
		if item not in self.itemsDict:
			return "This element does not exist"
		
		index = self.itemsDict[item]
		last = self.itemsList[len(itemsList) - 1]
		# swap the last element with the item you want to remove
		self.itemsList[index], last = last, self.itemsList[index]
		# remove the element from the list
		self.itemsList.pop()
		# update index of last element now that it has moved places
		self.itemsDict[last] = index
		# remove the element from the dictionary
		self.itemsDict.pop('item')

	def getRandomElement(self):
		# generate a random index from list size
		r = random.randint(0, len(self.itemsList))
		return self.itemsList[r]


