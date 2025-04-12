A = [64, 34, 25, 12, 22, 11, 90]
print(A)
m = 0

while m < len(A) - 1:
    for i in range(0, len(A)-1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
    m += 1

print(f'\n{A}')