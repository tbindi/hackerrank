'''
You will be provided with N lines of what are possibly IP addresses. You need to detect if the text contained in each of the lines represents an (a)IPv4 address (b)IPv6 address or (c)None of these.

IPv4 was the first publicly used Internet Protocol which used 4 byte addresses which permitted for 232 addresses. The typical format of an IPv4 address is A.B.C.D where A, B, C and D are Integers lying between 0 and 255 (both inclusive).

IPv6, with 128 bits was developed to permit the expansion of the address space. To quote from the linked article: The 128 bits of an IPv6 address are represented in 8 groups of 16 bits each. Each group is written as 4 hexadecimal digits and the groups are separated by colons (:). The address 2001:0db8:0000:0000:0000:ff00:0042:8329 is an example of this representation. Consecutive sections of zeros will be left as they are.

I/P:
3
This line has junk text.  
121.18.19.20  
2001:0db8:0000:0000:0000:ff00:0042:8329  

O/P:
Neither    
IPv4  
IPv6  
'''

import string


def check_ip(inp):
    for i in inp:
        if len(i.split('.')) == 4:
            temp = i.split('.')
            flag = True
            for j in temp:
                flag &= j.isdigit()
                if j.isdigit():
                    flag &= (int(j) >= 0 and int(j) <= 255)
                
            if flag:
                print 'IPv4'
            else:
                print 'Neither'
        elif len(i.split(':')) == 8:
            temp = i.split(':')
            flag = True
            for j in temp:
                flag &= all(c in string.hexdigits for c in j)
                flag &= len(j) <= 4
                    
            if flag:
                print 'IPv6'
            else:
                print 'Neither'
        else:
            print "Neither"

            

if __name__ == "__main__":
    T = int(raw_input())
    inp = []
    while T != 0:
        T -= 1
        inp.append(raw_input())
        
    check_ip(inp)