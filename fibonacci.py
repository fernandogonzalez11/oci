def fibonacci(n, i, anterior, resultado):
    if n == 1:
        return print(0)
    elif i == n:
        return print(resultado)
        
    fibonacci(n, i+1, resultado, anterior+resultado)
    
fibonacci(3,2,0,1)