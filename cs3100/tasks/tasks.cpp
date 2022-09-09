#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;


/**
 * @brief Implementation of the GraphNode class we will use to generate the graph.
 * 
 * @class GraphNode
 * 
 * The GraphNode class stores how many indegrees a vertex has,
 * the label of the vertex, and a vector of pointers which represent the outgoing edges 
 */
class GraphNode {
public:
	GraphNode() {
		indegrees = 0;
	}
	int indegrees; 
	string label;
	vector<GraphNode*> ptrs;
};

void sortGraph(vector<GraphNode*> degZero, vector<GraphNode*> s);

int main(int argc, char** argv) {
	vector<GraphNode*> nodes;
	vector<string> titles;

	// attempt to open the supplied file
    ifstream file(argv[1], ifstream::binary);
    // report any problems opening the file and then exit
    if (!file.is_open()) {
        cout << "Unable to open file '" << argv[1] << "'." << endl;
        exit(2);
    }

    while (file.good()) {
	    // read in two strings
	    GraphNode* a;
	    GraphNode* b;
	    string s1, s2;
	    file >> s1;
	    file >> s2;
	    if (s1 == "0")
	    	break;
	    //Check if you've already made any other nodes
	    if (nodes.size() != 0) {
	    	bool aExists = false;
	    	for (int i = 0; i < nodes.size(); i++) {
	    		if (s1 == nodes.at(i) -> label) {
	    			a = nodes.at(i);
	    			aExists = true;
	    			break;
	    		}
	    	}
	    	bool bExists = false;
	    	for (int i = 0; i < nodes.size(); i++) {
	    		if (s2 == nodes.at(i) -> label) {
	    			b = nodes.at(i);
	    			bExists = true;
	    			break;
	    		}
	    	}
	    

	    	if (aExists == false) {
	    		a = new GraphNode();
	    		a -> label = s1;
	    		nodes.push_back(a);
	    	}

	    	if (bExists == false) {
	    		b = new GraphNode();
	    		b -> label = s2;
	    		nodes.push_back(b);
	    	}

	    	a -> ptrs.push_back(b);
	    	b -> indegrees += 1;

	    } else { //These are the first two nodes
	    	a = new GraphNode();
	    	b = new GraphNode();
	    	a -> label = s1;
	    	b -> label = s2;
	    	a -> ptrs.push_back(b);
	    	b -> indegrees += 1;
	    	nodes.push_back(a);
	    	nodes.push_back(b);
	    }

	    

	    // output those strings
	    //cout << s1 << " -> ";
	    //cout << s2 << endl;
	} 
	vector<GraphNode*> degreeZero;
	for (int i = 0; i < nodes.size(); i++) {
		if (nodes.at(i) -> indegrees == 0) {
			//cout << nodes.at(i) -> label << endl;
			degreeZero.push_back(nodes.at(i));
		}
	}

	vector<GraphNode*> sorted;
	sortGraph(degreeZero, sorted);
	cout << endl;

}

/**
 * @brief Runs a topological sort on the given set of vertices and their edges
 * 
 * @param degZero a vector of vertices that have no incoming edges
 * @param s an empty vector that will contain the result of the topological sort
 * 
 * @author Wesley Stepler (pws3ms)
 * @date April 25, 2022
 */
void sortGraph(vector<GraphNode*> degZero, vector<GraphNode*> s) {
	while (degZero.size() != 0) {
		GraphNode* temp = degZero.at(degZero.size()-1);
		degZero.pop_back();
		s.push_back(temp);
		for (int i = 0; i < temp -> ptrs.size(); i++) {
			if (temp -> ptrs.at(i) != NULL) {
				temp -> ptrs.at(i) -> indegrees -= 1;
				if (temp -> ptrs.at(i) -> indegrees == 0)
					degZero.push_back(temp -> ptrs.at(i));

			}
		}
	}

	//cout << "Sorted: " << endl;
	for (int i = 0; i < s.size(); i++) {
		if (s.at(i) -> indegrees != 0) {
			cout << "Error: Graph has at least one cycle";
			break;
		}
		else
			cout << s.at(i) -> label << " ";
		

	}
}