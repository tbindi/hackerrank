/*
You’re given the pointer to the head node of a sorted doubly linked list and an integer to insert into the list. Create a node and insert it into the appropriate position in the list. The head node might be NULL to indicate that the list is empty.

I/P:
NULL , data = 2 
NULL <-- 2 <--> 4 <--> 6 --> NULL , data = 5

O/P:
NULL <-- 2 --> NULL
NULL <-- 2 <--> 4 <--> 5 <--> 6 --> NULL
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
	Node* prev;
};Node* SortedInsert(Node *head,int data)
{
    Node * temp = new Node();
    temp->data = data;
    temp->next = NULL;
    temp->prev = NULL;
    if (head == NULL)
    {
        head = temp;
        return head;
    }

    if (temp->data <= head->data)
    {
        temp->next = head;
        head->prev = temp;
        head = temp;
        return head;
    }

    Node *curr = head;
    while (curr->next!=NULL)
    {
        if (temp->data <= curr->data)
        {   
            curr->prev->next = temp;
            temp->prev = curr->prev;
            temp->next = curr;
            curr->prev = temp;
            return head;
        }

        curr = curr->next;
    }

    if (temp->data <= curr->data)
    {   // insert before last node
        curr->prev->next = temp;
        temp->prev = curr->prev;
        temp->next = curr;
        curr->prev = temp;
        return head;
    }
    // else insert at the end.
    curr->next = temp;
    temp->prev = curr;
    return head;
}void Print(Node *head) {
	if(head == NULL) return;
	while(head->next != NULL){ cout<<head->data<<" "; head = head->next;}
	cout<<head->data<<" ";
	while(head->prev != NULL) { cout<<head->data<<" "; head = head->prev; }
	cout<<head->data<<"\n";
}
int main()
{
	int t; cin>>t;
	Node *head = NULL;
	while(t--) {
	   int n; cin>>n;
           head = NULL;
	   for(int i = 0;i<n;i++) {
		   int x; cin>>x;
		   head = SortedInsert(head,x);
	       Print(head);
	   }
	}
}