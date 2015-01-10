'''
In the previous challenge, you wrote code to perform an Insertion Sort on an unsorted array. But how would you prove that the code is correct? I.e. how do you show that for any input, your code will provide the right output?

Loop Invariant 
In computer science, you could prove it formally with a loop invariant, where you state that a desired property is maintained in your loop. Such a proof is broken down into 3 parts:

Initialization - It is true (in a limited sense) before the loop runs.
Maintenance - If it's true before an iteration of a loop, it remains true before the next iteration.
Termination. It will terminate in a useful way, once it is finished.
Insertion Sort's Invariant 
Say you have some InsertionSort code, where the outer loop goes through the whole array A:

for(int i = 1; i < A.length; i++){
//insertion sort code
You could then state the following loop invariant:

At the start of every iteration of the outer loop (indexed with i), the subarray until ar[i] consists of the original elements that were there, but in sorted order.

I/P:
6
1 4 3 5 6 2

O/P:
1 2 3 4 5 6
'''

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i
        key = l[i]
        while (l[j-1] > key) and (j > 0):
           l[j] = l[j-1]
           j -= 1
        l[j] = key
        


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))