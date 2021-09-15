"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):

	if right >= left:
		middle = (right + left) // 2

		if mylist[middle] == key:
			return middle

		elif mylist[middle] > key:
			return _binary_search(mylist, key, left, middle - 1)

		else:
			return _binary_search(mylist, key, middle + 1, right)

	else:
		return -1


def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,2,3,4,5], 4) == 3
	assert binary_search([1,2,3,4,5], 3) == 2



def time_search(search_fn, mylist, key):

	start = time.time()

	search_fn(mylist, key)

	end = time.time()

	milliseconds = (end - start) * 1000

	return milliseconds


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

	tuples = []

	for j in sizes:

		tuple = []

		list1 = []
		for i in range(int(j)):
			list1.append(i)

		linear1time = time_search(linear_search, list1, -1)
		binary1time = time_search(binary_search, list1, -1)

		tuple.append(int(j))
		tuple.append(linear1time)
		tuple.append(binary1time)

		tuples.append(tuple)


	print_results(tuples)


def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

compare_search()
