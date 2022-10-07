num_nodes = 3
adj_matrix = [
    [0,1,1],
    [0,0,1],
    [0,0,0]
]

run_time = 0
# Naieve Implementation
for i in range(0, len(adj_matrix)):
    counter = 0
    for j in range(0, len(adj_matrix[i])):
        run_time += 1
        if adj_matrix[i][j] == 0:
            counter += 1
    if counter == num_nodes:
        print(i)
        print(run_time)
        break
    run_time += 1

# Faster Implementation
candidate_nodes = [0, 1, 2]
for i in range(0, len(adj_matrix)):
    for j in range(0, len(adj_matrix[i])):
        if adj_matrix[i][j] == 0:


"""
Pseudo-Code
hash table of candidate nodes
While candidate nodes > 1:
    Set u as the first row, and v as the next column after the first that hasn't been eliminated.
    if (u, v) == 0, 
        remove v from the candidate nodes and ignore the vth row and column from now on
    else if (u, v) == 1, 
        remove u from the candidate nodes and ignore the uth and vth row and column from now on

Once you know what the last remaining candidate node is, go to that row in the matrix and confirm that it is all zeroes. If it is, you have found your sink-node.
"""    



"""
The algorithm will run as follows: while there is more than one row left in the matrix, which we will call g, if g[u][v] is equal to 0, remove the row corresponding to the node v in g. And if g[u][v] is equal to 1, then remove the row corresponding to u in g.


set u to the first index that is still a candidate for the sink-node (so, if our graph had nodes labeled 0, 1, 2, 3, 4, and we had no information about any of them, we would set u to be the 0th row. But if we already knew 0 and 1 were not the sink node, we would set u to be the 2nd row), and set v to index u + 1, and then

"""   
    
    


    
"""

