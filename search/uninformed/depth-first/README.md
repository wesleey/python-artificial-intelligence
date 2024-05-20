# Depth-first Search (DFS)
## Introduction
A depth-first search (DFS) algorithm explores graph or tree structures by traversing down one branch as far as possible before backtracking. This strategy entails managing the frontier, which is the set of nodes that are yet to be explored. In DFS, the frontier is typically handled using a stack data structure, adhering to the "last-in, first-out" (LIFO) principle.

## Usage
```bash
python maze.py maze.txt
```

## Examples
### Maze 1
![img](./images/maze1.png)
### Solution 1
![img](./images/maze1_solution.png)
### States Explored: 17
![img](./images/maze1_explored.png)

### Maze 2
![img](./images/maze2.png)
### Solution 2
![img](./images/maze2_solution.png)
### States Explored: 194
![img](./images/maze2_explored.png)

### Maze 3
![img](./images/maze3.png)
### Solution 3
![img](./images/maze3_solution.png)
### States Explored: 483
![img](./images/maze3_explored.png)

## References
- [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/)
