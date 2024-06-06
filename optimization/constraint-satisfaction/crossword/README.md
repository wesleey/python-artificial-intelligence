# Crossword

This project implements a Crossword Puzzle Solver using Constraint Satisfaction Problems (CSP). The solver employs techniques such as node consistency, arc consistency (AC-3), and backtracking search with heuristics to efficiently solve crossword puzzles.

![Crossword](./images/crossword.png)

## Usage
```bash
python generate.py structure words [output]
```

## Features
- Enforces node and arc consistency.
- Uses backtracking search with heuristics.
- Can print the crossword puzzle to the terminal.
- Can save the crossword puzzle as an image file

## References
- [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/)
