for counter in range(5):
    print(counter, 2 * counter)
print()
for counter in range(5):
    print(counter, 2 * counter, sep=",", end=".\n")

for counter in range(1, 11):    # counter = 1, 2, 3, ..., 10
    print(counter, end=" ")
print()
for counter in range(10):       # counter = 0, 1, 2, 3, ..., 9
    print(counter + 1, end=" ")
print()
# counter = 7, 14, 21, 28, ..., 70
for counter in range(7, 71, 7):
    print(counter, end = " ")
'''
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    ...
    7 x 10 = 70
'''
print()
for counter in range(1, 11, 1):
    print("7 x", counter, "=", counter * 7)
print()
counter = 1
while counter < 11:
    print("7 x", counter, "=", counter * 7)
    # counter = counter + 1
    counter += 1

# Saludar al mundo 100 veces
for counter in range(1, 101):   # counter = 1, 2, 3, ..., 99, 100
    print(counter, "Hola mundo")
print()
for counter in range(100):      # counter = 0, 1, 2, ..., 98, 99
    print(counter, "Hola mundo")
print()
for counter in range(2, 20, 3): # counter = 2, 5, 8, 11, 14, 17
    print(counter, end=" ")
print()
for counter in range(100, 30, -10):  # counter = 100, 90, 80, 70, 60, 50, 40
    print(counter, end=" ")
# counter = 15, 30, 45, 60, 75, 90
print()
for counter in range(15, 91, 15):
    print(counter, end=" ")
print()
# counter = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
for counter in range(10):
    print(counter, end=" ")
for counter in range(10, -1, -1):
    print(counter, end=" ")
print()

for row in range(1, 4):
    # row = 1, 2, 3
    for col in range(6, 9):
        # col = 6, 7, 8
        print("(", row, ",", col, ")", sep="")
        print("(", col, ",", row, ")", sep="")
print()
for i in range(10):         # i = 0, 1, 2, ..., 9
    for j in range(10):     # j = 0, 1, 2, ..., 9
        for k in range(10): # k = 0, 1, 2, ..., 9
            print(i, j, k)
'''
    i = 0
        j = 0
            k = 0, (0, 0, 0)
            k = 1, (0, 0, 1)
            k = 2, (0, 0, 2)
            :
            k = 9, (0, 0, 9)
        j = 1
            k = 0, (0, 1, 0)
            k = 1, (0, 1, 1)
            :
            k = 9, (0, 1, 9)
        :
        j = 9
            k = 0, (0, 9, 0)
            k = 1, (0, 9, 1)
            :
            k = 9, (0, 9, 9)
    i = 1
        j = 0
            k = 0, (1, 0, 0)
    :
    i = 9
        j = 9
            k = 9, (9, 9, 9)
'''

# Calcular la sumatoria de los números comprendidos entre A y B
# Si A = 5, B = 9, sumatoria = 5 + 6 + 7 + 8 + 9 = 35
A = 1
B = 100
S = 0
for counter in range(A, B + 1):  # counter = 5, 6, 7, 8, 9
    S = S + counter      # x = x + A <---> x += A
    #S += counter

print("Sumatoria: ", S)


