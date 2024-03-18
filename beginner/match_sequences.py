# Match sequences
from difflib import SequenceMatcher

seq1 = "My name is Ravi Billa"
seq2 = "Hi, my name is Ravi Billa"
seq3 = "I am learning how to program in Python"
score_1_2 = SequenceMatcher(None, seq1, seq2).ratio()
score_2_3 = SequenceMatcher(None, seq2, seq3).ratio()

print(f"seq1 and seq2 are {score_1_2 * 100: .2f} % similar")
print(f"seq2 and seq3 are {score_2_3 * 100: .2f} % similar")