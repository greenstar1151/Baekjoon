import sys
from collections import defaultdict


N = int(input())
case_in = sys.stdin.read().rstrip()
case_in = case_in.split('\n')
edges, K = case_in[:-1], int(case_in[-1])

graph_data = defaultdict(list)
root_node = 1
for i, edge in enumerate(edges):
    node_current = i + 1
    U, V = map(int, edge.split())
    graph_data[node_current] = [U, V]

def navigator(K: int): # yields bits of K(starting from lower) and yields 0 indefinitely
    while K != 0:
        yield K % 2
        K //= 2
    while True:
        yield 0

pathfinder = navigator(K-1) # bit sequence of K-1 is the navigator to determine left or right while desending binary tree
node_current_id = root_node
while True:
    node_child = graph_data[node_current_id]
    left, right = node_child
    if left == -1 and right == -1: # leaf, destination arrived
        break
    elif left == -1 or right == -1: # only one child, no need of pathfinding
        node_current_id = left if left != -1 else right
        continue
    else: # two children
        if next(pathfinder) == 0:
            node_current_id = node_child[0]
        else: # pathfinder == 1
            node_current_id = node_child[1]

print(node_current_id)

'''
13
2 -1
3 4
5 6
-1 7
8 -1
9 -1
10 11
12 13
-1 -1
-1 -1
-1 -1
-1 -1
-1 -1
1
'''
'''
K =  1,  2,  3, 4,  5
ac = 12, 10, 9, 11, 13
'''