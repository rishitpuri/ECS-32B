def bubblesort(lst):
	n = len(lst)
	for i in range(n):
		for j in range(n-i-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]


lst = [9, 8, 3, 1, 5]
print ('Before: {}'.format(lst))
bubblesort(lst)
print ('After: {}'.format(lst))