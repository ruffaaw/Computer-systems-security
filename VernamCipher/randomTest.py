import math

def randomTest(input, n):
    ones = input.count('1') 
    zeroes = input.count('0')    
    s = abs(ones - zeroes)  
    p = math.erfc(float(s)/(math.sqrt(float(n)) * math.sqrt(2.0))) 
    success = ( p >= 0.01)  # success = true if p-value >= 0.01
    return success