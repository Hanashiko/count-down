def count_down(i):
    print(i)
    if i <= 0:
        return
    else:
        count_down(i-1)

count_down(6)
