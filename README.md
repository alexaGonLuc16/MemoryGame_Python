# Memory Game

This repository contains a Memory Game project developed in Python, where players are tasked with matching pairs of cards. The game runs in the console and keeps track of scores.

## How to Play

1. The game starts by asking the player for the size of the memory board. Only **even numbers between 2 and 10** are allowed.
2. The player must enter two coordinates (row and column) to reveal two cards. The goal is to find pairs of matching cards.
3. If the cards match, they remain face-up. If they do not match, they will flip back face-down, and the player loses a point.
4. The game continues until all pairs have been found. At the end, the score is saved, and previous scores can be reviewed.

## Requirements

- Python 3.x (only required if you want to run the source code)
- A terminal or console to run the Python script.

## Installation

### Running the Source Code

To set up and play the game using the source code on your machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/memory_game.git
    cd memory_game
    ```

2. **Run the game**:
    Run the game using Python:
    ```bash
    python memoryGame.py
    ```

### Running the Executable

If you prefer to run the game without installing Python, you can use the compiled executable. 

1. **Download the executable** (`memoryGame.exe`) from the releases section of this repository.
2. **Run the executable**:
    - Simply double-click the `memoryGame.exe` file to start the game. 
    - There is no need to have Python or any additional software installed.

### Optional: Compiling the Source Code to an Executable

If you want to compile the Python file to an executable (for Windows), you can use the `PyInstaller` package:

```bash
pip install pyinstaller
pyinstaller --onefile memoryGame.py
