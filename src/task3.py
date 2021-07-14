'''
Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

Here are the rules for csRaindrop. If the input number:

has 3 as a factor, add "Pling" to the result.
has 5 as a factor, add "Plang" to the result.
has 7 as a factor, add "Plong" to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.
Examples:

csRaindrops(28) -> "Plong"
28 has 7 as a factor, but not 3 or 5.
csRaindrops(30) -> "PlingPlang"
30 has both 3 and 5 as factors, but not 7.
csRaindrops(34) -> "34"
34 is not factored by 3, 5, or 7
'''

def csRaindrops(number):
    num = []
    # Need individual if statements so the code can check each one. elif won't work.
    if number % 3 == 0:
        # Need to append to an empty list seeing as using return functions only passes 14/18 tests. The last 4 tests have plingplong for example, so appending strings like these into a list is necessary
        num.append('Pling')
    if number % 5 == 0:
        num.append('Plang')
    if number % 7 == 0:
        num.append('Plong')
    if len(num) == 0:
        return str(number)
    # All these if statements need the appended list they've created converted back into a string
    return ''.join(num)
