def encrypt(message, key):
  cryptogram=[]
  for i,j in zip(message, key):
    cryptogram.append((i+j)%2)
  return cryptogram