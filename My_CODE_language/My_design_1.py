codes = ["black", "brown", "red", "orange", 'yellow', "green", "blue", "violet", "grey", "white", "sp"]
codes_ano = ["bla", "br", "r", "o", 'y', "gree", "blu", "v", "grey", "w", "sp"]


def encrypt(data):
    enc_code = []
    ascis = []
    
    for wrd in data:
        for lett in wrd:
            ascis.append(ord(lett))
            ascis.append("sp")
        ascis.append('-')
    ascis.pop()
    
    for i in ascis:
        if i == 'sp' or i == '-':
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
        if i == '-':
            ascis.append(' ')
            continue
        if i in codes:
            if i == 'sp':
                ascis.append(int(val))
                val = ''
                continue
            val += str(codes.index(i))
    try:
        ascis.append(int(val))
    except:
        pass
        
    for i in ascis:
        if i == ' ':
            letr += i
            continue
        letr += chr(i)
    return letr

stri = input("Write string: ")
choi = int(input("Write 1 to encrypt, 2 to decrypt: "))
stri = stri.split(" ")

if choi == 1:
    print("Encrypted str: ")
    print(encrypt(stri))
elif choi == 2:
    print("Decrypted str: ")
    print(decrypt(stri))
else:
    print("Exitting....")
    exit()
