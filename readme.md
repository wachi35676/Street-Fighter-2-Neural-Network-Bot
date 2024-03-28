# Street Fighter II Neural Network Bot

This is a Python implementation of an AI bot that plays the game Street Fighter II Turbo and competes against an opponent. The bot uses a combination of hard-coded rules and a trained neural network model to make decisions and execute actions during gameplay.

## Files

1. **bot.py**: This file contains the `Bot` class, which is the core of the bot's decision-making process. It includes methods for fighting against the opponent, running commands, and tracking the game state.

2. **player.py**: This file defines the `Player` class, which represents a player in the game. It contains information such as the player's character, health, coordinates, and button states.

3. **command.py**: This file defines the `Command` class, which represents the commands that the bot can execute during the game. It includes buttons and other game-related information.

4. **game_state.py**: This file defines the `GameState` class, which represents all the information received from the game at a single time instance, including player data, timer, and round status.

5. **controller.py**: This file serves as the main entry point for the program. It establishes a connection with the game, receives game state information, and sends commands to the game based on the bot's decisions.

6. **buttons.py**: This file defines the `Buttons` class, which represents a SNES gamepad used for playing Street Fighter, containing 12 boolean members representing individual buttons.

7. **training.py**: This file contains code for training a neural network model using data collected during gameplay. The trained model is used by the `Bot` class to make predictions and inform its decision-making process.

8. **model.h5**: This is the trained neural network model file, which is loaded and used by the `Bot` class during gameplay.

9. **game_data.csv**: This file contains the gameplay data collected during training, which is used by the `training.py` script to train the neural network model.

10. **capture_input.py**: This file provides a script to capture and record keyboard inputs, which can be used to generate training data for the bot.

11. **testing_model.py**: This file demonstrates how to load the trained neural network model and make predictions using new data.

## Usage

To run the project, you need to have the game running and connected to the appropriate ports (9999 for player 1, 10000 for player 2). Then, you can execute the `controller.py` file with the appropriate command-line argument to specify which player the bot will control:

```
python controller.py 1  # For player 1
python controller.py 2  # For player 2
```

During gameplay, the bot will make decisions based on the current game state and execute commands accordingly. The bot's behavior is defined in the `Bot` class, and it can be modified or extended as needed.

## Data Collection and Training

1. To collect training data, run the `capture_input.py` script and perform the desired actions in the game. The script will record your keyboard inputs in the `record.csv` file.

2. After collecting sufficient training data, use the `training.py` script to train the neural network model. The trained model will be saved as `model.h5`.

3. The `testing_model.py` script demonstrates how to load the trained model and make predictions using new data.

## Dependencies

This project requires the following Python libraries:

- NumPy
- TensorFlow
- Scikit-learn
- Pandas
- keyboard

Make sure to install these libraries before running the project.
