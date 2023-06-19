import os
x = 0
y = 'C:/'
while x<40:
    x = x + 1
    z = y + str(x)
    r = str(z)+'/'
    os.mkdir(r)