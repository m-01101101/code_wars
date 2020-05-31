"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. 
And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

(Use the English alphabet with 26 letters!)
"""


def find_missing_letter(chars: list) -> str:
    alphabet = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
    alphabet = [a.upper() if chars[0].isupper()
                else a for a in alphabet.split(', ')]
    # in case chars not sorted and has duplicates
    input = list(sorted(set(chars)))
    return [a for a, b in zip(alphabet[alphabet.index(input[0]):], input) if a != b][0]


# The ord() function returns an integer representing the Unicode character.
# ord('5')  # 53
# ord('A')  # 65
def _find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
