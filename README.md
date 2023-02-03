# Tic-Tac-Toe with ai
## Tic-Tac-Toe game, that you can play against your computer. The computer have two levels of difficulty — easy and medium.

The top-left cell will have the coordinates (1, 1) and the bottom-right cell will have the coordinates (3, 3), as shown in this table:

(1, 1) (1, 2) (1, 3) <br>
(2, 1) (2, 2) (2, 3) <br>
(3, 1) (3, 2) (3, 3) <br>

The program ask the user to enter the coordinates of the cell where they want to make a move.

The program work in the following way:

1. Request command fron user. It can be 'exit' to quit the game or 'start' with 2 params of players: 'user' for human and 'easy' and 'medium' for ai.
1. Output the specified 3x3 table before the user makes a move.
2. Request that the user enters the coordinates of the move they wish to make.
3. The user then inputs two numbers representing the cell in which they wish to place their X or O. The game always starts with X.
4. Analyze the user input and show messages in the following situations:
• This cell is occupied! Choose another one! — if the cell is not empty;
• You should enter numbers! — if the user tries to enter letters or symbols instead of numbers;
• Coordinates should be from 1 to 3! — if the user attempts to enter coordinates outside of the table's range.
Display the table again with the user's most recent move included.
Output the state of the game.

## Example
```bash
Input command: > start easy
Bad parameters!

Input command: > start easy user
---------
|       |
|       |
|       |
---------
Making move level "easy"
---------
|       |
|       |
|     X |
---------
Enter the coordinates: > 2 2
---------
|       |
|   O   |
|     X |
---------
Making move level "easy"
---------
|   X   |
|   O   |
|     X |
---------
Enter the coordinates: > 3 1
---------
|   X   |
|   O   |
| O   X |
---------
Making move level "easy"
---------
|   X X |
|   O   |
| O   X |
---------
Enter the coordinates: > 2 3
---------
|   X X |
|   O O |
| O   X |
---------
Making move level "easy"
---------
| X X X |
|   O O |
| O   X |
---------
X wins
```
