'''
In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an element with just the first element - that is already "sorted" since there's nothing to its left that is smaller than it.

In this challenge, don't print every time you move an element. Instead, print the array every time an element is "inserted" into the array in (what is currently) its correct place. Since the array composed of just the first element is already "sorted", begin printing from the second element and on.

I/P:
6
1 4 3 5 6 2

O/P:
1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 
'''

def print_ar(ar):
    out = str('')
    for i in ar:
        out += str(i) + ' '
    print out

    
# Head ends here
def insertionSort(ar):
    for i in range(1,len(ar)):
        x = ar[i]
        j = i
        while j > 0 and ar[j-1] > x:
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = x
        print_ar(ar)
          
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)