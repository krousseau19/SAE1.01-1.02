# Terminal Games Collection

This small Python project provides a collection of terminal games implemented for learning and fun. The program bundles four games with a unified menu and persistent player statistics saved to a binary file.

## Included games
- Guessing Game (Devinette)
  - One player chooses a secret number, the other tries to guess it.
  - Supports three interval sizes: [1–100], [1–1,000], [1–10,000].
  - Machines (AI) can play at three difficulties: random, intermediate (mix), and optimal (binary search).

- Matches (Allumettes)
  - Classic take-1-to-3 matches game starting from 20 matches.
  - Last player to take the final match loses; AIs implement random / intermediate / optimal strategies.

- Tic-Tac-Toe (Morpion)
  - 3×3 board, two players alternate placing X and O.
  - AI: random, intermediate (mix), or optimal (looks for wins/blocks, center, corners, edges).

- Connect Four (Puissance 4)
  - 7 columns × 6 rows grid, four-in-a-row wins.
  - AI: random, intermediate (mix), or optimal (checks winning moves, blocking moves, priority order).

## Main features
- Unified text-based menu with ASCII art and interactive prompts.
- Game modes:
  1. Human vs Human
  2. Human vs Machine
  3. Machine vs Machine
- Difficulty levels for machine players: Easy, Intermediate, Hard.
- Persistent player statistics and leaderboards stored in `Data/data.sav` (pickle binary file).

## Quick start
1. Make sure you have Python 3.10+ (project was developed with Python 3.11).
2. Run the main program from the `Programmes` folder:

```bash
python3 principal.py
```

Follow the on-screen menu to select mode, difficulty and which game to play.

## Files and responsibilities
- `principal.py` — main program and menu orchestration. Handles mode/difficulty selection and saving/loading player data.
- `ressource.py` — helper module: `Joueur` class, menu helpers, player creation, save/load (pickle) and leaderboard functions.
- `devinette.py` — guessing game implementation and AI strategies.
- `allumette.py` — matches game implementation and AI strategies.
- `morpion.py` — tic-tac-toe implementation, board display, AI strategies.
- `puissance4.py` — connect four implementation, grid handling and AIs.
- `Data/data.sav` — binary file used to store player records. The repository includes a `Data/` folder with this file.

## Player data and persistence
- Player records (high scores, games played/won) are pickled into `Data/data.sav`.
- When creating a human player, the program checks for an existing saved record and loads it if present.

## Controls and interaction
- Most prompts expect integer choices (menu selections, column numbers, etc.). Input validation is implemented, and invalid entries will prompt an error and a retry.
- Tic-tac-toe uses coordinates like `A1`, `B3` (letter then digit).

## Notes, limitations and tips
- The project is intended as a terminal/learning project; no external dependencies are required beyond the Python standard library.
- The pickle file (`Data/data.sav`) must be writable by the program to save stats. If you move the project, keep the `Data` folder alongside the scripts or update paths in `ressource.py`.
- Some AI implementations use simple heuristics; they are not perfect but demonstrate strategy tiers.
- The code uses ANSI escape sequences for colored terminal output — behavior may vary across terminals.


