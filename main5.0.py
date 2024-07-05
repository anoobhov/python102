arr=list()
arr.append(9)
arr.append(13)
arr.append(1)
arr.append(4)
print(arr)
arr.insert(3,2)
arr.sort(reverse=True)
print(arr)
arr.pop(2)

arr2=arr
print(arr2)
arr2[1]=0
print(arr2,arr)     #wtf why both change?? that's because arr is referring to the same address and when i did
                    #arr2 = arr,arr2 is too now referring to the same array.But would i copy an array?????
arr2=arr.copy()
arr2[1]=1
print(arr2,arr)     #done