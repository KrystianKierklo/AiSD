# zadanie 1

def numbers(n):
    if n<0:
        return
    print(n)
    numbers(n-1)


# zadanie 2

def fib(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# zadanie 3
def power(number, n):
    if n < 1:
        return 1
    return number * power(number, n-1)

# zadanie 4
def reverse(txt):
    return txt[::-1]

# zadanie 5
def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    elif n in(0,1):
        return 1

# zadanie 6
def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    licznik = 1
    while(licznik*licznik < n):
        if(prime(licznik)):
            if(n % licznik == 0):
                return False
        licznik += 1
    return True

# zadanie 7




# zadanie 8





# zadanie 9





# zadanie 10




numbers(30)
print(fib(20))
print(power(3,3))
print(reverse('XDXD'))
print(factorial(4))
print(prime(17))

