# Breadth-First Search (BFS)
## Introduction
A breadth-first search (BFS) algorithm explores graph or tree structures by traversing level by level, visiting all nodes at the current depth before moving on to nodes at the next depth level. This strategy involves managing the frontier, which is the set of nodes that are yet to be explored. In BFS, the frontier is typically handled using a queue data structure, adhering to the "first-in, first-out" (FIFO) principle.

## Usage
```bash
python maze.py maze.txt
```

## Examples
### Maze 1
![img](./images/maze1.png)
### Solution 1
![img](./images/maze1_solution.png)
### States Explored: 6
![img](./images/maze1_explored.png)

### Maze 2
![img](./images/maze2.png)
### Solution 2
![img](./images/maze2_solution.png)
### States Explored: 77
![img](./images/maze2_explored.png)

### Maze 3
![img](./images/maze3.png)
### Solution 3
![img](./images/maze3_solution.png)
### States Explored: 545
![img](./images/maze3_explored.png)

## References
- [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/)
