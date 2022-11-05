def lcs(A, B):
    """вычисление длины наибольшей общей подпоследовательности среди двух последовательностей (A, B)
       out - наибольшая общая подпоследовательнсоть
    """
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range (1, len(A) + 1):
        for j in range (1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    out = []
    for i in range(len(F), 0, -1):
        for j in range(len(F[0]), 0, -1):
            if

    return F[-1][-1], F


A = "1234658754135489741576"
B = "5789410083157343121780065123415431"
l, posl = lcs(A, B)
print(l)
for row in posl:
    for elem in row:
        print(str(elem).ljust(3), end=" ")
    print()
