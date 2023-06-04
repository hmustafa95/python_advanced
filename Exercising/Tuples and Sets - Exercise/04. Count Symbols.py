text = input()
letters = {}

for idx in text:
    if idx not in letters:
        letters[idx] = 0
    letters[idx] += 1

for k, v in sorted(letters.items()):
    print(f"{k}: {v} time/s")