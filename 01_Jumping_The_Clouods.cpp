//
// Created by Jan Engelke on 08/12/2019.
//Taken from
// https://www.hackerrank.com/challenges/jumping-on-the-clouds/
//

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the jumpingOnClouds function below.
int jumpingOnClouds(vector<int> c) {
    int i = 0;
    int s = 0;
    while (i < c.size() - 1){
        if (i + 2 <= c.size() - 1) {
            if (c[i + 2] == 0) {
                i += 2;
            }
            else {
                i += 1;
            }
            s += 1;
        }
        else {
            i += 1;
            s += 1;

        }
    }
    return s;

}
