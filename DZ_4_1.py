
s = 0

def rect_paral_square(a, b, c):
	def rect_square(i, j):
		return i * j

	global s
	s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))


rect_paral_square(2, 4, 6)
print(s)
rect_paral_square(5, 8, 2)
print(s)
rect_paral_square(1, 6, 8)
print(s)