

def get_list():
	f = open('input.txt')
	strings = f.read()
	strlist = strings.split('\n')
	strlist.pop()

	intlist = []
	for n in strlist:
		ni = int(n)
		intlist.append(ni)

	return intlist


def first_answer():
	
	intlist = get_list()

	result = []
	no_result = []

	for n in intlist:
		for m in intlist:
			if n == m:
				pass
			elif n + m == 2020:
				result.append([n, m])
				break

			else:
				no_result.append([n, m])

	product = result[0][0] * result[0][1]

	return product

print 'first answer: ', first_answer()


def second_answer():

	intlist = get_list()

	def tester(i, j, k):
		if i + j + k == 2020:
			return [i, j, k]

	def get_numbers():
		for i in intlist:
			for j in intlist:
				for k in intlist:
					if tester(i, j, k):
						return tester(i, j, k)

	answer = get_numbers()
	return answer[0] * answer[1] * answer [2]

print 'second_answer: ', second_answer()




