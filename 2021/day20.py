import numpy as np

f = open('input.txt')

algo = f.readline()
algo = algo.strip()

line = f.readline() # blank
line = f.readline()

size = 5
size = 100

img = np.zeros((size+110, size+110), dtype = int)

row = 51
while line:
    line = line.strip()
    for col in range(len(line)):
        if line[col] == '1':
            img[row, col+51] = 1

    line = f.readline()
    row += 1

#print(img)

offset = 0

for loop in range(50):
    if loop % 2 == 0:
        newimg = np.ones((size+110, size+110), dtype = int)
    else:
        newimg = np.zeros((size+110, size+110), dtype = int)
    #newimg = np.zeros((size+110, size+110), dtype = int)

    for row in range(1, size+109):
        for col in range(1, size+109):
            sub = img[row-1:row+2, col-1:col+2]

            bits = ''
            for r in range(3):
                for c in range(3):
                    bits += str(sub[r, c])
            idx = int(bits, 2)
            newimg[row, col] = algo[idx]

        #exit(0)

    img = newimg

    print(loop, np.sum(newimg))
