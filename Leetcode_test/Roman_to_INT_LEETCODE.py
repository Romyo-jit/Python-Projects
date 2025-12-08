

numlist = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

num = "XC"
sum = 0
prev = None

for i in num:
    match prev:
        case 'I':
            if i == 'V' or i == 'X':
                sum = sum + numlist[i] - 2
            else:
                sum = sum + numlist[i] 
        case 'X':
            if i == 'L' or i == 'C':
                sum = sum + numlist[i] - 20
            else:
                sum = sum + numlist[i] 
        case 'C':
            if i == 'D' or i == 'M':
                sum = sum + numlist[i] - 200
            else:
                sum = sum + numlist[i]
        case _:
            sum = sum + numlist[i] 
    prev = i

print(sum)