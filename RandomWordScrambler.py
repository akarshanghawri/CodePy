from random import randint

def something(str):
    # Split the input sentence into words
    words = str.split()
    jumbled_str = ""

    for word in words:
        f_letter = word[0]  # First letter remains unchanged
        l_letter = word[-1]  # Last letter remains unchanged
        rest = word[1:-1]  # Middle portion of the word to be jumbled
        length_rest = len(rest)
        new_word = ""
        uniquenum = []  # To keep track of used indices for randomization

        # Randomly shuffle the middle characters
        while length_rest != 0:
            random_num = randint(0, len(rest) - 1)
            if random_num not in uniquenum:  # Avoid repeating characters
                new_word += rest[random_num]
                length_rest -= 1 
                uniquenum.append(random_num)

        # Reconstruct the jumbled word and add it to the result
        jumbled_word = f_letter + new_word + l_letter
        jumbled_str += jumbled_word + " "

    return jumbled_str  # Return the final jumbled sentence

# Input sentence
str = "Creativity thrives when challenges inspire innovative solutions for unexpected opportunities"

# Display the result
print(f"Original sentence : {str}\n\nJumbled sentence : {something(str)}")
