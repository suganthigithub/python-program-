
def fiboncci(count):
 
    fib_list=[0,1]

any(map(lambda_: fib_list.append(sum(fib_list[-2:])),range(2,count)))

return fib_list[:count]

print(fibonacci(50))