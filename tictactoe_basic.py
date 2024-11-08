# Initialize the Tic-Tac-Toe board as a 3x3 grid with empty spots
l = [["___", "___", "___"],
     ["___", "___", "___"],
     ["___", "___", "___"]]

# List representing the two players ("O" for Player 1 and "X" for Player 2)
l1 = [" O ", " X "]

# Print game introduction and instructions
print("# tic-tac-toe")
print("The first player will play as \"O\" ")
print("The second player will play as \"X\" ")
print("The format to play is -")

# Display the initial empty board
for i in range(3):
    for j in range(3):
        print(l[i][j], end="  ")
    print()

# Start the game loop
while True:
    # Player 1's turn
    a = int(input("Enter row number for 1st player: "))
    b = int(input("Enter column number for 1st player: "))  

    # Update the board with Player 1's move
    l[a].pop(b)
    l[a].insert(b, l1[0])

    # Print the updated board after Player 1's move
    for i in range(3):
        for j in range(3):
            print(l[i][j], end="  ")
        print()
    
    # Check if Player 1 has won (horizontal, vertical, or diagonal)
    if (" O " == l[0][0] and " O " == l[0][1] and " O " == l[0][2]) or \
       (" O " == l[1][0] and " O " == l[1][1] and " O " == l[1][2]) or \
       (" O " == l[2][0] and " O " == l[2][1] and " O " == l[2][2]) or \
       (" O " == l[0][0] and " O " == l[1][0] and " O " == l[2][0]) or \
       (" O " == l[0][1] and " O " == l[1][1] and " O " == l[2][1]) or \
       (" O " == l[0][2] and " O " == l[1][2] and " O " == l[2][2]) or \
       (" O " == l[0][0] and " O " == l[1][1] and " O " == l[2][2]) or \
       (" O " == l[0][2] and " O " == l[1][1] and " O " == l[2][0]):
        print("Player 1 you won!!!")
        break

    # Player 2's turn
    c = int(input("Enter row number for 2nd player: "))
    d = int(input("Enter column number for 2nd player: "))  

    # Update the board with Player 2's move
    l[c].pop(d)
    l[c].insert(d, l1[1])

    # Print the updated board after Player 2's move
    for i in range(3):
        for j in range(3):
            print(l[i][j], end="  ")
        print()

    # Check if Player 2 has won (horizontal, vertical, or diagonal)
    if (" X " == l[0][0] and " X " == l[0][1] and " X " == l[0][2]) or \
       (" X " == l[1][0] and " X " == l[1][1] and " X " == l[1][2]) or \
       (" X " == l[2][0] and " X " == l[2][1] and " X " == l[2][2]) or \
       (" X " == l[0][0] and " X " == l[1][0] and " X " == l[2][0]) or \
       (" X " == l[0][1] and " X " == l[1][1] and " X " == l[2][1]) or \
       (" X " == l[0][2] and " X " == l[1][2] and " X " == l[2][2]) or \
       (" X " == l[0][0] and " X " == l[1][1] and " X " == l[2][2]) or \
       (" X " == l[0][2] and " X " == l[1][1] and " X " == l[2][0]):
        print("Player 2 you won!!!")
        break
