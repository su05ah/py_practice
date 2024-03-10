print("구구단을 외우자! 구구단을 외우자!")
x = input("몇단을 외워볼까~?")
x = int(x)

def multification(a):
    k = a * x
    return k

for m in range(1,10):
    print(x,"단은",x,"x",m,"=",multification(m))





    
