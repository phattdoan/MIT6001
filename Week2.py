# PS2
# -----------------------------------------------------------------------------
def monthlyUnpaidBalance(b, p, i, m):
    for l in range (1, m):
        b = b - p
        b = b + i / 12 * b
    return b == 0

def minimumPayment(balance, annualInterestRate, length):
    for minimum in range (0, balance):



balance = 10000
annualInterestRate = 18
length = 12




# PS1b
# -----------------------------------------------------------------------------
def countWord(input, word):
    word_count = 0
    w_position = 0
    for i in input:
        if i == word[w_position]:
            w_position += 1
            if w_position == len(word):
                word_count += 1
                w_position = 0
        else:
            w_position = 0
    return word_count

test = 'abobsbobde'
word = 'bobs'
print(countWord(test, word))


# PS1a
# -----------------------------------------------------------------------------
def isVowel(char):
    vowel = ['a', 'e', 'i', 'o', 'u']
    ans = False
    for v in vowel:
        if char == v:
            ans = True
    return ans

def countVowel(s):
    count = 0
    for char in s:
        if isVowel(char) == True:
            count = count + 1
    return count

# Polysum
# -----------------------------------------------------------------------------
import numpy as np
def polysum(n, s):
    area = (0.25 * n * (s*s))/(np.tan(np.pi/n))
    perimeter = n * s
    return round(area + (perimeter*perimeter), 4)

# Vowel
# -----------------------------------------------------------------------------
def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = False
    for v in vowel:
        if char == v:
            ans = True
    return ans