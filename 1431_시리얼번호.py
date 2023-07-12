n = int(input())
L = []
for i in range(n):
    L.append(input())
for i in range(n-1):
    for j in range(i+1, n):
        if len(L[i]) > len(L[j]):
            L[i],L[j] = L[j],L[i]
        
        elif len(L[i]) == len(L[j]):
            sum_a = 0
            sum_b = 0
            for a,b in zip(L[i],L[j]):
                if a.isdigit():
                    sum_a += int(a)
                if b.isdigit():
                    sum_b += int(b)
            if sum_a > sum_b:
                L[i],L[j] = L[j],L[i]
            
            elif sum_a == sum_b:
                for a,b in zip(L[i],L[j]):
                    if a > b:
                        L[i],L[j] = L[j],L[i]
                        break
                    elif a < b:
                        break

for i in L:
    print(i)     
