'''
Problem Statement

Given two integers: L and R,

find the maximal values of A xor B given, L ≤ A ≤ B ≤ R

I/P:
10
15

O/P:
7

In the second sample let's say L=10, R=15, then all pairs which comply to above condition are 
10⊕10=0 
10⊕11=1 
10⊕12=6 
10⊕13=7 
10⊕14=4 
10⊕15=5 
11⊕11=0 
11⊕12=7 
11⊕13=6 
11⊕14=5 
11⊕15=4 
12⊕12=0 
12⊕13=1 
12⊕14=2 
12⊕15=3 
13⊕13=0 
13⊕14=3 
13⊕15=2 
14⊕14=0 
14⊕15=1 
15⊕15=0 
Here two pairs (10,13) and (11,12) have maximum xor value 7 and this is the answer.
'''



def  maxXor( l,  r):
	max = l ^ l
	while l <= r:
		c = l
		while c <= r:
			if max < ( l ^ c ):
				max = l ^ c
			c += 1
		l += 1

	return max


_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
