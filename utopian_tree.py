'''
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter. 
Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

I/P:
2
3
4

O/P:
6
7


Explanation: #01: 
There are 2 testcases. 
N = 3: 
the height of the tree at the end of the 1st cycle = 2 
the height of the tree at the end of the 2nd cycle = 3 
the height of the tree at the end of the 3rd cycle = 6

N = 4: 
the height of the tree at the end of the 4th cycle = 7
'''

def ret_value(level):
	if level == 0:
		return 1
	elif level % 2 == 1:
		return 2 * ret_value(level-1)
	elif level % 2 == 0:
		return 1 + ret_value(level-1)


if __name__ == "__main__":
    n = input()
    inp = []
    while n != 0:
        inp.append(input())
        n -= 1

    for i in iter(inp):
    	print ret_value(i)