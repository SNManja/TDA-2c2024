#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;  
    vector<int> res;

    while (T--) {
        int N;
        cin >> N;  

        vector<pair<int, int>> actividades(N);

        
        for (int i = 0; i < N; i++) {
            int start, end;
            cin >> start >> end;
            actividades[i] = { start, end };
        }

        sort(actividades.begin(), actividades.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;  
        });

        int current = 0;
        int thisRes = 0;
        for (int i = 0; i < actividades.size(); i++) {
            if (actividades[i].first >= current) {
                thisRes += 1;
                current = actividades[i].second;
            }
        }
        res.push_back(thisRes);
      
    }

    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << endl;

    }

    return 0;
}