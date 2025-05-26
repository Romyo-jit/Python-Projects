codes = ["bla", "br", "r", "o", 'y', "gree", "blu", "v", "grey", "w", "sp"]

def encrypt(data):
    enc_code = []
    ascis = []
    
    for wrd in data:
        for lett in wrd:
            ascis.append(ord(lett))
            ascis.append("sp")
            
    for i in ascis:
        if i == 'sp':
            enc_code.append(i)
            continue
        for dig in str(i):
            enc_code.append(codes[int(dig)])
    return ' '.join(enc_code)
    
def decrypt(data):
    letr = ''
    ascis = []
    val = ''
    
    for i in data:
        if i in codes:
            if i == 'sp':
                if val:
                    ascis.append(int(val))
                    val = ''
                continue
            val = val + str(codes.index(i))
    try:
        if val:
            ascis.append(int(val))
    except:
        pass
    
    for i in ascis:
        letr += chr(i)
    return letr

stri = input("Write string: ")
choi = int(input("Write 1 to encrypt, 2 to decrypt: "))

stri = stri.split(" ")

'''
stri = "br br r sp o r bla"
stri = "Helloguys"

choi = 1
'''

if choi == 1:
    print("Encrypted str: ")
    print(encrypt(stri))
elif choi == 2:
    print("Decrypted str: ")
    print(decrypt(stri))
else:
    print("Exitting....")
    exit()
