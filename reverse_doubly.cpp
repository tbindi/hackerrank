/*
You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list. The head node might be NULL to indicate that the list is empty.

I/P:
NULL 
NULL <-- 2 <--> 4 <--> 6 --> NULL

O/P:
NULL
NULL <-- 6 <--> 4 <--> 2 --> NULL
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
};/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev
   }
*/
Node* Reverse(Node* head)
{
    Node *temp = NULL;  
    Node *current = head;
      
     /* swap next and prev for all nodes of 
       doubly linked list */
     while (current !=  NULL)
     {
       temp = current->prev;
       current->prev = current->next;
       current->next = temp;              
       current = current->prev;
     }      
      
     /* Before changing head, check for the cases like empty 
        list and list with only one node */
     if(temp != NULL )
        head = temp->prev;
    return head;
}Node* Insert(Node *head, int data)
{
	Node *temp = new Node();
	temp->data = data; temp->prev = NULL; temp->next = NULL;
	if(head == NULL) return temp;
	head->prev = temp;
	temp->next = head;
	return temp;
}
void Print(Node *head) {
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
		   head = Insert(head,x);
	   }
	   head = Reverse(head);
	   Print(head);
	}
}