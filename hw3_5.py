def ternarySearchRec(alist, l, r, item):
    if (r >= l):
        midpoint1 = l + (r - l)//3
        midpoint2 = midpoint1 + (r - l)//3

        if alist[midpoint1] == item:
            return midpoint1

        if alist[midpoint1] > item:
            return midpoint2

        if alist[midpoint1] > item:
            return ternarySearchRec(alist, l, midpoint1-1, item)

        if alist[midpoint2] < item:
            return ternarySearchRec(alist, midpoint2+1, r, item)

        return ternarySearchRec(alist, midpoint1+1, midpoint2-1, item)

    return -1

alist = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

l = 0
r = 9
item = 50
x = ternarySearchRec(alist, l, r, item)
print("index of", item, "is", x)