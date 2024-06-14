from generateRandomPrimeInteger import generateRandomPrime
from BBS import generateBits
from generateToBinary import word_to_ascii
from generateToChar import binary_to_ascii
from encrypt import encrypt
from decrypt import decrypt
from readFile import read_file
from randomTest import randomTest

message=read_file('./textFile.txt')
print(message)
key=generateBits(generateRandomPrime(),len(message)*8)
print(key)
cryptogram=encrypt(word_to_ascii(message), key)
print(cryptogram)
print(binary_to_ascii(decrypt(cryptogram, key)))
print(randomTest(cryptogram, len(cryptogram)))