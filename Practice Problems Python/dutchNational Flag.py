A = [0,1,2,2,1,0,2,0,1]
def arrayMeth(array):
    zeroes = 0
    ones = 0
    twos = 0
    totalArray = []
    for num in range(len(array)):
        if array[num] == 0:
            zeroes += 1
            print("added zero")
        elif array[num] == 1:
            ones += 1
            print("added one")
        elif array[num] == 2:
            twos += 1
            print("added two")
    for i in range(zeroes):
        totalArray.append(0)
    for i in range(ones):
        totalArray.append(1)
    for i in range(twos):
        totalArray.append(2)
    print(totalArray)
arrayMeth(A)