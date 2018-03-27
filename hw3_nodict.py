text = input("Please type anything:\n")

for ch in set(text):
    print(ch, text.count(ch))
