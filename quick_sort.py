'''
The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm. Insertion Sort has a running time of O(N2) which isn't fast enough for most purposes. Instead, sorting in the real-world is done with faster algorithms like Quicksort, which will be covered in the challenges that follow.

The first step of Quicksort is to partition an array into two smaller arrays.

I/P:
5
4 5 3 7 2

O/P:
3 2 4 5 7

'''


# Head ends here
def partition(ar):
    pivot = ar[0]
    left = []
    right = []
    for i,c in enumerate(ar[1:]):
        if c > pivot:
            right.append(c)
        else:
            left.append(c)
            
    print " ".join([str(x) for x in left + [pivot] + right])
            
    
    
# Tail starts here
m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)