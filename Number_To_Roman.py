def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number = number % num[i]
        while div:
            print(rom[i], end = "")
            div = div - 1
        i = i - 1
 
number = int(input('Enter num :'))
print("Roman value is:", end = " ")
printRoman(number)