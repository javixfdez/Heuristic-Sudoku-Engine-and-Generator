# Sudoku Engine: Algorithmic Solver & Generator

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Python-based Sudoku engine implementing Depth-First Search (Backtracking) and Greedy heuristic algorithms. Features a full pipeline for valid board generation, logic validation, and complexity analysis

## Project Overview
This project, developed for **Programming II**, focuses on the implementation of advanced algorithms to solve and generate Sudoku puzzle.The goal is to efficiently populate a $9\times9$ grid while adhering to the core constraints: every row, column, and $3\times3$ subgrid must contain digits 1-9 without repetition.

## Algorithmic Approaches
The engine compares two distinct methodologies to handle Sudoku as a constraint-satisfaction problem:

### 1. Backtracking (Depth-First Search)
A methodical technique that fills cells by exploring valid possibilities recursively. 
* **Reliability:** Guaranteed to find a solution if it exists.
* **Complexity:** In the worst-case scenario, it explores $O(9^{81})$ configurations.

### 2. Greedy Heuristic
An optimized approach that selects the most "promising" number at each step based on local frequency.
* **Efficiency:** Uses `get_possible_numbers_greedy` to sort candidates by their occurrence in rows, columns, and subgrids.
* **Optimization:** Significantly reduces the number of reversals/backtracks required in practical cases.

## Key Features
- **Dynamic Board Generation:** Creates full, valid boards by first filling diagonal $3\times3$ subgrids and then completing the rest via backtracking.
- **Playable Puzzle Creation:** Generates puzzles of varying difficulty by selectively removing up to 50 numbers from a complete board.
- **Robust Validation:** Includes a comprehensive testing suite for original, empty, and invalid boards (e.g., handling repeated numbers in rows).
