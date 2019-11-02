# from string import ascii_lowercase

# n=int(input("Enter the Size"))

# width = 4*n - 3
# s = ascii_lowercase[:n]
# s = s[::-1] + s[1:]

# for c in s:
#     pat = s[:s.index(c)]
#     pat = '-'.join(pat + c + pat[::-1])
#     dashes = (width - len(pat)) // 2 * '-'
#     print(dashes + pat + dashes)
def recur_fibo(n):
       
    if n <= 1:
       return n
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))



nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))