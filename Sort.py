import time
import winsound

def countingSort(array, place, drawData):
    size = len(array)
    output = [(0, "")] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i][0] // place
        count[index % 10] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]


    i = size - 1
    while i >= 0:
        index = array[i][0] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1


    for i in range(0, size):
        array[i] = output[i]
        drawData()

def playSound(frequency):
    winsound.Beep(frequency*100,100)

def radixSort(array, drawData):
    max_element = 95
    place = 1
    while max_element // place > 0:
        countingSort(array, place, drawData)
        playSound(10)
        place *= 10

def Sort_Tuple(tup, drawData):  
    lst = len(tup)  
    for i in range(0, lst):
        playSound(10)  
        for j in range(0, lst-i-1):
            if (tup[j][0] > tup[j + 1][0]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp 
                drawData()
