# Chess960 Evaluation Suite

A Python project for systematically evaluating Chess960 (Fischer Random Chess) starting positions using the Stockfish chess engine.

## Overview

Chess960 has 960 possible starting positions. This project analyzes positions that don't have all pawns fully defended in their initial setup, evaluating them with Stockfish at depth 18 to understand their strategic characteristics.

## Project Structure

- **`chess960.py`** - Generates all 960 valid Chess960 positions and converts them to FEN notation
- **`pawn_support.py`** - Validates pawn support constraints (checks if pawns are defended by back rank pieces)
- **`main.py`** - Main evaluation loop that batches and evaluates positions with Stockfish
- **`.devcontainer/devcontainer.json`** - Dev container configuration with Python 3.10 and Stockfish

## Requirements

- Python 3.10+
- Stockfish chess engine
- stockfish Python package

## Installation

### Local Setup
```bash
pip install -r requirements.txt
sudo apt-get install stockfish  # On Ubuntu/Debian
# or brew install stockfish     # On macOS
```

### Dev Container
Open the project in GitHub Codespaces or VS Code with Dev Containers extension - the environment will be automatically configured.

## Usage

Run the evaluation script:
```bash
python3 main.py
```

The script will:
1. Generate all 960 Chess960 positions
2. Filter to positions with unsupported pawns
3. Evaluate the next 100 unevaluated positions using Stockfish
4. Save results incrementally to `chess960_results.json`

Results are persisted, so subsequent runs will continue from where the previous run ended.

## Output

Results are saved to `chess960_results.json` with the following structure:
```json
{
  "position_index": {
    "backrank": ["R", "N", "B", "Q", "K", "B", "N", "R"],
    "fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "eval": 25
  }
}
```

- `eval`: Centipawn evaluation from Stockfish (null for mate scores)
- `backrank`: The back rank piece configuration
- `fen`: Full FEN string for the position

## Analysis Focus

The project specifically analyzes positions where not all pawns are fully defended, as these represent more interesting strategic starting positions compared to positions where every pawn is protected.
