//{ Driver Code Starts
//Initial Template for Java



import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            int n = Integer.parseInt(br.readLine().trim());
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            new Solution().rearrange(arr, n);
            for (int i = 0; i < n; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


//User function Template for Java




class Solution {
    void rearrange(int arr[], int n) {
        
        int PosNeg[] = new int[n];
        int j = 0; 
        int k = n - 1; 
        
        for (int i = 0; i < n; i++) {
            if (arr[i] >= 0) {
                PosNeg[j] = arr[i];
                j++;
            } else {
                PosNeg[k] = arr[i];
                k--;
            }
        }
        int t = 0, s = n - 1, f = 0;
        while (t < j && s > k) {
            arr[f] = PosNeg[t];
            f++;
            t++;
            if (f < n) {
                arr[f] = PosNeg[s];
                f++;
                s--;
            }
        }
        while (t < j) {
            if (f < n) {
                arr[f] = PosNeg[t];
                f++;
                t++;
            }
        }
        while (s > k) {
            if (f < n) {
                arr[f] = PosNeg[s];
                f++;
                s--;
            }
        }
    }
}