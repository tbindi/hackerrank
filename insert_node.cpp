/*
You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node. A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

I/P:
NULL, data = 3, position = 0 
3 --> NULL, data = 4, position = 0

O/P:
3 --> NULL
4 --> 3 --> NULL
*/

#include <iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
struct Node
{
	int data;
	Node *next;
};Node* InsertNth(Node *head, int data, int position)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->next = NULL;
    Node *temp = head;
    if(position == 0)
    {
        newNode->next = head;
        head = newNode;
    }
    else
    {
        for(int i = 1; i < position; i++)
            temp = temp->next;
        newNode->next = temp->next;
        temp->next = newNode;
    }
    return head;
}void Print(Node* head)
{
	while(head != NULL)
	{
		cout<<head->data;
		head=head->next;
	}
}

int main()
{
	int t;
	cin>>t;
	    Node *head = NULL;
		 head = new Node();
		 head->data = 2;
		 head->next = NULL;
	while(t-- >0){
		int x,n; cin>>x>>n;
		 head = InsertNth(head,x,n);
	}
	 Print(head);
	   cout<<"\n";

}