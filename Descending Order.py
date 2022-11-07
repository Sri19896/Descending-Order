def descending_order(num):
    if num < 0:
        print('error')
    else:
        l = str(num)
        s = list()
        for i in l:
            s.append(i)
    s = sorted(s, reverse=True)
    return (int('6'.join(s)))


print(descending_order(42145))
