str_list = list(str(input()))

s = []
value = 1
score = 0
prev = None
for string in str_list:
    if string == "(" :
        s.append(string)
        value *= 2
    elif string == "[":
        s.append(string)
        value *= 3
    elif string == ")":
        if len(s) == 0  :
            score = 0
            break
        if prev =="(" :
            score += value
        elif s[-1] == "[":
            score = 0
            break
        s.pop()
        value //= 2
    else:
        if len(s) == 0:
            score = 0
            break
        if prev =="[":
            score += value
        elif s[-1] == "(":
            score = 0
            break
        s.pop()
        value //= 3
    prev = string
if s:
    score = 0
print(score)