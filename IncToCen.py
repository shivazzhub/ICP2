L = input().split()
# 1 inch = 2.54 cm
res=[]
for i in range(0,len(L)):
  res.append(float(L[i])*2.54)
print(res)
