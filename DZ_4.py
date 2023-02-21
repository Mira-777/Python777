def rect_paral_square(a, b, c):
	def rect_square(i, j):
		return i * j

	s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
	return s	


print(rect_paral_square(2, 4, 6))
print(rect_paral_square(5, 8, 2))
print(rect_paral_square(1, 6, 8))
