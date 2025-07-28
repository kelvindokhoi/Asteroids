# Asteroids

A classic arcade-style game built with Python and Pygame. Navigate a spaceship through an asteroid field, shoot asteroids to break them into smaller pieces, and avoid collisions to survive as long as possible.

## Features
- Smooth spaceship controls for rotation, thrust, and shooting.
- Dynamic asteroid spawning and collision detection.
- Retro-style graphics and sound effects.
- Scoring system based on destroying asteroids.

## Prerequisites
- Python 3.12
- Pygame library
- Virtual environment (recommended)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/kelvindokhoi/Asteroids.git
   cd Asteroids
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game
1. Ensure the virtual environment is activated:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Run the main script:
   ```bash
   python main.py
   ```

## Controls
- **Left/Right Arrow Keys**: Rotate the spaceship.
- **Up Arrow Key**: Thrust forward.
- **Spacebar**: Shoot bullets.
- **Escape**: Quit the game.

## Project Structure
- `main.py`: Entry point for the game.
- `constants.py`: Game configuration and constants.
- `player.py`: Player spaceship logic.
- `asteroid.py`: Asteroid behavior and properties.
- `asteroidfield.py`: Manages asteroid spawning.
- `shot.py`: Bullet mechanics.
- `circleshape.py`: Base class for circular game objects.
- `requirements.txt`: Project dependencies.
- `venv/`: Virtual environment directory.

## Development
- The game was developed as part of a learning project for Python and Pygame.
- Git commits show progress from initializing Pygame and core files to completing the game logic (June 29-30, 2025).

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes. Issues can be reported on the [GitHub repository](https://github.com/kelvindokhoi/Asteroids).

## License
This project is licensed under the MIT License.