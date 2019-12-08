//
// Created by Jan Engelke on 08/12/2019.
// Taken from
// https://www.hackerrank.com/challenges/repeated-string
//

#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {

    long int_div_num = (n / s.size());

    long remainder = n % s.size();
    string substring = s.substr(0, remainder);

    long string_count = count(s.begin(), s.end(), 'a');
    long substring_count = count(substring.begin(), substring.end(), 'a');

    long count = string_count * int_div_num + substring_count;

    return count;

}