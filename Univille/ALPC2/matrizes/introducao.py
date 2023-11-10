M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

l = 0
while l < len(M):
  c = 0
  while c < len(M[l]):
    print(M[l][c])
    c += 1
  l += 1
  
"""   
for l in M:
  for c in l:
    print(c)
 """