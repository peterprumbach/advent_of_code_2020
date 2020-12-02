numbers = []

with open('1/numbers') as file:
    numbers = list(map(int, file.readlines()))

#Puzzle 1.1
for i in numbers:
    for j in numbers:
        if(i+j==2020):
            print(i*j)

#Puzzle 1.2
for i in numbers:
    for j in numbers:
        for k in numbers:
            if(i+j+k==2020):
                print(i*j*k)