//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class Main{
	static BufferedReader br;
    static PrintWriter ot;
    public static void main(String[] args) throws IOException{
        
        br = new BufferedReader(new InputStreamReader(System.in));
        ot = new PrintWriter(System.out);

        int t = Integer.parseInt(br.readLine());

        while(t-->0){
            
            String s[] = br.readLine().trim().split(" ");
            
            int n = Integer.parseInt(s[0]);
            int k = Integer.parseInt(s[1]);
            int a[] = new int[n];
            s = br.readLine().trim().split(" ");
            for(int i = 0; i < n; i++)
                a[i] = Integer.parseInt(s[i]);
            Solution obj = new Solution();
            ArrayList<Integer> res = obj.subarraySum(a, n, k);
            for(int ii = 0;ii<res.size();ii++)
                ot.print(res.get(ii) + " ");
            ot.println();
        }
        ot.close();
    }

}
// } Driver Code Ends


class Solution
{
   
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) 
    {
        int  sum=0;
        int i,j;
        i=j=0;
        ArrayList<Integer>al=new ArrayList<>();
        if(s==0){
            while(j < n && arr[j]!=0){
                j++;
            }
            if(j<n && arr[j]==0){
                al.add(j+1);
                al.add(j+1);
                return al;
            }
            else{
                al.add(-1);
                return al;
            }
        }
        else{
        while (j < n) {
        
                sum += arr[j];
            
           
            while (sum > s && i < j) {
                sum -= arr[i];
                i++;
            }
            
 
            if (sum == s) {
                al.add(i + 1); 
                al.add(j+1); 
                return al;
            }
            j++;
        }
        
        al.add(-1); 
        return al;
    }
    }
}