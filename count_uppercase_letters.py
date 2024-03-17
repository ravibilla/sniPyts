# Count uppercase letters
count = 0 
with open("./files/sample.txt", "r") as f:
    text = f.read()
    for i in text:
        if i.isupper():
            count += 1
print(f"There are {count} uppercase letters")
