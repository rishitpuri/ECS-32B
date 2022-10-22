def mergeSort(lst):
    print("splitting ",lst)
    if len(lst)>1:
        mid = len(lst)//2
        l = lst[:mid]
        r = lst[mid:]

        mergeSort(l)
        mergeSort(r)
        i=0
        j=0
        n=0       
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[n]=l[i]
                i=i+1
            else:
                lst[n]=r[j]
                j=j+1
            n=n+1

        while i < len(l):
            lst[n]=l[i]
            i=i+1
            n=n+1

        while j < len(r):
            lst[n]=r[j]
            j=j+1
            n=n+1
    print("merging ",lst)

lst = [9,32,1,65,57,93,24,73,3]
mergeSort(lst)
print(lst)
