'''
King Robert has 7 kingdoms under his rule. He finds out from a raven that the Dothraki are soon going to wage a war against him. But, he knows the Dothraki need to cross the Narrow River to enter his realm. There is only one bridge that connects both banks of the river which is sealed by a huge door.

I/P:
aaabbbb

O/P:
YES

I/P:
cdefghmnopqrstuvw

O/P:
NO

I/P:
cdcdcdcdeeeef

O/P:
YES
'''
def if_palind(string):
	i = 0
	flag = True
	final = True
	if len(string) % 2 == 1:
		while i < len(string):
			if string.count(string[i]) % 2 == 1 and flag:
				flag = False
			elif string.count(string[i]) % 2 == 1 and not flag:
				final = False
				break
			string = string.replace(string[i],'')
			i += 1
	else:
		while i < len(string):
			if string.count(string[i]) % 2 == 1:
				final = False
				break
			string = string.replace(string[i],'')
			i += 1
	return final


if __name__ == "__main__":
    inp = raw_input()
    if if_palind(inp):
    	print "YES"
    else:
    	print "NO"