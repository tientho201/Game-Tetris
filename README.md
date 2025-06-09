# Tetris Game

A classic Tetris game implemented in Python using the Pygame library.

## Features

- Simple and user-friendly graphical interface
- Score system based on cleared lines
- Next block preview
- Pause functionality
- Game over when no more blocks can be placed
- Block rotation and movement support

## Installation

1. Make sure you have Python (version 3.x) installed
2. Install the Pygame library:
```bash
pip install pygame
```

## How to Play

1. Run the game:
```bash
python src/main.py
```

2. Controls:
- Left/Right Arrow: Move block left/right
- Down Arrow: Move block down faster
- Up Arrow: Rotate block
- P key: Pause/Resume game
- R key: Restart game when game over

## Game Rules

- Blocks automatically fall down
- Players can move and rotate blocks
- When a line is completely filled, it disappears and the player earns points
- Game ends when no more blocks can be placed

## Project Structure

```
src/
├── main.py      # Main file to run the game
├── gui.py       # Handles interface and input
├── board.py     # Manages game board
├── block.py     # Defines blocks
└── constants.py # Constants and configuration
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
