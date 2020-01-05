# TicTacToe
Simple TicTacToe game with AI, made with Pygame. 

## Usage
### Requirements 
This used *python3*. You need **pygame** and **numpy** to play this.

### Running
After cloning the repo, just run `python play.py` or `python3 play.py`.

### Playing
As of now, you have the first move. The AI will then make a move, and so on. The program will track who wins. When a game is over you can press *reset* so start over. *reset* can be pressed at any time to reset (when you know you will lose...).

You can change the difficulty of the AI by pressing the *Change AI* button. The AI has a difficulty between 1 and 5. You should beat it at 1, and maybe 2, but higher than that it is more or less unbeatable...


## Rules
Each player places three pieces on the board. When a player places the forth piece, the first he/she placed will disappear. Next time the second one will disappear. In this way a player will only have three pieces on the board, and the game will never draw.


## TODO

- Make the AI actually unbeatable...
- Different colors on pieces for AI and player
- Change the overall aesthetics
- Indicate to the player who won (it is now only printed in the consolse)
- More features, if possible...
