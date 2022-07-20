from function.sum import sum
from function.factorial import factorial
from function.product import product
from function.prime import prime
from function.merge_sort import merge_sort

print(sum.sum(5, 6));
print(product.product(5, 6))
print(factorial.factorial(6))
print(prime.prime(7))
arr = [4, 3, 6, 1, 2, 9, 12, 2, 5]
print(merge_sort.merge_sort(arr, 0, len(arr)-1))