import sys

print("              HANGMAN             ")

def hangman(l, hint):
    # Replace character in word with "_"
    def replace(l, x):
        val = l.index(x)
        l[val] = "_"
        return l

    # Function to get unique characters from the list
    def unique(l):
        l1 = []
        for i in l:
            if i not in l1:
                l1.append(i)
            else:
                continue
        return l1

    print()
    print("All the characters:")
    char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print(char)
    print()
    
    xs = []  # List to store guessed characters
    k = "_ "  # Placeholder for the word
    j = 0  # Index for words
    newl = ['_'] * len(l[j])  # List with underscores for the word
    word = list(l[j])  # Convert word to list for easy modification
    word2 = list(l[j])  # Store original word for comparison
    
    print("HINT:", hint[0])  # Display hint
    print(f"Length of the word: {len(l[j])}")  # Display word length
    print(k * len(l[j]))  # Display underscores as placeholders
    j += 1

    y = 0  # Counter for correct guesses
    s = 6  # Number of attempts

    while True:
        x = input("Enter character: ")

        if x in xs:  # Check if the character was already guessed
            print("You guessed it already")
            continue

        elif x not in word:  # If character is not in word
            s -= 1  # Decrease attempts
            for i in newl:
                print(i, end=" ")
            print()
            print(f"Sorry {x.upper()} is not in the word")
            print(f"Attempts left: {s}")
            print()
            print(replace(char, x.upper()))  # Update the character list for guessed letters

        else:
            y += 1  # Increase correct guesses
            print("You guessed it correctly")
            if word.count(x) > 1:  # If the letter appears more than once
                for i in range(word.count(x)):
                    newl[word.index(x)] = x
                    word[word.index(x)] = "_"
            else:
                newl[word.index(x)] = x  # Update the list with the correct guess

            for i in newl:
                print(i, end=" ")
            print()

        xs.append(x)  # Add guessed letter to the list

        if s == 0:  # Check if attempts are over
            print("You lost!")
            print("The word was:", word)
            sys.exit()

        elif y == len(unique(word2)):  # Check if all characters have been guessed correctly
            print("You Won!")
            break

        else:
            continue  # Continue the game

# Start of the game
s = 1
d = {
    "puma": "Shoe Brand", "atlantic": "Ocean",
    "ronaldo": "Footballer", "chemistry": "Subject",
    "giraffe": "Animal", "meghalaya": "Indian state",
    "swimming": "Sport", "strawberry": "Fruit",
    "vietnam": "Country"
}

for i, j in d.items():
    print("Level:", s)
    hangman([i], [j])  # Start hangman for each word
    s += 1
    if i == "vietnam":
        print("Congratulations!!!")
        print("You have completed all the levels.")
