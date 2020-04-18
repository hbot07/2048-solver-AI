# 2048-solver-AI  
If you have not played the game before, you may do so at [gabrielecirulli.github.io/2048](gabrielecirulli.github.io/2048) to get a sense of how the game works.  
An instance of the 2048-puzzle game is played on a 4×4 grid, with numbered tiles that slide in all four directions when a player moves them. Every turn, a new tile will randomly appear in an empty spot on the board, with a value of either 2 or 4. Per the input direction given by the player, all tiles on the grid slide as far as possible in that direction, until they either (1) collide with another tile, or (2) collide with the edge of the grid. If two tiles of the same number collide while moving, they will merge into a single tile, valued at the sum of the two original tiles that collided. The resulting tile cannot merge with another tile again in the same move.  
![image](https://user-images.githubusercontent.com/46916990/79671234-b194c680-81e6-11ea-9c53-98f486847eda.png)
![image](https://user-images.githubusercontent.com/46916990/79671251-c2453c80-81e6-11ea-8eeb-2e139e7bdd56.png)
![image](https://user-images.githubusercontent.com/46916990/79671254-c6715a00-81e6-11ea-89f1-2ccf7a052251.png)

## Skeleton Code    
GameManager.py. This is the driver program that loads your Computer AI and Player AI, and begins a game where they compete with each other. See below on how to execute this program.
Grid.py. This module defines the Grid object, along with some useful operations: move(), getAvailableCells(), insertTile(), and clone(), which you may use in your code. These are available to get you started, but they are by no means the most efficient methods available. If you wish to strive for better performance, feel free to ignore these and write your own helper methods in a separate file.
BaseAI.py. This is the base class for any AI component. All AIs inherit from this module, and implement the getMove() function, which takes a Grid object as parameter and returns a move (there are different "moves" for different AIs).
ComputerAI.py. This inherits from BaseAI. The getMove() function returns a computer action that is a tuple (x, y) indicating the place you want to place a tile.
BaseDisplayer.py and Displayer.py. These print the grid.

## Execution  
$ python3 GameManager_3.py

### Final Result:  
Results of 10 trials:  
Trials with max tile of 512: 10 %  
Trials with max tile of 1024: 50 %  
Trials with max tile of 2048: 30 %  
Trials with max tile of 4096: 10 %  

