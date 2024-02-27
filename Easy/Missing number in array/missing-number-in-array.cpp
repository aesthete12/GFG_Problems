//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;




// } Driver Code Ends
// User function template for C++

class Solution {
public:
    int missingNumber(vector<int>& nums, int n) {
        // Calculate the sum of all integers from 1 to n
        int sum = (n * (n + 1)) / 2;
        
        // Subtract the sum of the elements in the array
        for (int num : nums) {
            sum -= num;
        }
        
        // The result will be the missing number
        return sum;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> array(n - 1);
        for (int i = 0; i < n - 1; ++i) cin >> array[i];
        Solution obj;
        cout << obj.missingNumber(array, n) << "\n";
    }
    return 0;
}
// } Driver Code Ends