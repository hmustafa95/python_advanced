from collections import deque

eggs = deque(map(int, input().split(', ')))
papers = list(map(int, input().split(', ')))
box_size = 50
boxes_filled = 0

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    paper = papers.pop()
    result = egg + paper
    if result <= box_size:
        boxes_filled += 1

if boxes_filled >= 1:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")
