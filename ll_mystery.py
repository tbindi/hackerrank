'''
James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows 2 rules:

(a) He can reduce the value of a letter, e.g. he can change 'd' to 'c', but he cannot change 'c' to 'd'. 
(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.

Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome. 

I/P:
4
abc
abcba
abcd
cba

O/P:
2
0
4
2
'''

def get_pal(string):
	i = value = 0
	while i <= (len(string)-1)/2:
		value += abs(ord(string[i])-ord(string[len(string)-i-1]))
		i += 1

	return value


if __name__ == "__main__":
    n = input()
    inp = []
    while n != 0:
        inp.append(raw_input())
        n -= 1

    for i in iter(inp):
    	print get_pal(i)