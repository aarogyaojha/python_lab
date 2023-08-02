nlist = []


def mergesort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        left = nlist[:mid]
        right = nlist[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nlist[k] = left[i]
                i += 1
            else:
                nlist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nlist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nlist[k] = right[j]
            j += 1
            k += 1


n = int(input("enter the number"))
for i in range(n):
    num = int(input())
    nlist.append(num)

mergesort(nlist)
print(nlist)
