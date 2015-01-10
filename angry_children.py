'''
Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to distribute one packet to each of the K children in the village (each packet may contain different number of candies). To avoid any fighting among the children, he would like to pick K out of N packets, such that unfairness is minimized.

Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi denotes the number of candies in the ith packet, then we define unfairness as

max(x1,x2,...xk) - min(x1,x2,...xk)

where max denotes the highest value amongst the elements, and min denotes the least value amongst the elements. Can you figure out the minimum unfairness and print it?
'''

n = int(input())
k = int(input())

vec = []
for i in range(0, n):
    vec.append(int(input()))

vec.sort()

m = vec[-1] - vec[len(vec) - k + 1]
for i in range(0, n-k+1):
    if vec[i+k-1] - vec[i] < m:
        m = vec[i+k-1] - vec[i]

print(m)