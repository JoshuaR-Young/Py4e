def count(word, letter):

    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

# Example usage
word = 'banana'
letter = 'a'
print(f"The letter '{letter}' appears {count(word, letter)} times in the word '{word}'.")
