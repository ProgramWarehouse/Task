from string import ascii_lowercase

n=int(input("Enter the Size"))

width = 4*n - 3
s = ascii_lowercase[:n]
s = s[::-1] + s[1:]

for c in s:
    pat = s[:s.index(c)]
    pat = '-'.join(pat + c + pat[::-1])
    dashes = (width - len(pat)) // 2 * '-'
    print(dashes + pat + dashes)
