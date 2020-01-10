//
// Created by jan on 29.12.19.
// https://www.hackerrank.com/challenges/ctci-bubble-sort
//

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the countSwaps function below.
void countSwaps(vector<int> a) {
    int s = 0;
    for (int i = 0; i < a.size(); i++){
        for (int j = 0; j < a.size() - 1; j++){
            if (a[j] > a[j + 1]){
                swap(a[j], a[j + 1]);
                s++;

            }
        }
    }
    cout << "Array is sorted in " << s << " swaps." << endl;
    cout << "First Element: " << a.front() << endl;
    cout << "Last Element: " << a.back() << endl;
}