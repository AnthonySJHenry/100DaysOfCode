def reverseArray(a):
    arx = []
    
    for x in range(len(a)-1, -1, -1):
        arx.append(a[x])
    return arx
        
arr = [2, 5, 6, 7]
print(reverseArray(arr))