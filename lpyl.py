matches = int(input())

rate = list(map(int, input().split(' ')))
print(rate)
def max_subarray(array):
    max = 0
    currentMax = 0
    for i in range(len(array)):
        currentMax += array[i]
        if currentMax < 0:
            currentMax = 0
        if max < currentMax:
            max = currentMax
    return max


print(max_subarray(rate))
