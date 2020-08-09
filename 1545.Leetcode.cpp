#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
using namespace std;
string reverseStr(string s) {
        int start = 0, end = s.length() -1;
        while(start<end) {
            swap(s[start], s[end]);
            start++;
            end--;
        }
        return s;
    }

    string invert(string s) {
       for(int i = 0; i < s.length(); i++) {
           if(s[i] == '1')
               s[i] = '0';
           else
               s[i] = '1';
       }
        return s;
    }


    char findKthBit(int n, int k) {
        vector<string> s(n);

        s[0] = "0";
        for(int i = 1; i < n; i++) {
            s[i] = s[i-1] + "1" + reverseStr(invert(s[i-1]));
        }
       // cout<<s[n]<<endl;
       //for(int i = 1; i < n; i++) {
           //cout<<s[i]<<endl;
        //}
        string res = s[n-1];
        //cout<<"String:"<<res<<endl;
        return res[k-1];
    }

int main() {

   cout << "\nThe character is: "<<findKthBit(4,11);
}

