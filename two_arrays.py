'''
You are given two integer arrays, A and B, each containing N integers. The size of the array is less than or equal to 1000. You are free to permute the order of the elements in the arrays.

Now here's the real question: Is there an permutation A', B' possible of A and B, such that, A'i+B'i ≥ K for all i, where A'i denotes the ith element in the array A' and B'i denotes ith element in the array B'.

I/P:
2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4

O/P:
YES
NO
'''

t = input()
assert 1 <= t <= 10
for i in range(t):
    n,k = map(int, raw_input().strip().split())
    assert 1 <= n <= 1000
    assert 1 <= k <= 10**9
    A = map(int, raw_input().strip().split())
    A.sort()
    assert all(0 <= ele <= 10**9 for ele in A)
    B = map(int, raw_input().strip().split())
    B.sort(reverse=True)
    assert all(0 <= ele <= 10**9 for ele in B)
    answer = True
    for a,b in zip(A,B):
        if a+b < k:
            answer = False
    if answer:
        print "YES"
    else:
        print "NO"