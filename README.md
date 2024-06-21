# Bingo Recommender

**Terminal-based program to play Bingo efficiently with recommendation system**

**Board Generation:** 
   - At the start, you will be prompted to enter the size of the board (N).
   - The program generates a random N*N matrix with numbers ranging from 1 to N\*N.

### Playing the Game

1. **Enter Numbers to Strike:**
   - After the board is generated, you enter the numbers you want to strike off the board (one or more in a single line). This simulates the other player's turn.

2. **Displaying the Board:**
   - The program displays the updated matrix. Stricken numbers will be shown in red font.
   - The program also recommends the next number to strike, which is displayed in green font. This is your turn.

3. **Your Turn:**
   - You can either strike the recommended number or any other available number.

4. **Repeating Steps:**
   - The above steps repeat until you achieve a BINGO, at which point the program terminates.

### Recommendation System
  - The recommendation system analyzes the current state of the board to determine which number has the highest priority for striking.
  - Priority is based on the potential to complete rows, columns, or diagonals (achieving Bingo).
  - The system also calculates the number of connections (potential Bingos) for each available number.
  - Finally it recommends the one with the highest priority.
  - If multiple numbers have the same priority, the system evaluates additional factors such as the number of connections to decide the optimal number to recommend.

## Technologies Used

- **Language:** Python
- **Module:** Colorama (for colorizing terminal output)
