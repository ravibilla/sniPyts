# Check spelling
#!pip install pyspellchecker
from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter a word: ")
if word in corrector:
    print(f"Spelling of {word} is correct!")
else: 
    correct_word = corrector.correction(word)
    print(f"Correct spelling of {word} is: {correct_word}")
