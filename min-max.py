arr = [1, 4, 3, 5, 8, 6]

minimum = arr[0]
maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]

print(minimum, maximum)
