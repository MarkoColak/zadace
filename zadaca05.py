def funkcija(n):
    for i in range(n):
        if i % 2 == 0 or i % 2 != 0:
            yield i

    iterator = iter(funkcija(20))


    while 1:
        try:
            print(next(iterator))
        except:
            break

funkcija(20)
