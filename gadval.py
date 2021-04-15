def g():
    a = int(input('n: '))
    b = int(input('m: '))
    for i in range(1, a+1):
        print()
        for j in range(1, b+1):
            print(i * j , end=' ')
print(g())