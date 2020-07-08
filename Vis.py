import random
from tkinter import *
from tkinter import ttk
from Sort import Sort_Tuple, radixSort
from HSV import hsv

HSV = []
sortList = []
num = 256
hsv(HSV, num)

for i in range(96):
    sortList.append(i)

sortHSV = list(zip(sortList, HSV))
random.shuffle(sortHSV)

root = Tk()
root.maxsize(1280, 720)
root.config(bg="grey")
UI_frame = Frame(root, width=100, height=50, bg='white')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.grid(row=1, column=0, padx=140, pady=60)


def drawData():
    canvas.delete("all")
    cHeight = 400
    cWidth = 600
    xWidth = float(cWidth / len(sortHSV))
    for i in range(len(sortHSV)):
        x0 = xWidth * i
        y0 = 0
        x1 = cWidth
        y1 = cHeight
        canvas.create_rectangle(x0,y0,x1,y1, fill=sortHSV[i][1], outline="")
    root.update()

def startAlgR():
    radixSort(sortHSV, drawData)

def startAlgB():
    Sort_Tuple(sortHSV, drawData)

Button(UI_frame, text="Generate", command=drawData, bg='red').grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="RadixSolution", command=startAlgR, bg='red').grid(row=1, column=2, padx=5, pady=5)
Button(UI_frame, text="BubbleSolution", command=startAlgB, bg='red').grid(row=2, column=2, padx=5, pady=5)

root.mainloop()