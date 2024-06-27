//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
import java.lang.*;

class GFG {
    public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int test = Integer.parseInt(br.readLine());
		while(test-- > 0) {
			int N = Integer.parseInt(br.readLine());
			int [] A = new int[N];
			String [] str = br.readLine().trim().split(" ");
			for(int i = 0; i < N; i++)
				A[i] = Integer.parseInt(str[i]);
			Solution ob = new Solution();
			System.out.println(ob.equalSum(A, N));
		}
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    int equalSum(int [] A, int N) {
        //Write your code here
        int right_sum=0,left_sum=0,total_sum=0;
        for(int i=0;i<N;i++) total_sum+=A[i];
        
        for(int i=0;i<N;i++)
        {
            right_sum=total_sum-left_sum-A[i];
            if(right_sum==left_sum) return i+1;
            else left_sum+=A[i];
        }
        return -1;
    }
}