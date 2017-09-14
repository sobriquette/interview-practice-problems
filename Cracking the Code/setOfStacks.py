# Implement a data structure that will start a new stack 
# when the previous one reaches a threshold.

class setOfStacks:
	def __init__(self, maxSize):
		self.stackList = [[]]
		self.maxSize = maxSize

	def getLastStack(self):
		if len(self.stackList) == 0:
			return None
		return self.stackList[len(self.stackList) - 1]

	def getLastStackSize(self):
		return len(self.getLastStack())

	def push(self, item):
		if self.getLastStackSize() >= self.maxSize:
			self.stackList.append([item])
		else:
			self.getLastStack().append(item)

	def pop(self):
		if self.getLastStackSize() <= 0:
			self.stackList.pop()

		return self.getLastStack().pop()

	def popAt(self, index):
		# swap value to be popped with next val
		# until it is the last in stackList
		self.stackList[index][self.maxSize - 1], self.stackList[index + 1][0] = \
		self.stackList[index + 1][0], self.stackList[index][self.maxSize - 1]
		for s in range(index + 1, len(self.stackList) - 1):
			for j in range(1, len(self.stackList[s])):
				self.stackList[s][j-1], self.stackList[s][j] = self.stackList[s][j], self.stackList[s][j-1]
			
			self.stackList[s][self.maxSize - 1], self.stackList[s + 1][0] = \
			self.stackList[s + 1][0], self.stackList[s][self.maxSize - 1]

		return self.getLastStack().pop()

if __name__=="__main__":
	mySetOfStacks = setOfStacks(3)
	mySetOfStacks.getLastStack()
	mySetOfStacks.getLastStackSize()
	mySetOfStacks.push(1)
	mySetOfStacks.push(3)
	mySetOfStacks.push(4)
	mySetOfStacks.push(10)
	mySetOfStacks.push(0)
	mySetOfStacks.push(15)
	mySetOfStacks.push(16)
	mySetOfStacks.push(20)
	mySetOfStacks.push(36)
	mySetOfStacks.push(6)
	mySetOfStacks.push(14)
	print(mySetOfStacks.stackList)
	mySetOfStacks.popAt(1)
	print(mySetOfStacks.stackList)
