def combine_duplicate_characters(s):
    stack = []
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])
    
    return ''.join([c for c, count in stack if count == 1])

print(combine_duplicate_characters("aaabbbacccaaa"))
