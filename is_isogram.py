def is_isogram(word):
    if type(word) != str or word.strip() == "" :
        return False
    
    freq = {}
    for char in word.lower():
        if char.isalpha():  
            if char in freq:
                freq[char] += 1  
            else:
                freq[char] = 1
    
    # Return True if all character frequencies are 1 (isogram)
    return len(set(freq.values())) == 1 