'''
Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.


I/P:
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

O/P:
3
4
0
0
4

Explanation

AAAA⟹A, 3 deletions
BBBBB⟹B, 4 deletions
ABABABAB⟹ABABABAB, 0 deletions
BABABA⟹BABABA, 0 deletions
AAABBB⟹AB, 4 deletions
'''


def num_del(string):
	first = string[0]
	value = 0
	i = 1
	while i != len(string):
		if first == string[i]:
			value += 1
		else:
			first = string[i]
		i += 1
	
	return value


if __name__ == "__main__":
    n = input()
    inp = []
    while n != 0:
        inp.append(raw_input())
        n -= 1

    for i in iter(inp):
    	print num_del(i)