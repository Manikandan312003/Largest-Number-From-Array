def largestNumber(a):
    s = [a[0]]
    for i in a[1:]:
        b = list(s)
        c = int("".join(map(str, b)))
        w = []
        for j in range(len(s) + 1):
            b.insert(j, i)
            d = int("".join(map(str, b)))
            if d < c:
                s = list(w)
                break
            w = list(b)
            b = list(s)
            c = d
        s = list(w)
    return "".join(list(map(str,s)))
print(largestNumber(list(map(int,input().split()))))
