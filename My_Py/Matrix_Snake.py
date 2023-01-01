import numpy
class Snakes:
    """Класс способов получения змейки в матрице"""
    import numpy
    def __init__(self, mx, n):
        self._mx = mx
        self._n = n
    def np_snake(mx, n, k=1, sm=0):
        """mx - массив numpy
           n - текущая сторона заполняемого квадрата
           k - заполняемый номер
           sm - номер итерации, смещение
       """
        for _ in range(4):
            if k == len(mx) ** 2:
                mx[sm, sm] = k
                return
            mx[sm,sm:sm+n-1] = range(k, k + n - 1)
            k += n - 1
            mx[:] = numpy.rot90(mx)
        Snakes.np_snake(mx, n - 2, k, sm + 1)
        while mx[0, 0] != 1:
            mx[:] = numpy.rot90(mx)
        return




N = int(input("Ввести размер поля: "))
mx = numpy.zeros((N, N), dtype=int)
Snakes.np_snake(mx, N)
for row in mx:
    for elem in row:
        print(str(elem).ljust(3), end=" ")
    print()
