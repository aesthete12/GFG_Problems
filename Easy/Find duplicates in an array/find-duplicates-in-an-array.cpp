//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    vector<int> duplicates(long long a[], int n) {
        unordered_set<int> seen;
        unordered_set<int> duplicates;
        vector<int> result;

        for (int i = 0; i < n; i++) {
            if (seen.find(a[i]) != seen.end()) { // Found a duplicate
                duplicates.insert(a[i]);
            } else {
                seen.insert(a[i]);
            }
        }

        for (auto& num : duplicates) {
            result.push_back(num);
        }

        if (result.empty()) {
            result.push_back(-1); // No duplicates found
        } else {
            sort(result.begin(), result.end()); // Sort the result in ascending order
        }

        return result;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n;
        cin >> n;
        long long a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution obj;
        vector<int> ans = obj.duplicates(a, n);
        for (int i : ans) cout << i << ' ';
        cout << endl;
    }
    return 0;
}

// } Driver Code Ends