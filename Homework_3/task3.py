def multiply_2_max(var1, var2, var3, *args, **kwargs):
    """Multiplys 2 vars except the small one. Input: 3 numbers."""
    sorlist = sorted([var1, var2, var3])
    otv = sorlist[1] * sorlist[2]
    print(otv)

multiply_2_max(9, 5, 8)
multiply_2_max(4, 5, 3)