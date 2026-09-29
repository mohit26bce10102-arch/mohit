# Rock Paper Scissors Game

A classic command-line implementation of Rock Paper Scissors. Built by a first-semester B.Tech CSE student utilizing pure Python variables, conditional rule dictionaries, loops, and math statistics.

## Project Structure
- `main.py`: The entire game is compacted into a single runnable python file. No external text documents to download or configure.

## Features
- **Dictionary Rule Logic**: Abandons messy if/elif logic structures substituting a clean dictionary matching key-value pairs to determine round winners.
- **Dynamic Series Math**: Play Best of 3 (First to 2) or Best of 5 (First to 3) seamlessly.
- **Tolerant Inputs**: Program successfully handles full words (`rock`, `paper`, `scissors`) or rapid abbreviations (`r`, `p`, `s`). Caps agnostic.
- **Session Stats Engine**: Securely maps consecutive gaming matches into a floating percentage calculation dynamically tracking your win/loss metrics until application shutdown.

## Setup and Run Instructions

1. Ensure Python 3 is installed horizontally on your machine (`python --version`).
2. Download or clone this folder containing `main.py`.
3. Open your computer's terminal or command prompt.
4. Navigate locally to the game folder:
   ```bash
   cd "path/to/rock paper game"
   ```
5. Execute the active python file natively:
   ```bash
   python main.py
   ```
   *(macOS or Linux environments may require `python3 main.py`)*