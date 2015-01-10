'''
Jack wants to build an IDE on his own. Help him build a feature which identifies the comments, in the source code of computer programs. Assume, that the programs are written either in C, C++ or Java. The commenting conventions are displayed here, for your convenience. At this point of time you only need to handle simple and common kinds of comments. You don't need to handle nested comments, or multi-line comments inside single comments or single-comments inside multi-line comments.

Your task is to write a program, which accepts as input, a C or C++ or Java program and outputs only the comments from those programs. Your program will be tested on source codes of not more than 200 lines.
// this is a single line comment
x = 1; // a single line comment after code

/* This is one way of writing comments */ 
/* This is a multiline 
   comment. These can often
   be useful*/

I/P:
/*This is a program to calculate area of a circle after getting the radius as input from the user*/  
#include<stdio.h>  
int main()  
{  
   double radius,area;//variables for storing radius and area  
   printf("Enter the radius of the circle whose area is to be calculated\n");  
   scanf("%lf",&radius);//entering the value for radius of the circle as float data type  
   area=(22.0/7.0)*pow(radius,2);//Mathematical function pow is used to calculate square of radius  
   printf("The area of the circle is %lf",area);//displaying the results  
   getch();  
}  
/*A test run for the program was carried out and following output was observed  
If 50 is the radius of the circle whose area is to be calculated
The area of the circle is 7857.1429*/  


O/P:
/*This is a program to calculate area of a circle after getting the radius as input from the user*/
//variables for storing radius and area  
//entering the value for radius of the circle as float data type  
//Mathematical function pow is used to calculate square of radius
//displaying the results  
/*A test run for the program was carried out and following output was observed  
If 50 is the radius of the circle
The area of the circle is 7857.1429*/  
'''


def print_comments(inp):
    p_check = False
    for i in inp:
        if str('//') in i:
            print i[i.find('//'):]
        if p_check:
            print i
        if str('*/') in i and p_check:
            p_check = False
            continue
        if str('/*') in i:
            if str('*/') in i:
                print i
            else:
                print i
                p_check = True
                continue
            
            

if __name__ == "__main__":
    inp = []
    while True:
        try:
            temp = raw_input()
        except EOFError, e:
            break
        inp.append(temp)
        
    print_comments(inp)