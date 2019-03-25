## Game Description :video_game:
Contributors:
- Daniil Oliynyk
- Arshia Gharai
- Joo Hyun Jeon
- Jathavan Sellathurai
- Gabriel El Haddad

Our game is a cloned version of the board game Connect 4 that we called Line Up 4. The game was developed using Python3 and the Pygame library.

## Screenshots
[[Back to top]](https://github.com/daniil-oliynyk/csc290gadjj#csc290[gadjj])

| ![Screen 1](https://github.com/daniil-oliynyk/csc290gadjj/blob/master/screenshots/Screen%20Shot%202019-03-18%20at%203.41.44%20PM.png)| ![Screen 2](https://github.com/daniil-oliynyk/csc290gadjj/blob/master/screenshots/Screen%20Shot%202019-03-18%20at%203.42.41%20PM.png)|
| ![Screen 3](https://github.com/daniil-oliynyk/csc290gadjj/blob/master/screenshots/Screen%20Shot%202019-03-18%20at%203.43.06%20PM.png)| ![Screen 4](https://github.com/daniil-oliynyk/csc290gadjj/blob/master/screenshots/NewEndScreen.png)|

## How to play (Features) :star:
[[Back to top]](https://github.com/daniil-oliynyk/csc290gadjj#csc290[gadjj])

- The start screen contains Start, Quit and Help buttons.
  - Click on the start button to start playing Line Up 4
  - Click on the Quit button to leave the game and close the window
  - Click on the Help button for the instructions of the game and to learn how to play if you don't already know
- The main game screen conatain a 7x6 grid where the actual game will take place
  - The game will go on untill either a player wins or the board gets filled up
  - In order for a player to win, they have to line up 4 disks vertically, horizontally or diogonally
- The last screen pops when either a player has won or the board is filled up
  - This screen conatins a message "Game Over!" followed by the player that won the game
  - Click on the RETURN TO MAIN to go back to the main menu


## Installation Instructions :floppy_disk: 
### For `Windows` 
- :arrow_down: [Download the installer](https://github.com/daniil-oliynyk/csc290gadjj/releases/tag/v1.0.0)
### For `Ubuntu/Debian`
- Have python3 and pygame installed
```bash
$ sudo apt-get install python3 
$ sudo apt-get install python-pygame
```
- Clone the repo and run python
```bash
$ git clone https://github.com/daniil-oliynyk/csc290gadjj.git
$ cd csc290gadjj/src
$ python3 Main.py
```
### For `MacOS`
- Have python3 and pygame installed
```bash
$ brew install python3
$ sudo easy_install pip
```
- Clone the repo and run python
```bash
$ git clone https://github.com/daniil-oliynyk/csc290gadjj.git
$ cd csc290gadjj/src
$ python3 Main.py
```

## Project Directory and Code Structure :file_folder: 

### Directory Structure
There is one main directory for our project, the `src/` directory. All of the source code can be found in it. The code is designed and structed around Model-View-Controller design patter for clearer design and easier expandability.

### Code Structure
- `Main.py` contains the main game loop which initializes our Model, View and Controller
- The `Model.py` class is the model of the game board. There are also "sub models" like the `Disc.py` file which contains the representation of the discs that the players use. The two interact as if they are one
- The `View.py` contains the start screen and the main game screen
    -`def display(self):` displays the main game screen and the end game screen when needed
    - `def start_screen(self):` is called on to display the start menu for the game. It uses our custom `Button.py` button models. The start screen can be expanded upon by simply adding more buttons in the `init` method and handling the mouse clicks to provide additional functionality

For Example:
 ```python
 if self.start_buttons[n].is_over(clicked): #check the quit game button
    self.start_buttons[n].color = (x,x,x)
    if self.pygame.mouse.get_pressed()[0]: #check for click
        #do something
 ```
 
For additional functionailty such as a Pause screen, follow the way the start screen is designed and implemented

- The `Controller.py` handles all input that the game recieves and some custom such as replay option in the game over screens.
    - Done through additional methods that are invoked when, for example, the game over flag is raised in the game loop.

To add custom key handlers (like `def go_replay_handler(self):`):
```python
for event in self.pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_()#(refer to pygame documentation for keys):
            return True
return False

```


## License and author info
[[Back to top]](https://github.com/daniil-oliynyk/csc290gadjj#csc290[gadjj])

- The license is made by Arshia Gharai under MIT License (a copy of the license can be found at https://github.com/daniil-oliynyk/csc290gadjj/blob/master/LICENSE.txt)
- The screenshots were all taken from our own game and were not taken from any other website
