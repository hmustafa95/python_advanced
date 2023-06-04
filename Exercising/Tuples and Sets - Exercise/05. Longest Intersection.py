number = int(input())
longest_intersection = {}

for idx in range(number):
    left_range, right_range = input().split()
    left_start_idx, left_end_idx = tuple(map(int, left_range.split(',')))
    right_start_idx, right_end_idx = tuple(map(int, right_range.split(',')))
    left_set = {num for num in range(left_start_idx, left_end_idx + 1)}
    right_set = {num for num in range(right_start_idx, right_end_idx + 1)}
    intersection = left_set & right_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str, {i for i in longest_intersection}))}] with length {len(longest_intersection)}")