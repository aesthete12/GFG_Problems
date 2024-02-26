//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    vector<string> AllPossibleStrings(const string& s) {
        vector<string> result;
        generate(s, 0, "", result);
        sort(result.begin(), result.end()); // Sort the result lexicographically
        return result;
    }

private:
    void generate(const string& s, int index, string current, vector<string>& result) {
        if (index == s.length()) {
            if (!current.empty()) {
                result.push_back(current);
            }
            return;
        }

        generate(s, index + 1, current, result); // Exclude current character

        current.push_back(s[index]);
        generate(s, index + 1, current, result); // Include current character
    }
};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string s;
		cin >> s;
		Solution ob;
		vector<string> res = ob.AllPossibleStrings(s);
		for(auto i : res)
			cout << i <<" ";
		cout << "\n";

	}
	return 0;
}
// } Driver Code Ends