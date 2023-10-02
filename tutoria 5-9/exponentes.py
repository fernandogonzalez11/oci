def exponenciar(base, exp):
    if exp == 1:
        return base
    elif exp % 2 == 0:
        return exponenciar(base, exp//2)**2
    else:
        return base*exponenciar(base, (exp-1)//2)**2

print(exponenciar(3, 3))