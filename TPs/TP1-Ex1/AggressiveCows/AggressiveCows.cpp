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


2
5 3
1
2
8
4
9
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





bool colocarVacas(vector<int>& stalls, int cows, int distMin) {
    int stallsLen = stalls.size();
    int lastNum = stalls[0];
    cows--;

    for (int i = 1; i < stallsLen; i++) {
        if (stalls[i] - lastNum >= distMin) {
            lastNum = stalls[i];
            cows--;
        }

        if (cows == 0) {
            return true;
        }
    }

    return cows == 0;
}



int aggresiveCows(vector<int>& stalls, int cows) {
    sort(stalls.begin(), stalls.end());
    int low = 1;  
    int high = stalls.back() - stalls[0]; 
    int res = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (colocarVacas(stalls, cows, mid)) {
            res = mid;  
            low = mid + 1;  
        }
        else {
            high = mid - 1; 
        }
    }

    return res;  
}

int main() {
    int t;
    cin >> t;
    vector<int> res;

    while (t--) {

        int n, c;
        cin >> n >> c;
        vector<int> stall(n);

        for (int i = 0; i < n; i++) {
            int si;
            cin >> si;
            stall[i] = si;
        }
        res.push_back(aggresiveCows(stall, c));

    }

    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << endl;;
    }
    
    return 0;
}