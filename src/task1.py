"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0
Notes:

The input integer will not be negative.
"""

'''
This version runs too slow. Only passed 2/5 tests due to a runtime error
'''
# def csReverseIntegerBits(n):
#     # Converting integer to binary
#     binint = bin(n)
#     # Have to remove 0b from binary
#     stripped_binint = binint.strip("0b")
#     # Reversing binint with index slicing
#     r_binint = stripped_binint[::-1]
#     # Converting from binary back to an integer
#     return int(r_binint, 2)

def csReverseIntegerBits(n):
    # This converts to the input, n, only AFTER the third place, automatically removing the 
    binint = bin(n)[2:]
    r_binint = binint[::-1]
    # Second argument, 2, is 0 indexed, thus it's converting the bin to an integer by 3 decimal places. The default is 10.
    return int(r_binint, 2)
