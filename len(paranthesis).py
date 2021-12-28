def longestValidParentheses(s):
    stack = []
    max_len = 0
    temp_len = 0
    for char in s:
        if char == '(':
            stack.append(temp_len)
            temp_len = 0
        elif char == ')':
            if stack:
                temp_len += stack.pop() + 2
                max_len = max(temp_len, max_len)
            else:
                temp_len = 0

    return max_len