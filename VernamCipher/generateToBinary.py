def word_to_ascii(word):
  binary_list = []
  for char in word:
    ascii_value = ord(char)  
    binary_value = bin(ascii_value)[2:].zfill(8)  
    binary_list.extend([int(bit) for bit in binary_value])
  return binary_list