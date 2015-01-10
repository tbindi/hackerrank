'''
Little Bob loves chocolates, and goes to a store with $N in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?

I/P:
3
10 2 5
12 4 4
6 2 2

O/P:
6
3
5
'''


def chocolate_feast(inp):
    for i in inp:
        N = i[0]
        C = i[1]
        M = i[2]
        ate = wrap = int(N/C)
        while wrap >= M:
            ate += int(wrap/M)
            wrap = int(wrap%M) + int(wrap/M)
        print ate
            

    
if __name__ == "__main__":
    T = int(raw_input())
    inp = []
    while T != 0:
        inp.append(map(int,raw_input().split(' ')))
        T -= 1
    
    chocolate_feast(inp)