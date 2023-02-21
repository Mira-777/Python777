def rect_paral_square(a, b, c):
    s = 0

    def rect_square(i, j):
        nonlocal s
        s += i * j

    rect_square(a, b)
    rect_square(a, c)
    rect_square(b, c)

    return 2 * s
print(rect_paral_square(2, 4, 6))
print(rect_paral_square(5, 8, 2))
print(rect_paral_square(1, 6, 8))