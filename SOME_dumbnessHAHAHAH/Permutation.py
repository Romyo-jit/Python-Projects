import math

def main():
    try:
        n = int(input("Enter the number of elements('n') :"))
        r = int(input("Enter the the number of selected objects arranged in a certain order('r') :"))
    except:
        print("Input error..")
        exit()
    
    print(f"\nP(n, r) = {math.perm(n, r)}")
    
main()