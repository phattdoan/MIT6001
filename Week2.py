# PS2
# -----------------------------------------------------------------------------
# check if the minimum payment will payoff of the credit card in the pre-determined length
def monthlyUnpaidBalance(b, p, i, m):
    for l in range(0, m):
        b = (b - p) + (i / 12) * (b -p)
    return b <= 0

def minimumPayment(balance, annualInterestRate, length):
    for minimum in range(0, balance):
        if monthlyUnpaidBalance(balance, minimum, annualInterestRate, length) == True:
            break
    return minimum

balance = 3926
annualInterestRate = 0.2
length = 12
print("You would need to make a minimum payment of $%8.2f to payoff a balance of $%8.2f in %8.2f months" % (minimumPayment(balance, annualInterestRate, length), balance, length))

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