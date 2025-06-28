def isbalance(s):
    stack = []
    bracketdict={
        '}' : '{',
        ']' : '[',
        ')' : '('
    }
    for b in s:
        if b in bracketdict and stack and bracketdict[b] == stack[-1]:
            stack.pop()
        else:
            stack.append(b)
    if stack:
        return("NO")
    else:
        return("YES")

s='{}'
ans=isbalance(s)
print(ans)
