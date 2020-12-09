numbers = []

with open('9/numbers') as file:
    numbers = list(map(int, file.readlines()))

preamble=[]
for i in range(0, 25):
    preamble.append(numbers[i])

search=[]
for i in range(25, len(numbers)):
    search.append(numbers[i])

result = []

for i in search:
    for j in preamble:
        for k in preamble:
            if(j+k!=i):
                result.append(i)
                return

print(result[0])