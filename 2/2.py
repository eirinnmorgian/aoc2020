
def get_list():
	f = open('input.txt')
	strings = f.read()
	strlist = strings.split('\n')
	strlist.pop()

	rebuilt = []
	for s in strlist:
		unpacked = s.split(' ')
		rule = unpacked[0].split('-')

		obj = {'min': int(rule[0]), 'max': int(rule[1]), 'letter': unpacked[1][0], 'password': unpacked[2]}
		rebuilt.append(obj)

	return rebuilt


def first_check(rebuilt):

	valid = []
	for r in rebuilt:
		count = 0
		for p in r['password']:
			if p == r['letter']:
				count = count + 1
		if count >= r['min']:
			if count <= r['max']:
				valid.append(r)

	return valid


def second_check(rebuilt):
	
	valid = []
	for r in rebuilt:
		pos_a = r['min'] - 1
		pos_b = r['max'] - 1
		if r['password'][pos_a] == r['letter'] and r['password'][pos_b] != r['letter']:
			valid.append(r)
		elif r['password'][pos_b] == r['letter'] and r['password'][pos_a] != r['letter']:
			valid.append(r)

	return valid


def count_passwords(valid):
	
	count = 0
	for v in valid:
		count = count + 1

	return count


def engine():

	unsorted_objects = get_list()
	print 'All Objects:', count_passwords(unsorted_objects)
	
	first_valid = first_check(unsorted_objects)
	print 'FIRST COUNT:', count_passwords(first_valid)

	second_valid = second_check(unsorted_objects)
	print 'SECOND COUNT', count_passwords(second_valid)


engine()