# Sudoku Engine: Algorithmic Solver & Generator

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Python-based Sudoku engine implementing Depth-First Search (Backtracking) and Greedy heuristic algorithms. Features a full pipeline for valid board generation, logic validation, and complexity analysis

## Project Overview
[cite_start]This project, developed for **Programming II**, focuses on the implementation of advanced algorithms to solve and generate Sudoku puzzles[cite: 1, 3, 8]. [cite_start]The goal is to efficiently populate a $9\times9$ grid while adhering to the core constraints: every row, column, and $3\times3$ subgrid must contain digits 1-9 without repetition[cite: 8].

## Algorithmic Approaches
The engine compares two distinct methodologies to handle Sudoku as a constraint-satisfaction problem:

### 1. Backtracking (Depth-First Search)
[cite_start]A methodical technique that fills cells by exploring valid possibilities recursively[cite: 16, 82]. 
* [cite_start]**Reliability:** Guaranteed to find a solution if it exists[cite: 84].
* [cite_start]**Complexity:** In the worst-case scenario, it explores $O(9^{81})$ configurations[cite: 150].

### 2. Greedy Heuristic
[cite_start]An optimized approach that selects the most "promising" number at each step based on local frequency[cite: 17, 121].
* [cite_start]**Efficiency:** Uses `get_possible_numbers_greedy` to sort candidates by their occurrence in rows, columns, and subgrids[cite: 120].
* [cite_start]**Optimization:** Significantly reduces the number of reversals/backtracks required in practical cases[cite: 157].

## Key Features
- [cite_start]**Dynamic Board Generation:** Creates full, valid boards by first filling diagonal $3\times3$ subgrids and then completing the rest via backtracking[cite: 126, 131].
- [cite_start]**Playable Puzzle Creation:** Generates puzzles of varying difficulty by selectively removing up to 50 numbers from a complete board[cite: 132, 138].
- [cite_start]**Robust Validation:** Includes a comprehensive testing suite for original, empty, and invalid boards (e.g., handling repeated numbers in rows)[cite: 158, 160].

## Complexity Analysis
| Method | Theoretical Worst Case | Practical Efficiency |
| :--- | :--- | :--- |
| **Backtracking** | $O(9^{81})$ | High for standard puzzles |
| **Greedy** | $O(9^{81})$ | [cite_start]Superior for complex/typical cases [cite: 157] |

[cite_start]The Greedy function performs row/column checks at $O(9)$ and sorts candidates at $O(9 \log 9)$, maintaining a constant $O(1)$ overhead due to the fixed board size[cite: 154, 155].
