'''
You are given an integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.

The first few elements of fibonacci sequence are 0,1,1,2,3,5,8,13, A fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are 0 and 1.

I/P:
3
5
7
8

O/P:
IsFibo
IsNotFibo
IsFibo
'''
import math


def if_perfect_square(a):
	x = int(math.sqrt(a))
	return (x*x == a)


def if_fibo(a):
	return if_perfect_square(5*a*a + 4) or if_perfect_square(5*a*a - 4)


if __name__ == "__main__":
    n = input()
    inp = []
    while n != 0:
        inp.append(int(raw_input()))
        n -= 1

    for i in iter(inp):
    	if if_fibo(i):
    		print "IsFibo"
    	else:
    		print "IsNotFibo"