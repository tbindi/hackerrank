/*

Given N integers, count the number of pairs of integers whose difference is K

I/P:
5 2  
1 5 3 4 2

O/P:
3
*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int k = in.nextInt();
		Set<Integer> set = new HashSet<Integer>();
		for (int i = 0; i < n; i++) {
			set.add(in.nextInt());
		}
		findPairs(set, k);
	}
 
	private static void findPairs(Set<Integer> set, int k) {
		int pairs = 0;
		for(Integer i: set){
			pairs += set.contains(i+k) ? 1:0;
		}
		
		System.out.println(pairs);
		
	}
}