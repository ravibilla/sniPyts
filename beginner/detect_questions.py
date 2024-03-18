# Detect questions
#!pip install -U nltk
from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where", 
                  "name", "is", "how", "do", "does",
                  "which", "are", "could", "would", 
                  "should", "has", "have", "whom", "whose", "don't"]

question = input("Input a sentence: ")
question = question.lower()
tokens = word_tokenize(question)

if any(word in tokens for word in question_words):
    print("This is a quesiton!")
else:
    print("This is not a question!")