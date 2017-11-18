def checker(str):
    f=s=b=g=0
    for i in str:
        if i == "(":
            b += 1
        elif i == ")":
            count -= 1
        elif i== '{':
            f += 1
        elif i == '}':
            f -= 1
        elif i == '[':
            s += 1
        elif i == ']':
            s-=1
        elif i == '<':
            g += 1
        elif i == '>':
            g -= 1
    if b and g and s and f == 0:
        print('matched')
    else:
        print('not matched')
a = input('expression:')
print(checker(a))