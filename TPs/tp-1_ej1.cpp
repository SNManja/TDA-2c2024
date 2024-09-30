/*
AGGRCOW - Aggressive cows
Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1 ... xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
Input
t – the number of test cases, then t test cases follows.
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi
Output
For each test case output one integer: the largest minimum distance.


1
5 3
1
2
8
4
9


*/

#include <iostream>
#include <algorithm>
#include <climits> 
#include <vector>
using namespace std;



int acRec(int i, int c, int ult, int lmd, vector<int>& s, int size) {
    if (i >= size && c != 0) {
        return INT_MAX;
    }
    else if (c == 0) {
        return lmd;
    }
    else {
        return min(acRec(i + 1, c - 1, i, max(lmd, s[i] - s[ult]), s, size), acRec(i+1,c,ult,lmd,s,size));
    }
}

int AggressiveCows(int c, vector<int>& s, int size) {
    sort(s.begin(), s.end());
    return acRec(0, c, 0, 0, s, size);
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        
        int n, c;
        cin >> n >> c;
        vector<int> stall(n);

        for (int i = 0; i < n; i++) {
            int si;
            cin >> si;
            stall[i] = si;
        }
        cout << AggressiveCows(c, stall, n) << endl;

    }
    return 0;
}