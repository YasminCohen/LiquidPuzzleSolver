# Liquid Puzzle Auto-Solver

This project provides an automated solution for the "Liquid Puzzle" game, employing advanced planning techniques and heuristics to quickly find solutions, even for large and complex puzzles.

## Features
- **Efficient Solving**: Utilizes heuristics to prioritize moves and solve puzzles faster.
- **Handles Large Inputs**: Designed to manage and solve large puzzles with many colors and tubes.
- **Recursive Backtracking**: Implements recursive backtracking to explore potential moves and find the optimal solution.
- **Snapshot-Based State Management**: Uses snapshots to keep track of game states and transitions.

## Example Usage
```python

# Example parameters
empty = 1
full = 3
size = 3
colors = 3
init = [[], [0, 1, 1], [2, 0, 1], [0, 2, 2]]

# Initialization of the first snapshot to start the solving process
initial_snapshot = snapshot(init, size, colors)
```
## How It Works

1. **Initialization**: Start with the initial configuration of the puzzle.
2. **Snapshot Creation**: Generate child snapshots representing possible moves from the current state.
3. **Heuristic Evaluation**: Calculate weights for each snapshot to prioritize more promising moves.
4. **Recursive Exploration**: Use recursive backtracking to explore potential solutions.
5. **Winning Condition**: Check for the winning condition where each tube contains only one color or is empty.

## Class Definitions

### `class snapshot`

- **Attributes**:
  - `init`: Initial state of the puzzle.
  - `size`: Size of each tube.
  - `color_count`: Number of different colors in the puzzle.
  - `dad`: Reference to the parent snapshot.
  - `childs`: List of child snapshots generated from the current state.
  - `weight`: Heuristic weight of the snapshot.
- **Methods**:
  - `create_childs()`: Generates child snapshots by simulating possible moves.
  - `forward()`: Recursively moves liquid between tubes.
  - `recognize_tube_with_the_same_color()`: Identifies tubes with the same color liquid.
  - `count_same()`: Counts the number of consecutive same-color liquids at the start of a tube.
  - `choose()`: Chooses the best child snapshot to continue solving.
  - `calc_weight()`: Calculates the heuristic weight of the snapshot.
  - `is_winner()`: Checks if the current state is a winning state.

## Running the Solver

To run the solver, initialize a `snapshot` object with the starting configuration of the puzzle and let the solver recursively find the solution.

```python
if __name__ == "__main__":
    initial_snapshot = snapshot(init, size, colors)
```

## Contributions
Contributions are welcome! Please fork the repository and submit pull requests.

## Getting Started

1. Clone the repository:
    ```sh
    git clone https://github.com/IlanSimchon/liquid-puzzle.git
    ```
2. Navigate to the project directory:
    ```sh
    cd liquid-puzzle
    ```
3. Run the solver with your puzzle configuration:
    ```python
    python main.py
    ```

## Contact
For any questions or issues, please open an issue on GitHub.


Feel free to modify and extend the code to fit different puzzle configurations and sizes. Enjoy solving Liquid Puzzles efficiently!

