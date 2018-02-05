import math

f = open("image.ppm", "w+")
f.write("P3 500 500 255")

for i in range(500):
    for j in range(500):
        x = 0
        y = 0
        z = 0
        if( ((i * j) / 2) > i + j):
            x = math.sqrt(i * j)
            y = math.sqrt(i) + math.sqrt(j)
        else:
            x = math.sqrt(i + j)
            y = math.sqrt(i * j)
        z = math.sqrt(i + j * 5)
        f.write(str(x) + " ");
        f.write(str(y) + " ");
        f.write(str(z) + " ");
