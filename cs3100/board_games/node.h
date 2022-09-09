#ifndef NODE_H
#define NODE_H
#include <string>
using namespace std;

class node {
    public:
        node(); //Constructor
        node* previous;
        string color;
        int distance;
        
};

#endif