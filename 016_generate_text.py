# Generate text
#!pip install transfomers
from transformers import pipeline

pipe = pipeline("text-generation", model="gpt2")
sentence = pipe("Hi, My name is Sally Ride, I am here", 
                max_length=100, 
                num_return_sequences=2)
for i in sentence:
  print(i["generated_text"])