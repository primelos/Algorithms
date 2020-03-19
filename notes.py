# def rec_factorial(n):
#     print(n)
#     if n <= 1:
#         return 1

    
#     prev = rec_factorial(n - 1)
#     return n *prev

# print(rec_factorial(150))

# def fib(n):
#   if n == 1:
#     return 1 # start at 0 or 1 up to you
#   elif n == 2:
   
#     return 1
#   elif n > 2:
#     return fib(n-1) + fib(n-2)
# # print(fib(10))
# for n in range(5, 6):
#   print(n, ':', fib(n))

cache = { 0: 1, 1: 1}
def fib(n):
  if n in cache:
    return cache [n]
  n_minus_1 = fib(n-1)
  n_minus_2 = fib(n-2)
  cache[n] = n_minus_1 + n_minus_2
  return cache[n]
print(fib(10))
# for n in range(5, 6):
#   print(n, ':', fib(n))