//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
//User function template for C++
class Solution {
public: 
    int print2largest(int arr[], int n) {
        if (n < 2) // if array has less than 2 elements, there's no second largest element
            return -1;
        
        // Sort the array in non-decreasing order
        sort(arr, arr + n);
        
        // Traverse from end to find the second largest distinct element
        int i = n - 2;
        while (i >= 0 && arr[i] == arr[n - 1]) // skip duplicates of the largest element
            i--;
        
        if (i < 0) // if all elements are duplicates of the largest element
            return -1;
        
        return arr[i];
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.print2largest(arr, n);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends