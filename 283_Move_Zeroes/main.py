#! /home/efe/anaconda3/bin/python3

arr = [0,0,12,8,9,11,43,5,0,6]

print(arr)

i = 0
while i < len(arr):
    if arr[i] == 0:
        j = i+1
        while j < len(arr):
            if arr[j] != 0:
                arr[i] = arr[j]
                arr[j] = 0
                i += 1
            j += 1
    i += 1

print(arr)
