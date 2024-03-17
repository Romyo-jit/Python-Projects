
###COMPLETED###

import hashlib as hl
from dotmodule import Dot

alg = input("Write hashing algorithm name defalt SHA256: ")
my_hash = input("Enter hash: ")
print("\nMatching your hash with Dictionary", end = '')
Dot()

if alg == "":
    alg = "SHA256"
def main(alg):
    def found(my_hash, has_pas):
        if my_hash == has_pas:
            print('\nMatched - Your hash matches to', pas.decode(),'\n')
            exit()
            
    with open('rockyou.txt', 'rb') as f:
        for pas in f:
            has = hl.new(alg)
            myhas = pas.strip().strip(b'\n')
            has.update(myhas)
            has_pas = has.hexdigest()
            found(my_hash, has_pas)
main(alg)
print('\nPassword is not in the Dictionary.')
exit()