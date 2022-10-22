def ternarySearch(l, alist, item):
    r = len(alist)
    while r >= l:
        midpoint1 = l + (r-l) // 3
        midpoint2 = r - (r-l) // 3

        if item == alist[midpoint1]:
            return midpoint1
        if item == midpoint2:
            return midpoint2
        if item < alist[midpoint1]:
            r = midpoint1 - 1
        
        elif item > alist[midpoint2]:
            l = midpoint2 + 1

        else:
            l = midpoint1 + 1
            r = midpoint2 - 1
    return -1 


alist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l = 0
item = 50
x = ternarySearch(l, alist, item)
print("index of", item, "is", x)
