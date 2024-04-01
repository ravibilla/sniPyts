# Check palindrome words
def check_palindrome_words(sentence):
    for i in (",.'?!/><}{{}}'"):
        sentence.replace(i, ' ')
    palindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    
    return palindrome

sentence = input("Enter a sentence: ")
print(check_palindrome_words(sentence))