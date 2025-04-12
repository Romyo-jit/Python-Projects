import threading

def printt(ret):
    if ret[0] == True:
        print("Prime")
    else:
        print("Not Prime")

def is_prime(n, r):
    for i in range(2, n):
        if n % i == 0:
            r.append(False)
            break
    if len(r) == 0:
        r.append(True)

num = int(input("Num :"))
ret1 = []
#ret2 = []
#t1 = threading.Thread(target=is_prime, args=[num, ret1])
#t1 = threading.Thread(target=is_prime, args=[int(num/2), ret1])
#t1.start()

is_prime(num, ret1)

printt(ret1)
