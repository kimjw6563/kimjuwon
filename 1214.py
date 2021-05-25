a, b = map(int, input().split())
if b == 1 :
    print("31")
if b == 2 :
    if a%400 == 0:
        print("29")
    elif a%4==0:
        if(a%100!=0):
            print("29")
        else:
            print("28")
    else:
        print("28")
if b == 3 :
    print("30")
if b == 4 :
    print("31")
if b == 5 :
    print("30")
if b == 6 :
    print("31")
if b == 7 :
    print("30")
if b == 8 :
    print("31")
if b == 9 :
    print("30")       
if b == 10 :
    print("31")
if b == 11 :
    print("30")
if b == 12 :
    print("31")
