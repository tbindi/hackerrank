'''
The running time of an algorithm for a specific input depends on the number of operations executed. More the number of operations, the longer the running time of an algorithm. We usually want to know how many operations an algorithm will execute in proportion to the size of its input. (We call the size of the input N.)

For example, the first two input files for InsertionSort were small, so it was able to sort them quickly. But the next two files were larger and sorting them took more time. What is the ratio of the running time of InsertionSort to the size of the Input? To answer this question, we need to examine the InsertionSort algorithm.


I/P:
5 
2 1 3 1 2

O/P:
4
'''

# Head ends here
def insertionSort(ar):
    count = 0
    for i in range(1,len(ar)):
        x = ar[i]
        j = i
        while j > 0 and ar[j-1] > x:
            ar[j] = ar[j-1]
            j -= 1
            count += 1
        ar[j] = x
    print count
        
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)