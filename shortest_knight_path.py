def knight(p1, p2):
    """
    Determines the minimum number of moves required for a knight 
    to move from position p1 to position p2 on a chessboard.
    
    Arguments:
        p1: str, starting position (e.g., "a1")
        p2: str, target position (e.g., "h8")
    
    Return:
        int, minimum moves required
    """
    def find_moves(p1):
        """
        Determines all possible knight moves from a given position.

        Argument:
            p1: str - The current position of the knight.

        Returns:
            list - A list of strings representing all valid moves.
        """

        # Chessboard column labels
        notations_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        alpha = p1[0]  # Extract the letter part (column)
        num = int(p1[1])  # Extract the number part (row)

        # Find the index of the current column
        for i in range(1, len(notations_alpha) + 1):
            if notations_alpha[i - 1] == alpha:
                # Determine possible left and right movements
                move_right = notations_alpha[i: i + 2]  
                move_left = notations_alpha[:i - 1][-2:]  
                move_alpha = move_left + move_right  # Combine possible moves
                break

        moves = []  # List to store valid moves
        loop = 1  # Keeps track of movement type

        # Identify the column before the current position
        before = notations_alpha[notations_alpha.index(alpha) - 1] if notations_alpha.index(alpha) > 0 else None

        for char in move_alpha:
            # Handle cases where move_left is empty (edge of board)
            if move_left == []:
                if num - 2 > 0 and loop == 1:
                    moves.append(char + str(num - 2))
                if num + 2 <= 8 and loop == 1:
                    moves.append(char + str(num + 2))
                if num - 1 > 0 and loop == 2:
                    moves.append(char + str(num - 1))
                if num + 1 <= 8 and loop == 2:
                    moves.append(char + str(num + 1))

            # Handle cases where only one left move is available
            elif len(move_left) == 1:
                if before in move_left:
                    if num - 2 > 0 and (loop == 1 or loop == 2):
                        moves.append(char + str(num - 2))
                    if num + 2 <= 8 and (loop == 1 or loop == 2):
                        moves.append(char + str(num + 2))
                    if num - 1 > 0 and loop == 3:
                        moves.append(char + str(num - 1))
                    if num + 1 <= 8 and loop == 3:
                        moves.append(char + str(num + 1))

            # Handle cases where both left moves are available
            else:
                if num - 2 > 0 and (loop == 2 or loop == 3):
                    moves.append(char + str(num - 2))
                if num + 2 <= 8 and (loop == 2 or loop == 3):
                    moves.append(char + str(num + 2))
                if num - 1 > 0 and (loop == 1 or loop == 4):
                    moves.append(char + str(num - 1))
                if num + 1 <= 8 and (loop == 1 or loop == 4):
                    moves.append(char + str(num + 1))

            loop += 1  # Increment loop counter

        return moves  # Return all valid knight moves

    def recursive(moves, p2, rep=1):
        """
        Recursively finds the minimum number of moves required to reach p2.

        Arguments:
            moves: list - List of possible knight positions in the current step.
            p2: str - Target position.
            rep: int - Counter for the number of recursive calls (moves taken).

        Returns:
            int - Minimum number of moves required to reach p2.
        """

        # If the target position is in the current possible moves, return the count
        if p2 in moves:
            return rep
        else:
            moves_2 = []  # Store the next set of possible moves

            # Iterate over all possible current moves to generate new moves
            for i in moves:
                moves_2 += find_moves(i)  # Add new moves

            # Recursively check the new moves with incremented step count
            return recursive(moves_2, p2, rep + 1)

    # Initial knight moves from p1
    moves = find_moves(p1)
    
    # Begin recursive search
    return recursive(moves, p2, 1)