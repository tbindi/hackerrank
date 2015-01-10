'''
Increasing popularity of hackerrank can be seen in tweets like

I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
Given a set of most popular tweets, your task is to find out how many of those tweets has the string hackerrank in it

I/P:
4
I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
interesting talk by hari, co-founder of hackerrank

O/P:
4
'''

def search(inp):
    count = 0
    for i in inp:
        if str('hackerrank') in str(i.lower()):
            count += 1
    
    print count
    

if __name__ == "__main__":
    T = int(raw_input())
    inp = []
    while T != 0:
        inp.append(raw_input())
        T -= 1
    
    search(inp)