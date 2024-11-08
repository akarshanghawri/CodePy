def permute(s):
    if len(s) == 0:          # Empty case
        return []
    elif len(s) == 1:        # Single character case
        return [s]
    else:
        result = []           # Store permutations
        for i in range(len(s)):
            char = s[i]              # Current character
            remain = s[:i] + s[i+1:] # Remaining characters
            for perm in permute(remain):   # Permutations of remaining
                result.append(char + perm)   # Add current char to each
        return result

# Test
s = "roman"
print(permute(s))  
