//
// Created by jan on 10.01.20.
// https://www.hackerrank.com/challenges/ctci-making-anagrams
//

#include <bits/stdc++.h>

using namespace std;

// Complete the makeAnagram function below.
int makeAnagram(string a, string b) {
    vector <int> char_arr (26, 0);
    double count = 0;
    for (int i : a){
        char_arr[i - 'a'] += 1;
    }
    for (int i : b){
        char_arr[i - 'a'] -= 1;
    }
    for (auto val : char_arr) { count += abs(val); }
    return count;
}