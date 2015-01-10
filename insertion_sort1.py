'''
Sorting 
One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms.

Insertion Sort 
These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. We will first start with an already sorted list.

Insert element into sorted list 
Given a sorted list with an unsorted number V in the right-most cell, can you write some simple code to insert V into the array so it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of V to a variable, and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until V can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace a value with V.

I/P:
5
2 4 6 8 3

O/P:
2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 

'''

def print_ar(ar):
    out = str('')
    for i in ar:
        out += str(i) + ' '
    print out

    
# Head ends here
def insertionSort(ar):    
    i = len(ar) - 1
    while i > 0:
        temp = ar[i]
        j = i
        while j > 0 and ar[j-1] > temp:
            ar[j] = ar[j-1]
            j = j - 1
            print_ar(ar)
        ar[j] = temp
        i = j - 1
    print_ar(ar)
    
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)