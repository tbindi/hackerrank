/*
You’re given the pointer to the head node of a linked list. Find whether the list contains any cycle (or loop). A linked list is said to contain cycle if any node is re-visited while traversing the list. The head pointer given may be null meaning that the list is empty.

I/P:
1 --> NULL

1 --> 2 --> 3
      ^     |
      |     |
       -----    

O/P:
0
1

*/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
using namespace std;
struct Node
{
	int data;
	Node* next;
};/*
  Detect loop in a linked list 
  List could be empty also
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int HasCycle(Node* head)
{
    Node* tortoise = head;
    Node* hare = head;
    if(head == NULL) return 0;
    if(head->next == NULL) return 0;
    while(hare = hare->next)
    {
        if(hare->next == NULL || tortoise->next == NULL ) { return 0; }
        if(hare == tortoise) { return 1; }
        hare = hare->next;
        if(hare == tortoise) { return 1; }
        tortoise = tortoise->next;
    }
}int main()
{
	Node *A, *B, *C, *D,*E,*F;
	A = new Node();	B= new Node();  C= new Node(); D = new Node(); E = new Node(); F= new Node();
	// case 1:  NULL list 
	if(HasCycle(NULL)) cout<<"1";
	else cout<<"0";
	//case 2:
	A->next = B; 
	B->next = C;
	C->next = A;
	if(HasCycle(A)) cout<<"1";
	else cout<<"0";
	//case 3:  
	A->next = B; B->next = C; C->next = D; D->next = E; E->next = F; F->next = E;
	if(HasCycle(A)) cout<<"1";
	else cout<<"0";
	//case 4:
	A->next = B; B->next = C; C->next = D; D->next = E; E->next = F; F->next = NULL;
	if(HasCycle(A)) cout<<"1";
	else cout<<"0";
	// case 5:
	A->next = B; B->next = C; C->next = D; D->next = E; E->next = F; F->next = A;
	if(HasCycle(A)) cout<<"1";
	else cout<<"0";
}