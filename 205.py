x = input()

if x.isdigit():
    print(f'{x}是數字')
elif x.isupper():
    print(f'{x}是大寫英文字母')
elif x.islower():
    print(f'{x}是小寫英文字母')
else:
    print(f'{x}是其他字元')