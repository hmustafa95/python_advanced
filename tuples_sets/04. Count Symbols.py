text = input()
letters = {}

for i in text:
    if i not in letters:
        letters[i] = 0
    letters[i] += 1

for i, v in sorted(letters.items()):
    print(f"{i}: {v} time/s")