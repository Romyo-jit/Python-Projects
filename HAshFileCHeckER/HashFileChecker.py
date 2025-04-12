#Completed
import hashlib as hl

def main():
    file_name, hash_algorithm, main_hash = user_input()
    info = checking(file_name, hash_algorithm, main_hash)
    print(info)

def user_input():
    print("***FILE HAVE TO BE IN SAME FOLDER***")
    file_name = input("Enter the name of your file :")
    while True:
        hash_algorithm = input("Enter the Hash Algorithm--\n\n1>SHA256\t2>SHA512\n3>MD5\t\t4>SHA1\n\n-->")
        match hash_algorithm:
            case '1':
                hash_algorithm = "SHA256"
                break
            case '2':
                hash_algorithm = "SHA512"
                break
            case '3':
                hash_algorithm = "MD5"
                break
            case '4':
                hash_algorithm = "SHA1"
                break
            case _:
                print("Wrong input. Retry..\n")
                continue
    main_hash = input("Enter your Hash :")
    return file_name, hash_algorithm, main_hash

def checking(name, algorithm, hash):
    with open(name, 'rb') as f:
        data_hash = hl.file_digest(f,algorithm).hexdigest()
    if data_hash == hash:
        return 'Matched'
    else:
        return 'Not Matched'

main()