def lcs(A, B):
    """вычисление длины наибольшей общей подпоследовательности среди двух последовательностей"""
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    out = []
    for i in range (1, len(A) + 1):
        for j in range (1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])


    return F[-1][-1], out


A = "12346587541354897415768451578945315789431534675412316873513546"
B = "57894100831573431217800651234154312345531533510768688677215468700613"
print(len(A))
print(len(B))
l, posl = lcs(A, B)
print(l)
print(posl)
print(len(posl))