import hashlib as hl

cpass=input("Write pass: ")
alg = input("Write Hashing Algorithm Defalt SHA256: ")
if alg == '':
    alg = 'SHA256'
h = hl.new(alg)
h.update(cpass.encode())
#h.update(a)

print ("Hex form :\n" + h.hexdigest())
#print()