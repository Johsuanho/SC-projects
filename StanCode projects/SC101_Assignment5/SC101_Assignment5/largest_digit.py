"""
File: largest_digit.py
Name: Johsuan
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number that was entered.
	:return: int, the digit with biggest value in n.
	"""
	max = 0
	if n < 0:
		n = -n
	return find_max(n, max)


def find_max(n, max):
	k = n % 10
	if n//10 == 0:
		if k > max:
			max = k
		return max
	else:
		if k > max:
			max = k
		return find_max(n//10, max)










if __name__ == '__main__':
	main()
