
def func(a, b, c):
    return a + b + c

func(*(1, 2, 3))
func(**{'x': 1, 'y': 2, 'z': 3})