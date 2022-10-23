text = input()

stack = []
for index in range(len(text)):
    char = text[index]
    if char == '(':
        stack.append(index)
    elif char == ')':
        final_bracket = stack.pop()
        sub_text = text[final_bracket:index + 1]
        print(sub_text)