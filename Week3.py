# semordnilap
# ------------------------------------------------------------------------------
def semordnilap(str1, str2):
    c1 = 0
    c2 = len(str2)
    answer = True
    while c1 <= (len(str1)-1):
        if str1[c1:c1+1] != str2[c2-1:c2]:
            answer = False
            break
        else:
            c1 += 1
            c2 -= 1
    return answer

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1 or str1 == '' or str2 == '':
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    if len(str1) != len(str2):
        return False

    return semordnilap(str1, str2)

# semordnilapRecur
# ------------------------------------------------------------------------------
def semordnilapRecur(str1, str2):
    c1 = 0
    c2 = len(str2)
    answer = True
    while c1 <= (len(str1)-1):
        if str1[c1:c1+1] != str2[c2-1:c2]:
            answer = False
            break
        else:
            c1 += 1
            c2 -= 1
    return answer

print(semordnilapWrapper('abcdefgh','hgfedcba'))

# isIn
# ------------------------------------------------------------------------------
def isIn(char, aStr):
    if aStr == '':
        return False

    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return aStr == char

    # Base case: See if the character in the middle of aStr equals the
    #   test character
    midIndex = int(len(aStr) / 2)
    midChar = aStr[midIndex]
    if char == midChar:
        # We found the character!
        return True

    # Recursive case: If the test character is smaller than the middle
    #  character, recursively search on the first half of aStr
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # Otherwise the test character is larger than the middle character,
    #  so recursively search on the last half of aStr
    else:
        return isIn(char, aStr[midIndex + 1:])

#print(isIn('c', 'phat'))

# lenRecur
# ------------------------------------------------------------------------------
def lenRecur(string):
    if string == "":
        return 0

    return 1 + lenRecur(string[1:])

#print(lenRecur('hellos'))

# lenIter
# ------------------------------------------------------------------------------
def lenIter(string):
    ans = 0
    for s in string:
        ans += 1
    return ans

#print(lenIter('hellos'))

# Palindrome
# ------------------------------------------------------------------------------
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#print(isPalindrome('abcgdba'))

# fibonacci
# ------------------------------------------------------------------------------
def fib(x):
    assert type(x) == int and x>= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

# gcdRecur
# ------------------------------------------------------------------------------
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

#print(gcdRecur(6, 8))

# recurPowerNew
# ------------------------------------------------------------------------------
def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif (exp % 2 == 0):
        return recurPowerNew(base*base, exp/2)
    elif (exp % 2 == 1):
        return base * recurPowerNew(base, exp - 1)

#print(recurPowerNew(2, 5))

# recurFactorial
# ------------------------------------------------------------------------------
def recurFact(n):
    if n == 0:
        return 1
    else:
        return n*recurFact(n-1)

#print(recurFact(10))

# recurPower
# ------------------------------------------------------------------------------
def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

#print(recurPower(5, 2))


# iterPower
# ------------------------------------------------------------------------------
def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

#print(iterPower(5, 2))
