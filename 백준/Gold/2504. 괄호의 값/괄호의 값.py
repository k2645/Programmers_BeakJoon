import sys

def isValidBracket(bracketArray):
    stack = []
    for i in bracketArray:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return not stack

bracketArray = sys.stdin.readline().strip()
stack = []
ans = 0
i = 0
if isValidBracket(bracketArray):
    while i < len(bracketArray):
        chr = bracketArray[i]
        if chr == '(' or chr == '[':
            stack.append(chr)
            i += 1
        else:
            addAnswer = 1
            while i < len(bracketArray):
                chr = bracketArray[i]
                if stack and chr == ')' and stack[-1] == '(':
                    addAnswer *= 2
                elif stack and chr == ']' and stack[-1] == '[':
                    addAnswer *= 3
                else:
                    break
                stack.pop()
                i += 1
            for k in stack:
                if k == '(':
                    addAnswer *= 2
                else:
                    addAnswer *= 3
            ans += addAnswer
    print(ans)
else:
    print('0')