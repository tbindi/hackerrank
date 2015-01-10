/*
You’re given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer, insert this node at the head of the linked list and return the new head node. The head pointer given may be null meaning that the initial list is empty.

I/P:
NULL , data = 1 
1 --> NULL , data = 2

O/P:
1 --> NULL
2 --> 1 --> NULL
*/

#include <iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

struct Node
{
	int data;
	Node *next;
};/*
  Insert Node at the begining of a linked list
  Initially head pointer argument could be NULL for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
return back the pointer to the head of the linked list in the below method.
*/
Node* Insert(Node *head,int data)
{
    Node *temp = new Node();
    temp->data = data;
    temp->next = head;
    return temp;
}void Print(Node *head)
{
	Node *temp = head;
	while(temp!= NULL){ cout<<temp->data<<"\n";temp = temp->next;}
}
int main()
{
	int t;
	cin>>t;
	Node *head = NULL;
	while(t-- >0)
	{
		int x; cin>>x;
		head = Insert(head,x);
	}
	Print(head);
}