/*
You’re given the pointer to the head node of a linked list. Change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

I/P:
NULL 
2 --> 3 --> NULL

O/P:
NULL
3 --> 2 --> NULL
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
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
    if(head == NULL)
        return NULL;
    
    Node *previous = NULL;
    while(head != NULL){
        Node *next = head->next;
        head->next = previous;
        previous = head;
        head = next;
    }
    return previous;
}Node* Insert(Node *head,int x)
{
   Node *temp = new Node();
   temp->data = x;
   temp->next = NULL;
   if(head == NULL) return temp;
   Node *temp1 = head;
   while(temp1->next != NULL)
	   temp1 = temp1->next;
   temp1->next = temp;
   return head;
}

void Print(Node* head)
{
	bool ok = true;
	while(head != NULL)
	{
		if(!ok) cout<<" ";
		else ok = false;
		cout<<head->data;
		head=head->next;
	}
}
int main()
{
	int t;
	cin>>t;
	while(t-- >0){
		Node *head = NULL;
		int x;cin>>x;
		while(x--)
		{
		  int n; cin>>n;
		  head = Insert(head,n);
		}
		head = Reverse(head);
	   Print(head);
	   cout<<"\n";

	}

}