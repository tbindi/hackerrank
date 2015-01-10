'''
You are given N lines and your task is to find out which of the N lines starts with

hi<BLANK>
where hi is case-insensitive and is not immediately followed by a space and a letter d(or D). 
In the above representation, BLANK denotes a space character.

I/P:
5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha

O/P:
Hi Alex how are you doing
'''

def search(inp):
    for i in inp:
        if str('hi ') == str(i[0:3]).lower() and str('d') != str(i[3]).lower():
            print i


if __name__ == "__main__":
    T = int(raw_input())
    inp = []
    while T != 0:
        T -= 1
        inp.append(raw_input())
        
    search(inp)