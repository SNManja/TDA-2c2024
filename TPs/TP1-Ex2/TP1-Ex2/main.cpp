#include <iostream>
#include <algorithm> 
#include <vector>
#include <unordered_map>

using namespace std;



int paintingRec(vector<int>& arr, vector<vector<vector<int>>>& memo,int i, int lastB, int lastW) {
    if (i == arr.size()) {
        return 0;
    }
    if (memo[i][lastB][lastW] != -1) {
        return memo[i][lastB][lastW];
    } else {
        int bestPath;

        bestPath = 1 + paintingRec(arr, memo, i + 1, lastB, lastW);

        if ( lastB == arr.size() || arr[lastB] < arr[i] ) {
            
            int blackPath = paintingRec(arr, memo, i + 1, i, lastW);

            if (blackPath < bestPath) {
                bestPath = blackPath;
            }
        }
        
        if ( lastW == arr.size() || arr[lastW] > arr[i] ) {
            
            int whitePath = paintingRec(arr, memo, i + 1, lastB, i); 
            if (whitePath < bestPath) {
                bestPath = whitePath;
            }
        }

        memo[i][lastB][lastW] = bestPath;
        return memo[i][lastB][lastW];
    }

   
}

int blackOrWhite(vector<int>& arr) {
    vector<vector<vector<int>>> memo(arr.size()+1, vector<vector<int>>(arr.size()+1, vector<int>(arr.size()+1, -1)));
;

    return paintingRec(arr, memo, 0, arr.size(), arr.size());
}


int main() {
    vector<vector<int>> testCases;
    int N;

    while (cin >> N && N != -1) {
        vector<int> seq(N);
        for (int i = 0; i < N; ++i) {
            cin >> seq[i];
        }
        testCases.push_back(seq);
    }

    for (int i = 0; i < testCases.size(); i++) {
        cout << blackOrWhite(testCases[i]) << endl;
    }

    return 0;
}