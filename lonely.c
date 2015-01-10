/*
There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs only once.

I/P:
1
1

O/P:
1
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
/* Head ends here */
int lonelyinteger(int a_size, int* a) {
    int i = 0;
    int temp;
    int j = i + 1;
    if(a_size == 1){
        return a[0];
    }else{
        while(i < a_size && j < a_size){
            if(a[i] == a[j]){
                if(j != (i+1)){
                    temp = a[i+1];
                    a[i+1] = a[j];
                    a[j] = temp;
                }
                i += 2;
                j = i+1;
            }else{
                j++;
            }
            if( i == 0 && j == a_size)
                break;
        }
        return a[i];
    }
}
/* Tail starts here */
int main() {
    int res;
    
    int _a_size, _a_i;
    scanf("%d", &_a_size);
    int _a[_a_size];
    for(_a_i = 0; _a_i < _a_size; _a_i++) { 
        scanf("%d", &_a[_a_i]);
    }
    
    res = lonelyinteger(_a_size,_a);
    printf("%d", res);
    
    return 0;
}