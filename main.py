"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
	# Base case for recursion
	if x.decimal_val < 10 or y.decimal_val < 10:
		return BinaryNumber(x.decimal_val * y.decimal_val)

	# Ensure x and y are of equal length
	x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)

	n = max(len(x.binary_vec), len(y.binary_vec))
	if n == 1:
		return BinaryNumber(int(x.binary_vec[0]) * int(y.binary_vec[0]))

	n = max(len(x.binary_vec), len(y.binary_vec))
	m = n // 2

	
	xL, xR = split_number(x.binary_vec)
	yL, yR = split_number(y.binary_vec)

	
	p1 = subquadratic_multiply(xL, yL)  # xL * yL
	p2 = subquadratic_multiply(xR, yR)  # xR * yR

	xSum = BinaryNumber(xL.decimal_val + xR.decimal_val)
	ySum = BinaryNumber(yL.decimal_val + yR.decimal_val)
	p3 = subquadratic_multiply(xSum, ySum)  # (xL + xR) * (yL + yR)


	middle_term = p3.decimal_val - p1.decimal_val - p2.decimal_val
	result = (p1.decimal_val << (2 * m)) + (middle_term << m) + p2.decimal_val

	return BinaryNumber(result)

  



def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000


x = BinaryNumber(2)
y = BinaryNumber(2)
result = subquadratic_multiply(x, y)
print(result)

