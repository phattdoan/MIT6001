# fibonacci
# ------------------------------------------------------------------------------
def fib(x):
    assert type(x) == int and x>= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

print(fib(35))

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
