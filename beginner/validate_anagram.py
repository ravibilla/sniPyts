# Validate anagram
def validate_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return(sorted(word1) == sorted(word2))

print(validate_anagram("cinema", "iceman"))
print(validate_anagram("cool", "loco"))
print(validate_anagram("men", "women"))