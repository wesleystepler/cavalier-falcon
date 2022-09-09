#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include "node.h"
using namespace std;

int main(int argc, char** argv) {
   ifstream file("input.txt");

   vector<vector<int>> adj_list; 
   vector<int> not_nodes; 
      if (!file.is_open()) {
    cout << "Unable to open file for reading" << endl;
    exit(2);
   } 

   string s;
   while (getline(file, s)) {

      if (s.size() > 1) {
        int which_node = 0;
         for(int i = 0; i < s.size(); i++) {
            int previous;

            if (isdigit(s[i])) {
                //cout << "Node: " << s[i] << endl;
                if (which_node > 0) {
                    cout << "Made it here" << endl; 
                    vector<int> connection{s[i]};
                    adj_list.insert(adj_list.begin()+previous, connection);
                }
            previous = s[i];
            }
            which_node++;  
            }       
       
        } else {
            cout << "Made it here" << endl;
            not_nodes.push_back(int(s.at(0)));
        }
    }

    for (int x : not_nodes) {
        cout << x << endl;
    }    

}
   
   

