//{ Driver Code Starts
// C++ program to remove recurring digits from
// a given number
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
public:
    vector<int> leaders(int a[], int n){
        vector<int> result;
        if(n == 0)
            return result;
        
        int max_right = a[n - 1]; // Rightmost element is always a leader
        result.push_back(max_right);
        
        for(int i = n - 2; i >= 0; i--){
            if(a[i] >= max_right){
                max_right = a[i];
                result.push_back(max_right);
            }
        }
        
        reverse(result.begin(), result.end()); // Reverse the result to maintain the original order
        return result;
    }
};

//{ Driver Code Starts.

int main()
{
   long long t;
   cin >> t;//testcases
   while (t--)
   {
       long long n;
       cin >> n;//total size of array
        
        int a[n];
        
        //inserting elements in the array
        for(long long i =0;i<n;i++){
            cin >> a[i];
        }
        Solution obj;
        //calling leaders() function
        vector<int> v = obj.leaders(a, n);
        
        //printing elements of the vector
        for(auto it = v.begin();it!=v.end();it++){
            cout << *it << " ";
        }
        
        cout << endl;

   }
}

// } Driver Code Ends