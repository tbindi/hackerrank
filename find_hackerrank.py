'''
At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

Starts with hackerrank
Ends with hackerrank
Start and ends with hackerrank

I/P:
4
i love hackerrank
hackerrank is an awesome place for programmers
hackerrank
i think hackerrank is a great place to hangout

O/P:
2
1
0
-1
'''
def find_hackerank(inp):
    check = 'hackerrank'
    for i in inp:
        if str(check) == i[0:10] and str(check) == i[-10:]:
            print 0
        elif str(check) == i[0:10]:
            print 1
        elif str(check) == i[-10:]:
            print 2
        else:
            print -1


if __name__ == "__main__":
    T = int(raw_input())
    inp = []
    while T != 0:
        T -= 1
        inp.append(raw_input())
        
    find_hackerank(inp)