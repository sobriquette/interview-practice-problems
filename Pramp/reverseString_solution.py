def sentence_reverse(sentence):
   mirror(sentence, start=0, end=len(sentence)-1)

   word_start = None
   spacers = (' ', '  ')

   for index, letter in enumerate(sentence):
      if letter in spacers:
          if word_start is not None:
                mirror(sentence, word_start, index-1)
                word_start = None
      elif index + 1 == len(sentence):
            if word_start is not None:
                mirror(sentence, word_start, index)
      else:
            if word_start is None:
                word_start = index
   return sentence


def mirror(item, start, end):
    while start < end:
      item[start], item[end] = item[end], item[start]
      start += 1
      end -= 1
    return item

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

for input, output in zip(inputs, outputs):
    result = sentence_reverse(input)
    print('{}\t{} == {}'.format(result == output, result, output))