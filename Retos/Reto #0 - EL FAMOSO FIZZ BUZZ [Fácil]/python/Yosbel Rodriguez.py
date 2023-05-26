## FIZZ BUZZ ###

for i in range(0,101):
    if i%3==0 and i%5==0:
        print(f"{i} FIZZ BUZZ")
    elif i%3==0:
        print(f"{i} FIZZ")
    elif i%5==0:
        print(f"{i} BUZZ")
    else:
        print(i)
