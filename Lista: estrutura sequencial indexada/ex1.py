def main():
   n = int(input("Insira um numero"))
   l = []
   while n > 0:
        num = float(input("Insira um numero: "))
        l.append(num)
        n -= 1
    
   for i in range(len(l) - 1, -1, -1):
        print(l[i])

#--------------------------------------------------
if __name__ == '__main__':
    main()
