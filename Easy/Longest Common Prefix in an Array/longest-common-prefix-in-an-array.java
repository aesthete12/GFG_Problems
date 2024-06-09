//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            int n = Integer.parseInt(read.readLine().trim());
            String arr[] = read.readLine().trim().split(" ");

            Solution ob = new Solution();
            System.out.println(ob.longestCommonPrefix(arr, n));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
    String longestCommonPrefix(String arr[], int n)
    {
        int min=arr[0].length();
        for(int i = 0 ; i <arr.length;i++)
        {
            if(min>arr[i].length())
                min = arr[i].length();
        }
        String common="";
        label:for(int i = 0 ; i <min;i++)
        {
            char c = arr[0].charAt(i);
            
            for(int k = 1 ; k <arr.length;k++)
            {
                if(c!=arr[k].charAt(i))
                {
                    if(i==0)
                    return "-1";

                    break label;
                }
                    
            }
            common+=c;
        }
        
        return common;
        
    }
}
