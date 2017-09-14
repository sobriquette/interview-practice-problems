# The "Sentence Reverse" Problem

# You are given an array of characters arr, which consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.
# How can you most efficiently reverse the order of the words in the array?
# Explain and implement your solution. Lastly, analyze its time and space complexities.

# For example:
# [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

# would turn into:
# [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]

# Input: ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

chars = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
spaces = ['', ' ', '  ']

inputs = [
    ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'],
    [],
    [' ', ' ', ' ', ' ', ' '],
    ['p', 'a', 'n', 'd', 'a', 's'],
    ['t', 'r', 'e', 'e', ' ', ' ', ' ', 'p', 'a', 'n', 'd', 'a']
]

outputs = [
    ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'e', 'r', 'f', 'e', 'c', 't'],
    [],
    [' ', ' ', ' ', ' ', ' '],
    ['p', 'a', 'n', 'd', 'a', 's'],
    ['p', 'a', 'n', 'd', 'a', ' ', ' ', ' ', 't', 'r', 'e', 'e']
]

class Stack:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      return self.items == []

   def push(self, item):
      self.items.append(item)

   def pop(self):
      return self.items.pop()

   def peek(self):
      return self.items[len(self.items) - 1]

   def size(self):
      return len(self.items)

def buildWordStack(chars):
   # push characters into a stack
   wordStack = Stack()

   for i in chars:
      wordStack.push(i)

   return wordStack

def reverseWordStack(wordStack):
   reversedWordStack = []
   index = 0

   while not wordStack.isEmpty():
      c = wordStack.pop()
      if c in spaces:
         # a space marks the end of the word
         # so append the space to the end of the reversed list
         # and set the last index of the list as the new insertion point
         # for chars in the next word
         reversedWordStack.append(c)
         index = len(reversedWordStack)
      else:
         # insert char into beginning of word
         # to reverse order in stack
         reversedWordStack.insert(index, c)

   return reversedWordStack

if __name__ == "__main__":
   # Test original problem input
   print(reverseWordStack(buildWordStack(chars)))
   
   # Test series of different inputs
   for i, o in zip(inputs, outputs):
    result = reverseWordStack(buildWordStack(i))
    print('{}\t{} == {}'.format(result == o, result, o))








