//
// Created by jan on 29.12.19.
// https://www.hackerrank.com/challenges/mark-and-toys
//

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the maximumToys function below.
int maximumToys(vector<int> prices, int k) {
    sort (prices.begin(), prices.end());
    int i = 0;
    long mysum = 0;
    for (int j = 0; j < prices.size(); j++){
        mysum += prices[j];
        if (mysum < k){
            i++;
        }
    }
    return(i);
}