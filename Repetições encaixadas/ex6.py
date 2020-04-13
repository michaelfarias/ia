
def main():
    n = int(input("Insira um numero (n >0): "))
    i = 1

    while i <= n:
        j = 1
        while j <= n:
            print(j,"+", i, " = ", i+j, end ="\t")
            j += 1
        print()
        i += 1

    i = 1
    print()


    while i <= n:
        j = 1
        while j <= n:
            print(i,"-", j, " = ", i - j, end ="\t")
            j += 1
        print()
        i += 1

    i = 1
    print()

    while i <= n:
        j = 1
        while j <= n:
            print(j,"*", i, " = ", i*j, end ="\t")
            j += 1
        print()
        i += 1

    i = 1
    print()

    while i <= n:
        j = 1
        while j <= n:
            print(i,"/", j, " = ", j/i, end ="\t")
            j += 1
        print()
        i += 1
#--------------------------------------------------
if __name__ == '__main__':
    main()


