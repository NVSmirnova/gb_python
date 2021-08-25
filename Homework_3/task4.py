def koren(base, stepen, *args, **kwargs):
    if(stepen < 0):
        print(base ** (-1/stepen))
    else:
        print(base ** (1/stepen))

koren(27, -3)
