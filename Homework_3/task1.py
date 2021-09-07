def division_even_zero(arg1, arg2, *args, **kwargs):
    try:
        otv = arg1 / arg2
    except ZeroDivisionError:
       print('u should not devide on zero =)')
       otv = None
    return(otv)

arg1 = int(input("type any number: "))
arg2 = int(input("type any number: "))
g = division_even_zero(arg1, arg2)
print(g)