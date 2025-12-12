#All questions must use a loop for full points.
import random
from itertools import count


def oddNumbers(n:int)-> str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string separated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    odd = ""
    for i in range(1,n+1,1):
        if i<n:
            if i%2 != 0:
                odd+= str(i)
            elif i%2 == 0:
                odd+= " "
        if i==n and i%2==1:
            odd+= str(i)
    print(odd)
    return odd

def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    back = ""
    for i in range (n,0,-1):
        if i>1:
            back += str(i)+" "
        elif i == 1:
            back+="1"
    print(back)
    return back


def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    roll = random.randint(1,10)
    tries = 0
    while roll in range(1,9):
        tries+= 1
        roll = random.randint(1, 10)
    print(f"it took {tries} tries to get a 10")

def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    gen = random.randint(1,100)
    nums = []
    for i in range(0,n,1):
        nums.append(gen)
        gen = random.randint(1,100)
    nums.sort()
    last = len(nums)-1
    smlst = nums[0]
    bgst = nums[last]
    print(nums)
    print(f"{smlst} and {bgst}")
    return smlst, bgst

def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    wLength = len(word)-1
    rev = ""
    for i in range(wLength,-1,-1):
        rev += word[i]
    return rev

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    order = ""
    endOrder = len(order)
    for i in range(1,n+1,1):
        if i%15 == 0:
            order += "fizzbuzz "
        elif i%3 == 0:
            order += "fizz "
        elif i%5 == 0:
            order += "buzz "
        else:
            order += str(i)+" "
    return order[0:-1]


def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    col = " "
    i = n
    while i != 1:
        if i %2 == 0:
            i = i//2
            col += str(i) + " "
        elif i%2 == 1:
            i = (3*i) + 1
            col += str(i) + " "
    cola = (str(n) + col[0:-1])
    return cola

def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    fib = [0,1]
    newN = 0
    if n <= 1:
        return str(fib[0])
    while len(fib) <= n:
        newN = fib[-1] + fib[-2]
        fib.append(newN)
    space = " "
    newFib = space.join(str(i) for i in fib)
    return newFib


#print(fibonacci(300))